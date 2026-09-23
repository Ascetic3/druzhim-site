"""Extract compact editable canvas instructions from the existing SVG concepts."""
from pathlib import Path
import json
from xml.etree import ElementTree as ET

ROOT = Path(__file__).parent
S = '{http://www.w3.org/2000/svg}'

def parse(path):
    root=ET.parse(path).getroot()
    board={'name':path.stem,'w':int(root.attrib['width']),'h':int(root.attrib['height']),'shapes':[],'texts':[]}
    for n in root:
        a=n.attrib
        if n.tag==S+'rect':
            board['shapes'].append({'t':'rect','x':float(a['x']),'y':float(a['y']),'w':float(a['width']),'h':float(a['height']),'rx':float(a.get('rx',0)),'fill':a.get('fill','none'),'stroke':a.get('stroke'),'sw':float(a.get('stroke-width',1))})
        elif n.tag==S+'path':
            board['shapes'].append({'t':'path','d':a['d'],'stroke':a.get('stroke','#203C32'),'sw':float(a.get('stroke-width',1))})
        elif n.tag==S+'circle':
            board['shapes'].append({'t':'circle','x':float(a['cx']),'y':float(a['cy']),'r':float(a['r']),'fill':a.get('fill','none'),'stroke':a.get('stroke'),'sw':float(a.get('stroke-width',1))})
        elif n.tag==S+'image':
            board['shapes'].append({'t':'image','x':float(a['x']),'y':float(a['y']),'w':float(a['width']),'h':float(a['height'])})
        elif n.tag==S+'text':
            ts=n.findall(S+'tspan')
            if not ts:continue
            ys=[float(t.attrib['y']) for t in ts]
            board['texts'].append({'copy':'\n'.join((t.text or '') for t in ts),'x':float(a['data-x']),'y':float(a['data-y']),'w':float(a['data-width']),'size':float(a['font-size']),'lh':ys[1]-ys[0] if len(ys)>1 else round(float(a['font-size'])*1.45),'font':a['font-family'],'weight':int(a.get('font-weight',400)),'fill':a['fill'],'align':a.get('text-anchor','start')})
    return board

desktop=[parse(p) for p in sorted((ROOT/'sections').glob('*.svg'))]
mobile=[parse(ROOT/'screens'/n) for n in ['mobile-hero-390.svg','mobile-audience-390.svg','mobile-foster-390.svg','mobile-season-390.svg','mobile-contact-390.svg','mobile-menu-open-390.svg','mobile-faq-390.svg']]
other=[parse(ROOT/'screens'/n) for n in ['system-states.svg','motion-storyboard.svg']]
for name,data in [('desktop',desktop),('mobile',mobile),('other',other)]:
    (ROOT/f'{name}-transfer.json').write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
    print(name,len(data),'boards',sum(len(x['shapes']) for x in data),'shapes',sum(len(x['texts']) for x in data),'texts')
