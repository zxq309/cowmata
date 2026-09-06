"""Rebuild COWMATA architecture SVGs using standard-library Python."""
import argparse
from html import escape
from pathlib import Path

PAPER, INK, MUTED, ACCENT = '#f7faf8', '#17352e', '#59716b', '#0a7ea4'


def diagram(kind, zh):
    def tr(en, cn): return cn if zh else en
    titles = {
        'system': tr('One system. Four focused repositories.', '一个总体项目，四个职责清晰的仓库'),
        'recognition': tr('Continuous sensing → behavior timelines', '连续传感 → 行为与事件时间线'),
        'risk': tr('Calving research starts with traceable evidence', '从可追溯辅助证据，推进产犊综合决策'),
    }
    parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="680" viewBox="0 0 1200 680" role="img" aria-labelledby="title desc">
<title id="title">{escape(titles[kind])}</title><desc id="desc">{tr('Solid arrows: current component flow. Dashed arrows: planned integration. No validated fused alert is claimed.', '实线为当前组件流程，虚线为待实现集成；不表示融合告警已验证。')}</desc>
<defs><marker id="arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="{MUTED}"/></marker><marker id="arrow-accent" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="{ACCENT}"/></marker><marker id="arrow-link" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="{ACCENT}"/></marker></defs>
<style>text{{font-family:'Segoe UI','Microsoft YaHei','Noto Sans CJK SC',sans-serif;fill:{INK}}}.tag{{font-size:12px;letter-spacing:1px;fill:{MUTED}}}.sub{{font-size:16px;fill:{MUTED}}}.name{{font-size:24px;font-weight:600}}.path{{fill:none;stroke:{MUTED};stroke-width:2;marker-end:url(#arrow)}}</style>
<rect width="1200" height="680" fill="{PAPER}"/>
<rect x="40" y="36" width="8" height="24" fill="#92c142"/>
<text x="64" y="56" class="tag">COWMATA / {kind.upper()} / 2026-09-07</text>
<text x="40" y="104" font-size="32" font-weight="600">{escape(titles[kind])}</text>''']
    nodes = []
    def node(x,y,w,h,tag,name,lines,focal=False,planned=False):
        stroke = ACCENT if focal else '#b8ccc4'
        fill = '#edf7fa' if focal else '#ffffff'
        dash = ' stroke-dasharray="6 4"' if planned else ''
        s = f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="2"{dash}/>'
        s += f'<text x="{x+20}" y="{y+28}" class="tag">{escape(tag)}</text><text x="{x+20}" y="{y+64}" class="name">{escape(name)}</text>'
        for i,line in enumerate(lines): s+=f'<text x="{x+20}" y="{y+92+i*24}" class="sub">{escape(line)}</text>'
        nodes.append(s+'</g>')
    def path(d,dashed=False): parts.append(f'<path d="{d}" class="path"'+(' stroke-dasharray="6 4"' if dashed else '')+'/>')
    if kind=='system':
        node(40,184,256,144,'INPUT',tr('Sensing + video','传感数据与同步视频'),[tr('Continuous IMU · temperature','连续 IMU · 温度'),tr('Reviewable observations','可回看、可核对的观测')])
        node(392,184,288,144,'ANNOTATOR',tr('Human review','人工标注与复核'),[tr('Aligned labels and intervals','对齐时间、标签和区间'),tr('Independent desktop tool','独立维护的桌面工具')])
        node(776,184,384,144,'COWMATA-TAILRING',tr('Behavior recognition','行为与事件识别'),[tr('Training · inference · evaluation','训练 · 推理 · 评估'),tr('Event candidates and state timelines','事件候选与状态时间线')],True)
        node(40,424,256,144,'AUXILIARY MODULES',tr('Sensor evidence','传感辅助证据'),[tr('Temperature · activity','温度 · 活动量'),tr('Current calving experiments','当前产犊实验模块')])
        node(392,424,288,144,'COWMATA-RISK / PRIVATE',tr('Decision research','综合决策研究'),[tr('Evidence modules available','辅助证据模块已接入'),tr('Fusion under development','融合决策待开发')],True)
        node(776,424,384,144,'ROADMAP',tr('Farm risk monitoring','牧场风险监测'),[tr('Calving · estrus · pregnancy · health','产犊 · 发情 · 妊娠 · 健康'),tr('Unified alerts remain planned','统一告警仍属规划')],planned=True)
        path('M168 184 V160 Q168 152 176 152 H960 Q968 152 968 160 V184')
        parts.append('<text x="448" y="140" class="sub">'+tr('Raw sensing for recognition','原始传感数据用于识别')+'</text>')
        path('M296 256 H392');path('M680 256 H776');path('M168 328 V424');path('M296 496 H392')
        path('M968 328 V368 Q968 376 960 376 H544 Q536 376 536 384 V424',True)
        path('M680 496 H776',True)
    elif kind=='recognition':
        labels=[('INPUT',tr('Continuous IMU','连续 IMU'),[tr('Absolute time · quality · gaps','绝对时间 · 质量 · 缺口')]),
                ('PREPROCESS',tr('Safe segments','连续段预处理'),[tr('Calibrate before windowing','先标定，再生成训练窗口')]),
                ('MODEL',tr('Temporal models','时序识别模型'),['GBDT / MS-TCN++']),
                ('POSTPROCESS',tr('Event assembly','事件组装'),[tr('Thresholds · state logic','阈值 · 站卧状态逻辑')]),
                ('OUTPUT',tr('Behavior timeline','行为事件时间线'),[tr('States · intervals · scores','状态 · 区间 · 分数')]),
                ('REVIEW',tr('Human confirmation','人工复核'),[tr('Candidate queue → annotator','候选队列 → 标注工具')])]
        positions=[(40,184),(432,184),(824,184),(824,424),(432,424),(40,424)]
        for i,((tag,name,lines),(x,y)) in enumerate(zip(labels,positions)): node(x,y,336,128,tag,name,lines,focal=i in [2,4])
        path('M376 248 H432');path('M768 248 H824');path('M992 312 V424');path('M824 488 H768');path('M432 488 H376')
    else:
        node(40,264,256,144,'V2 PACKET',tr('Bound stream','已绑定传感数据'),[tr('Cow · device · binding','牛只 · 设备 · 绑定'),tr('Receipt and evaluation time','接收时间与决策时间')])
        node(392,168,336,144,'TEMPERATURE / 0.6.0',tr('Temperature evidence','温度辅助证据'),[tr('Personal reference · cooling','个体参照 · 持续温降'),tr('Score + freshness weight','证据评分与时效权重')],True)
        node(392,392,336,144,'ACTIVITY / 1.0.0',tr('Activity evidence','活动量辅助证据'),[tr('Dynamic baseline · activity ratio','动态基线 · 活动比值'),tr('Coverage + evidence quality','观测覆盖与证据质量')],True)
        node(824,264,336,144,'NEXT / NOT IMPLEMENTED',tr('Calving fusion','产犊融合决策'),[tr('Combine evidence and events','联合辅助证据与行为事件'),tr('Calibrate and validate alerts','标定并验证统一告警')],planned=True)
        path('M296 304 H336 Q344 304 344 296 V248 Q344 240 352 240 H392')
        path('M296 368 H328 Q336 368 336 376 V456 Q336 464 344 464 H392')
        path('M728 240 H768 Q776 240 776 248 V296 Q776 304 784 304 H824',True)
        path('M728 464 H760 Q768 464 768 456 V376 Q768 368 776 368 H824',True)
    parts.extend(nodes)
    parts.append(f'<line x1="40" y1="616" x2="1160" y2="616" stroke="#cfddd7"/><text x="40" y="648" class="sub">'+escape(tr('Solid: current component flow   ·   Dashed: planned integration   ·   Evidence is not a calibrated risk probability', '实线：当前组件流程　·　虚线：待实现集成　·　辅助证据不等于已标定风险概率'))+'</text></svg>')
    return '\n'.join(parts)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--kind',choices=['system','recognition','risk'],required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    for language in ['en','zh']:
        (args.out/(args.kind+'-'+language+'.svg')).write_text(diagram(args.kind,language=='zh'),encoding='utf-8')
