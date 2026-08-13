from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

repo = Path(sys.argv[1]).resolve()
S = repo / "submissions/andyxu12341/jingzhang-city-timetable"


def replace_section(path: Path, heading: str, next_heading: str, body: str) -> None:
    text = path.read_text(encoding="utf-8")
    start = text.index(heading)
    end = text.index(next_heading, start + len(heading))
    new_text = text[:start] + heading + "\n\n" + body.strip() + "\n\n" + text[end:]
    path.write_text(new_text, encoding="utf-8")


zh_blue = r'''概念绿地层按 provisional boundary 复算 `green_ratio=31.5058%`，不是批准绿地率 [metric:green_ratio]；六处可逆公共空间概念比例约 1.4959% [metric:public_space_ratio]。本方案不把蓝绿系统当作静态“背景绿量”，而把它作为 T0 恒定权利的低技术底板：连续步行、无障碍、遮阴停留、安静空间和应急通行优先于任何 T2/T3 活动。京张一期已经建成开放、二期配套已形成新的慢行网络，因此近期设计重点是识别可进入、可停留、可切换与必须始终保持通畅的空间，而不是先新增大体量构筑物 [source:JZ-PARK-PHASE1-OFFICIAL] [source:JZ-PARK-PHASE2-2026]。

公共空间的时权表达通过 `geometry/green_space.geojson` 与 `geometry/public_space.geojson` 的概念图层建立索引，六处时序空间只承担“规则可被看见和测试”的示范，不以 1.4959% 作为规划目标 [data:geometry/public_space.geojson#PUBLIC-001]。每个节点都应同时说明 T0 连续路径、可预约边界、安静时段、人工责任和失败回退；正式道路断面、树木现状、排水、市政、照明、文保和真实使用强度到位后再校核尺度与材料。城市风貌以“**空间权利 + 时间权利**”为叙事：铁路时刻轴、站点、会让线和恢复逻辑转译为导视、铺装、公共信息与活动系统，而不是用通用科技蓝光代替京张历史 [standard:MOHURD-URBAN-DESIGN-MEASURES]。'''

zh_phase = r'''实施策略遵循“**先运营验证，后空间扩展；先可逆小试，后资本建设**”。近期第一项目是 **AI 原点 × 京张一期 TIME RIGHTS 1.0**：先完成 P0 两周人工基线，再进入 P1 四周可逆小试，同步部署 TimeSlot Contract、公开时权表、T0 无障碍/应急校核和免 App 导航；其场地依据来自已建成开放的京张一期 [source:JZ-PARK-PHASE1-OFFICIAL]，机器可读协议位于 `visual/assets/ai-origin-time-rights-pilot.json` [data:visual/assets/ai-origin-time-rights-pilot.json]。近期项目还包括三重点区时权界面样机、公开状态牌、人工接管演练与 Annual Time Rights Review，均优先使用现有公共空间和可撤除设施。

中期只有在 official polygon、道路/站口、真实人流、活动、物流、市政与管理边界补齐后，才把 P0/P1 的现场基线替换当前 proof 假设，重新计算冲突分钟、时序可达和空间可用率 [metric:peak_conflict_reduction_ratio]。若 T0 连续性、非 AI fallback、投诉响应或具名责任任何一项不达标，项目停留在 P0/P1，不进入扩展。远期才讨论更高等级具身智能公共运行、重点区空间改造和跨片区联动，前提是交通、安全、规划、市政、文保、权属与运营许可分别取得专业确认。该分期因此既是建设时序，也是“证据成熟度—授权等级”的升级路径 [depth:phasing_implementation]。'''

zh_risk = r'''官方 polygon 缺失，所有 provisional-derived 数量和落位须重算 [source:OFFICIAL-ANNOUNCEMENT]。FAR、高度、道路、市政、文保、权属不自行推定 [standard:MOHURD-CONTROL-DETAILED-PLANNING]。AI 原点 Pilot 尚未授权、尚未运行，所有 Gate 均为待验证目标 [data:visual/assets/ai-origin-time-rights-pilot.json]。机器人测试不等于公共部署许可；-70%、+25.9pp、+5.7% 等情景模型结果不等于现场绩效 [metric:peak_conflict_reduction_ratio]。基本公共服务不依赖人脸识别、持续个人追踪、强制 App 或单一供应商；任何现场数据采集优先采用聚合计数和人工观察。核心图和模型为本方案原创/程序化生成，版权说明见 `report/copyright_statement.md`。'''

replace_section(S / "proposal.md", "## 蓝绿空间、公共空间与城市风貌", "## 更新项目清单、实施政策与分期计划", zh_blue)
replace_section(S / "proposal.md", "## 更新项目清单、实施政策与分期计划", "## 指标体系、面积复算与合规矩阵", zh_phase)
replace_section(S / "proposal.md", "## 风险、版权与合规说明", "## 参考资料", zh_risk)

# Keep the bilingual companion substantively aligned with the stronger implementation logic.
en_blue = r'''On provisional geometry, the conceptual green-layer ratio is 31.5058% and six timetable public spaces represent about 1.4959%; neither is an approved statutory ratio [metric:green_ratio] [metric:public_space_ratio]. The blue-green system is treated as the low-tech substrate of T0 Constant Rights rather than decorative background: continuous walking, accessibility, shade/rest, quiet space and emergency passage take priority over any T2/T3 activation. Phase I is already open and Phase II supporting works add a slow-mobility network, so the near-term design task is to identify spaces that may switch state and spaces that must remain continuously passable, rather than beginning with large new structures [source:JZ-PARK-PHASE1-OFFICIAL] [source:JZ-PARK-PHASE2-2026].

The conceptual green/public-space GeoJSON provides a traceable index, not a statutory plan [data:geometry/public_space.geojson#PUBLIC-001]. Each timetable node must show the T0 route, reservable edge, quiet window, accountable human and rollback state. Street sections, trees, drainage, utilities, lighting, heritage controls and observed use intensity remain field/professional data gaps. Urban character translates railway time axes, station points, meet/pass and recovery logic into signage, paving, public information and event language rather than generic “future-tech” styling [standard:MOHURD-URBAN-DESIGN-MEASURES].'''

