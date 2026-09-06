"""Run real sibling component demos; no fused prediction is claimed."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace',type=Path,default=Path(__file__).resolve().parents[2])
    parser.add_argument('--recognition-python',type=Path,required=True)
    parser.add_argument('--include-risk',action='store_true')
    parser.add_argument('--risk-python',type=Path)
    parser.add_argument('--out',type=Path,default=Path('runs/component-demo.json'))
    args=parser.parse_args()
    if args.include_risk and not args.risk_python: parser.error('--include-risk requires --risk-python')
    specs=[('cowmata-tailring',args.recognition_python,['-m','cowmata','predict','--cache-key','demo_session_60s','--data-root','examples/demo_data','--out','runs/system-demo'])]
    if args.include_risk: specs.append(('cowmata-risk',args.risk_python,['examples/calving_evidence_demo.py']))
    for repo,python,_ in specs:
        if not (args.workspace/repo/'.git').exists(): parser.error('Missing checkout: '+repo)
        if not python.is_file(): parser.error('Missing Python executable: '+str(python))
    env=os.environ.copy();env['PYTHONIOENCODING']='utf-8'
    report={'schema_version':1,'fused_pipeline':False,'risk_demo_selected':args.include_risk,'components':[]}
    for repo,python,command in specs:
        root=(args.workspace/repo).resolve()
        commit=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip()
        result=subprocess.run([str(python.resolve()),*command],cwd=root,env=env,encoding='utf-8',capture_output=True)
        dirty=bool(subprocess.check_output(['git','-C',str(root),'status','--porcelain'],text=True).strip())
        row={'repository':repo,'commit':commit,'working_tree_dirty':dirty,
             'returncode':result.returncode,'stderr':result.stderr.strip()}
        try: row['output']=json.loads(result.stdout)
        except json.JSONDecodeError: row['output']=result.stdout;row['parse_error']=True
        report['components'].append(row)
    success=all(r['returncode']==0 and not r.get('parse_error') for r in report['components'])
    report['success']=success
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 0 if success else 1


if __name__=='__main__':
    sys.exit(main())
