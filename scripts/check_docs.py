"""Check local documentation links, SVG syntax and bilingual update dates."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote
import xml.etree.ElementTree as ET


def check(root):
    errors=[]
    ignored={'.git','.venv','__pycache__','build','dist'}
    for p in root.rglob('*'):
        if any(part in ignored for part in p.relative_to(root).parts) or not p.is_file(): continue
        if p.suffix=='.svg':
            try: ET.parse(p)
            except ET.ParseError as e: errors.append(str(p)+': '+str(e))
        if p.suffix not in {'.md','.html'}: continue
        text=p.read_text(encoding='utf-8-sig')
        links=re.findall(r'\]\(([^)]+)\)',text)+re.findall(r'(?:src|href)="([^"]+)"',text)
        for link in links:
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',link) or link.startswith(('#','//')): continue
            target=unquote(link.split('#')[0].split('?')[0])
            if not target or '{' in target: continue
            if not (p.parent/target).exists(): errors.append(str(p.relative_to(root))+': missing '+target)
    dates=re.findall(r'\b20\d{2}-\d{2}-\d{2}\b',(root/'CHANGELOG.md').read_text(encoding='utf-8'))
    newest=max(dates)
    for name in ['README.md','README.zh-CN.md']:
        text=(root/name).read_text(encoding='utf-8')
        match=re.search(r'## (?:Latest update|最新更新)\n(.*?)(?=\n## |\Z)',text,re.S)
        if not match or newest not in match.group(1): errors.append(name+': latest-update date differs from CHANGELOG '+newest)
    if errors:
        print('\n'.join(errors));return 1
    print('PASS: local links, SVG syntax, bilingual maintenance date '+newest)
    return 0


if __name__=='__main__':
    sys.exit(check(Path(__file__).resolve().parents[1]))