en_phase = r'''Implementation follows **operate and verify before expanding space; reversible pilot before capital construction**. The first near-term project is AI Origin × Jing-Zhang Phase I TIME RIGHTS 1.0: a two-week P0 human baseline followed by a four-week P1 reversible trial, together with the TimeSlot Contract, public Time Rights display, T0 accessibility/emergency checks and no-app navigation. The built/open Phase I is the site evidence [source:JZ-PARK-PHASE1-OFFICIAL], while the machine-readable pilot protocol is `visual/assets/ai-origin-time-rights-pilot.json` [data:visual/assets/ai-origin-time-rights-pilot.json]. Other near-term outputs are key-area rule interfaces, public status boards, human-takeover drills and an Annual Time Rights Review, using existing public space and removable equipment first.

Mid term begins only after official polygons, roads/station access, observed pedestrian activity, logistics, utilities and management boundaries are available; P0/P1 field baselines then replace proof assumptions and temporal conflict/accessibility are recalculated [metric:peak_conflict_reduction_ratio]. Failure of T0 continuity, non-AI fallback, complaint response or named accountability holds the project at P0/P1. Long-term embodied-AI public operation and spatial reconstruction require separate traffic, safety, planning, utility, heritage, ownership and operating confirmation. Phasing is therefore also an evidence-maturity and authorization ladder [depth:phasing_implementation].'''

en_risk = r'''Official polygons remain missing, so provisional-derived quantities and placements require recalculation [source:OFFICIAL-ANNOUNCEMENT]. FAR, height, roads, utilities, heritage and ownership are not invented [standard:MOHURD-CONTROL-DETAILED-PLANNING]. The AI Origin pilot is proposed, not authorized or run [data:visual/assets/ai-origin-time-rights-pilot.json]. Robotics testing is not deployment permission, and scenario-model outputs such as the 70% conflict reduction are not observed field performance [metric:peak_conflict_reduction_ratio]. Essential service does not depend on facial recognition, persistent tracking or a mandatory app; field evidence defaults to aggregate counts and human observation. Core figures/models are original or programmatically generated; see `report/copyright_statement.md`.'''

replace_section(S / "proposal.en.md", "## Blue-Green Network, Public Space, and Urban Character", "## Renewal Projects, Implementation Policy, and Phasing", en_blue)
replace_section(S / "proposal.en.md", "## Renewal Projects, Implementation Policy, and Phasing", "## Metrics, Area Recalculation, and Compliance Matrix", en_phase)
replace_section(S / "proposal.en.md", "## Risk, Copyright, and Compliance", "## References", en_risk)

# Unify optional derived summary branding when present.
for rel in ["report/narrative.md", "visual/index.html", "visual/index.en.html"]:
    p = S / rel
    if p.exists():
        t = p.read_text(encoding="utf-8")
        t = t.replace("京张运行图 · THE CITY TIMETABLE", "京张时权 · THE CITY TIMETABLE")
        t = t.replace("京张运行图", "京张时权")
        p.write_text(t, encoding="utf-8")

# Register bilingual SVG assets. Hashes are refreshed after rendering/self-check as well.
manifest_path = S / "manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
files = manifest.setdefault("files", [])
by_path = {item.get("path"): item for item in files}

pairs = [
    ("assets/figures/ai-origin-pilot.svg", "assets/figures/ai-origin-pilot.en.svg"),
    ("assets/figures/time-rights-hero.svg", "assets/figures/time-rights-hero.en.svg"),
    ("assets/figures/temporal-network-method.svg", "assets/figures/temporal-network-method.en.svg"),
    ("assets/figures/street-section-24h.svg", "assets/figures/street-section-24h.en.svg"),
    ("assets/figures/key-areas-24h.svg", "assets/figures/key-areas-24h.en.svg"),
    ("assets/figures/temporal-proof-results.svg", "assets/figures/temporal-proof-results.en.svg"),
]

for primary, counterpart in pairs:
    if primary not in by_path:
        item = {"path": primary, "role": "proposal_figure", "required": False, "language": "zh"}
        files.append(item)
        by_path[primary] = item
    else:
        by_path[primary]["language"] = "zh"
        by_path[primary]["role"] = by_path[primary].get("role", "proposal_figure")
    if counterpart not in by_path:
        item = {"path": counterpart, "role": "proposal_figure", "required": False, "language": "en", "translation_of": primary}
        files.append(item)
        by_path[counterpart] = item
    else:
        by_path[counterpart]["language"] = "en"
        by_path[counterpart]["translation_of"] = primary
        by_path[counterpart]["role"] = by_path[counterpart].get("role", "proposal_figure")

# Refresh every declared hash now; repo scripts will refresh again after generated artifacts change.
for item in files:
    rel = item.get("path")
    if not rel or rel == "manifest.json":
        continue
    p = S / rel
    if p.exists() and p.is_file():
        item["sha256"] = hashlib.sha256(p.read_bytes()).hexdigest()

manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("v0.5 content + manifest patch complete")
