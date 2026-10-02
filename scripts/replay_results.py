"""Offline current-draft point-estimate and sharp-bound replay; no API calls."""
import argparse
import csv
import json
from pathlib import Path
import numpy as np
from scipy.stats import rankdata, spearmanr

ROOT=None
RESULTS=Path(__file__).resolve().parents[1]/'results'

def partial(x,y,z):
    ranks=np.column_stack([rankdata(x),rankdata(y)])
    design=np.column_stack([np.ones(len(x)),z])
    residual=ranks-design@np.linalg.lstsq(design,ranks,rcond=None)[0]
    return float(np.corrcoef(residual.T)[0,1])

def weights(scores,k):
    boundary=np.partition(scores,len(scores)-k)[len(scores)-k]
    above,tied=scores>boundary,scores==boundary
    return above.astype(float)+tied*((k-above.sum())/tied.sum())

def main():
    global ROOT
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir', type=Path, required=True, help='Eligible locally held numeric inputs; see INPUTS.md')
    ROOT=parser.parse_args().data_dir
    with (ROOT/'verified_link_rows.csv').open() as f:rows=list(csv.DictReader(f))
    a=np.array([[float(r[k]) for k in ('year','accepted','tns','ens','recommendation','cumulative_log_citations','fixed24_log_citations')] for r in rows])
    expected=json.loads((RESULTS/'corrected_results.json').read_text())
    assert len(rows)==expected['joint_n']==3443
    for key,col in [('primary',5),('fixed24',6)]:
        values=[partial(a[:,j],a[:,col],a[:,:2]) for j in (2,3,4)]
        values.append(values[1]-values[0])
        np.testing.assert_allclose(values,expected[key]['partials_and_ENS_minus_TNS'],atol=1e-12)
        np.testing.assert_allclose([spearmanr(a[:,j],a[:,col]).statistic for j in (2,3,4)],expected[key]['raw'],atol=1e-12)
    for p in expected['selection']:
        mask=(a[:,0]==p['year'])
        if p['stage']!='all':mask &= a[:,1]==int(p['stage']=='accepted')
        pool=a[mask];k=max(1,round(len(pool)*.1));positive=pool[:,6]>=np.quantile(pool[:,6],.75)
        assert len(pool)==p['n'] and k==p['k']
        np.testing.assert_allclose([weights(pool[:,j],k)@positive/k for j in (2,3,4)],p['precision'],atol=1e-12)
    union=json.loads((ROOT/'score_observed_population.json').read_text())
    bounds=json.loads((RESULTS/'missing_outcome_bounds.json').read_text())
    known={r['forum']:float(r['fixed24_log_citations']) for r in rows}
    checked=0
    for p in bounds['panels']:
        pool=[r for r in union if r['year']==p['year'] and (p['stage']=='all' or r['accepted']==int(p['stage']=='accepted'))]
        score=np.array([r['scores'] for r in pool]); k=max(1,round(len(pool)*.1))
        observed=np.array([r['forum'] in known for r in pool]);threshold=np.quantile(a[a[:,0]==p['year'],6],.75)
        y=np.array([known[r['forum']]>=threshold if r['forum'] in known else np.nan for r in pool])
        assert len(pool)==p['n'] and int(observed.sum())==p['known_outcomes']
        for name,first,second in [('ENS_minus_TNS',1,0),('Recommendation_minus_ENS',2,1)]:
            d=(weights(score[:,first],k)-weights(score[:,second],k))/k
            fixed=d[observed]@y[observed]
            value=[fixed+np.minimum(d[~observed],0).sum(),fixed+np.maximum(d[~observed],0).sum()]
            np.testing.assert_allclose(value,p['contrasts'][name]['bounds'],atol=1e-12);checked+=2
    print(json.dumps({'status':'PASS','current_joint_rows':len(rows),'selection_panels':len(expected['selection']),
                      'bound_endpoints':checked,'uncertainty':'Frozen intervals retained; this fast replay does not rerun bootstraps or fit secondary models.'},indent=2))

if __name__=='__main__':main()
