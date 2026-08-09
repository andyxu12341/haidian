---
title: "京张运行图：把城市空间变成可审计、可切换的 AI 时序系统"
author_github: "andyxu12341"
language: "zh"
proposal_format_version: "2"
bilingual_contract_version: "1"
translation_file: "proposal.en.md"
license: "COMMUNITY-DISPLAY-ONLY"
summary: "以铁路运行图为文化与机制母题，把京张AI创新带组织成可公开、可审计、可人工接管的城市时序系统。机器人配送、低速自动接驳、青年夜间活动、日常通勤、无障碍和应急通行通过时间窗共享公共空间；T0恒定权利优先于所有算法调度，官方几何发布后再整体复算精确落位。"
tracks: ["robotics-autonomous-mobility", "youth-friendly-public-space", "jingzhang-heritage-narrative"]
scenarios: ["robot-delivery-low-speed", "ai-traffic-walkability", "ai-cultural-guide"]
iteration: "v0.2-structured"
---

# 京张运行图 · THE CITY TIMETABLE

一百年前，京张铁路解决的不只是“从哪里铺轨”，还必须处理何时发车、在哪里会让、谁先通过、发生延误后怎样恢复。一百年后，AI 城市面对相似的协调问题，只是对象从列车变成了人、机器人、低速自动接驳、公共活动与城市服务。

**京张运行图的核心不是给传统城市设计贴上 AI 标签，而是把“时间”变成与空间同等重要、可以公开、可以校验、可以人工接管的设计维度。** 城市公共空间不仅说明“这里是什么”，还要说明“何时允许什么、谁拥有优先权、冲突时如何退出、谁对最终决定负责”。

当前版本已经形成 TimeSlot Contract、12 张场景卡、九类 GeoJSON、metrics、来源表和三套矩阵，但五张双语核心图、离线 HTML、A3/A0 双语图纸、manifest、finalize/self-check/preflight 尚未完成，因此本文件仍是 **formal working package**，不是 `ready_for_review`，也不代表政府审定、法定规划、工程可行性或运营许可。

## 设计依据与资料清单

项目三层范围、三处重点区域、总体设计任务和成果深度以官方征集公告为主控依据 [source:OFFICIAL-ANNOUNCEMENT]；智能体共创原则、六项 Agent 任务、场景卡/画像/地标/运营要求以面向智能体任务书为依据 [source:AGENT-TASKBOOK]。专业表达同时参照仓库已登记的《城市设计管理办法》、控规编制审批办法和用地分类指南本地快照 [source:STD-URBAN-DESIGN] [source:STD-CONTROL-PLAN] [source:STD-LAND-USE]。

当前公开资料给出约 43.6 km² 统筹研究范围、约 11.4 km² 总体设计范围和 368.4 ha 三处重点区域，但精确 official polygon 尚未进入可信 site package。提交中的 `geometry/site_boundary.geojson` 与 `geometry/key_areas.geojson` 因此继续标记为 `provisional_constraint`、`official_boundary=false`；其面积、比例和节点关系只能用于生成、可视化和临时自检，官方 polygon 发布后必须整体重算 [source:BOUNDARY-SOURCE] [source:KEY-AREA-SOURCE] [assumption:A-BOUNDARY-001]。

容积率、建筑高度、建筑密度、正式绿地率控制、退线、道路红线、权属、市政容量和工程条件仍是待补数据。本案不以 schema 合理范围、新闻图、OSM、文字四至或 AI 推断补造这些法定条件 [assumption:A-CONTROLS-001]。

![三层范围与运行图总览](assets/figures/site-overview.png)

## 三层范围工作框架

### 43.6 km²：创新协同运行域

统筹研究范围不再重复画一张泛化的“大蓝图”，而是研究创新活动的时间网络：高校成果何时进入测试，企业何时获得场景窗口，全球活动何时连接三处重点区，人才服务、物流、夜间经济和公共服务如何避免相互挤压。输出以创新活动年历、跨片区协同关系和“三区两翼”的时间接口为主。

### 11.4 km²：City Timetable 主系统

总体设计范围形成三类空间：

1. **恒定权利空间**：基础步行、无障碍连续通行、应急与必要非数字服务不可被调度取消；
2. **时序共享空间**：物流、接驳、社区活动、青年活动和展陈可在明确时间窗中切换；
3. **受控测试空间**：机器人与低速自动接驳只有在安全前置条件、人工责任与退出机制具备时进入测试窗口。

### 368.4 ha：三类“时间治理”实验

三处重点区不复制同一套 AI 设施：众智园承担**测试与安全**，北京 AI 原点社区承担**24h 共创与生活权利平衡**，大钟寺承担**高频消费、轨道客流、夜间活动与物流错峰** [metric:key_area_count]。

## 统筹研究范围产业与未来城市研究

### 从 Space Plan 到 Time Plan

传统城市设计回答“什么在什么地方”；京张运行图增加“什么在什么时候发生、冲突时谁必须让行”。由此形成：一条贯穿南北的**时间主脊**、三类重点区**时序接口**和面向中关村科技服务翼/小月河场景赋能翼的跨域运行接口 [data:geometry/roads.geojson#ROAD-001] [metric:time_spine_length_m]。

### 六个全球机制案例

本案只借鉴可迁移机制，不把境外制度直接套用为北京标准：

| 案例 | 可迁移机制 | 对京张的启发 | 不可直接迁移 |
| --- | --- | --- | --- |
| NYC Open Streets 2026 | 街道按明确日期/时段切换 Full Closure、Limited Local Access 等模式，并保留应急与必要通行 | 公共空间必须公开“何时切换、哪些例外仍有效” | 纽约道路法规、运营主体与执法制度 [source:CASE-NYC-OPEN-STREETS-2026] |
| LADOT Code the Curb | 把路缘位置与规则数字化，使公共路权可被机器读取和管理 | TimeSlot Contract 应把空间、规则、时间窗和责任人结构化 | 洛杉矶政策与路缘数据库 [source:CASE-LADOT-CODE-THE-CURB] |
| OMF Curb Data Specification | 用开放数据结构表达 curb regulations、events 和 metrics | “运行图”不只做视觉图，应有机器可读合同与复算指标 | CDS 本身不是北京规划/交通规范 [source:CASE-OMF-CDS] |
| Singapore LTA / CETRAN | 自动驾驶测试与道路部署分离，强调安全评估、记录和运行条件 | 众智园必须把“受控测试”与“获准运营”明确区分 | 新加坡法律与测试许可不适用于北京 [source:CASE-SG-LTA-AV] |
| TfL School Streets | 在上下学时段临时限制机动车，稳定保护儿童步行环境 | T0/T1 可把“固定公共权利时段”设为不可被低优先级用途覆盖 | 英国 Traffic Order 与执法机制 [source:CASE-TFL-SCHOOL-STREETS] |
| Paris Rues aux écoles | 学校周边道路转化为更安全的步行、游戏和公共空间 | 青年友好不是多做“网红设施”，而是把安全公共空间权利写入运行机制 | 巴黎具体街道改造制度 [source:CASE-PARIS-RUES-ECOLES] |

这些案例共同支持一个判断：**真正的 AI 原生城市形态，不只是传感器更多，而是公共规则能够被人理解、被机器读取、被责任人复核，并在失败时安全退回。**

## 总体设计范围城市更新与控规深度城市设计

### 四级时间空间

**T0 恒定权利层 / Constant Rights**：无障碍连续通行、应急通道、基础步行、必要非数字服务路径。T0 不参与市场化预约，也不能被 AI 推荐覆盖。

**T1 日常固定层 / Routine Rhythm**：通勤高峰、学校时段、日常商业、公园慢行和居民基本出入。

**T2 弹性预约层 / Flexible Reservation**：机器人配送、低速自动接驳、临时展陈、社区课程、轻量青年活动。通过角色授权进入时间窗。

**T3 事件确认层 / Human-confirmed Event**：AI 大会、特殊测试周、Demo Night、大型路演和高客流事件。必须存在明确的人类责任角色。

TimeSlot Contract 规定每个请求至少包含：空间单元、时间窗、允许主体、优先级、时间层、无障碍保护、人类责任人、停止条件、回滚动作、日志、非 AI 等价路径和验证方法。冲突规则按 P0–P3 优先级执行，T0/P0 永远高于机器人、商业和活动预约 [metric:time_layer_count] [data:geometry/constraints.geojson#CONST-001]。

当前协议已经给出 4 个 PASS 与 4 个 FAIL 测试样例，例如“低峰机器人配送且 T0 无障碍通道连续”可进入人工/运营确认，而“机器人穿越唯一无障碍通道”“活动临时堵塞应急通道”“自动接驳缺少安全评估证据”必须直接拒绝 [metric:validator_negative_case_count]。

![用地与城市时序结构](assets/figures/land-use-structure.png)

## 重点区域详细设计

### 众智园：AI 运行图测试场

定位为**具身智能进入城市之前的可观察、可退出测试场**。空间设置受控测试环、人工接管点、公共观察场和运行日志界面。机器人配送、低速接驳、人群高峰退出和日志回放构成 4 个产业测试验证场景 [metric:test_validation_scenario_count]。

任何测试必须区分设计验证与正式运营许可；出现无障碍冲突、异常人群密度、通信/传感器降级或人工停止请求时立即降级或停止 [assumption:A-ROBOTICS-001]。

### 北京 AI 原点社区：24h 共创时序社区

定位为**青年创新节律与居民日常权利共存的社区**。白天支持学习、协作和公共服务，夜间允许 Demo Night、轻运动与学习空间切换，但居民安静权、普通通行和无障碍路径作为硬约束。

基本公共服务不以人脸识别、个人轨迹或强制 App 登录作为必要条件；AI 导航、活动预约和文化导览均提供物理导视、纸质信息或人工服务的等价路径 [metric:non_ai_fallback_coverage]。

### 大钟寺：智能原生生活时序场

定位为**高频人流、消费、轨道、夜间活动与机器物流的错峰共存场**：商业高峰优先人流，低峰安排受控补货/末端配送，夜间开放青年文化与消费活动，高客流或事件状态触发机器活动退出。

由于仓库 provisional `PROV-KEY-003` 的绝对位置与公开地理锚点关系已被社区提出复核，本阶段不把矩形粗略范围深化成具体路口、站城四象限或建筑工程方案 [assumption:A-DAZHONGSI-001]。

### 三处 AI 朝圣地标

1. **运行图大厅 / TIMETABLE HALL**：把全带当前模式、下一次切换、测试状态和年度活动变成公共可读界面；
2. **时间交换站 / TIME EXCHANGE**：把青年活动、社区课程、公共服务和城市测试窗口组织为可共享时间资源；
3. **百年发车台 / CENTENNIAL DEPARTURE**：以“发车—会让—延误—恢复”的京张铁路逻辑讲述从铁路现代化到 AI 城市治理的百年连续性。

![三个重点区与朝圣节点](assets/figures/key-areas.png)

## AI 创新生态、人才画像与 AI+ 场景

### 六类用户画像

- AI 创业团队与开发者：需要测试、发布、协作和低成本接入城市场景；
- 高校学生与青年研究者：需要学习、夜间交流和成果展示；
- 周边居民：需要稳定通行、安静休息、社区服务与知情反馈；
- 无障碍和高龄使用者：需要连续可达、低认知负担、非 App 等价路径；
- 商户与夜间从业者：需要客流、补货、垃圾清运和明确营业/物流时段；
- 物流、运维与应急角色：需要受控通行、故障处置、人工接管和审计记录。

### 12 张场景卡

| ID | 场景 | 类别 | 核心校验 |
| --- | --- | --- | --- |
| SC-01 | 机器人配送时间窗压力测试 | 测试验证 | 不得压缩 T0；有人工停机与回滚 |
| SC-02 | 低速自动接驳冲突降级测试 | 测试验证 | 安全前置证据、降级、人工接管 |
| SC-03 | 人群高峰自动退出测试 | 测试验证 | 高峰时机器使用先退出 |
| SC-04 | 人工接管与日志回放 | 测试验证 | 每次 override 有责任人和可重放日志 |
| SC-05 | 青年 Demo Night 可逆公共客厅 | 公共生活 | 居民通行、噪声、应急、活动结束后复原 |
| SC-06 | 免 App 公共服务导航 | 公共生活 | 无账号也能完成同等基本服务 |
| SC-07 | AI 文化导览 + 非数字等价路线 | 公共生活 | 历史/版权复核 + 物理导视等价 |
| SC-08 | 夜间学习与轻运动空间切换 | 公共生活 | 安静约束、维护窗口、人工值守 |
| SC-09 | 场景开放预约与准入 | 产业运营 | 规则、风险级别、责任主体可追踪 |
| SC-10 | 企业 Demo 时段共享 | 产业运营 | 公共空间不能被长期排他占用 |
| SC-11 | 活动日多主体排程 | 产业运营 | 冲突模拟、无障碍/应急优先、事后对账 |
| SC-12 | 公共运行图透明展示 | 产业运营 | 当前状态、切换时间、责任角色、非AI路线可见 |

12 个场景均已写入 `visual/assets/scenarios.json`，并保持人工复核字段与非 AI fallback 覆盖 [metric:scenario_count] [metric:human_override_coverage] [metric:non_ai_fallback_coverage]。这里的 100% 表示**设计合同字段覆盖率**，不是未来真实运营达标率 [assumption:A-METRICS-001]。

## 用地、建筑规模与拆改留方案

现阶段不以临时边界推导法定用地、不以示意建筑足迹推导实际存量，也不给出 FAR、高度和密度。`geometry/land_use.geojson` 使用可校验 land_use_code 表达概念功能结构，所有属性都注明“不构成控规批准” [source:STD-LAND-USE]。

建筑层设置 6 个 `candidate_retrofit` 示意单元，目标是表达“先利用存量、首层界面和可逆空间，再讨论新增建设”的设计态度；它们不对应已核实现状建筑。示意足迹复算约 88,629 m²，仅用于结构化模型测试 [metric:building_footprint_area_sqm]。

`floor_area_ratio` 继续保持 `unknown`，直到 official boundary 与 approved controls 可得 [metric:floor_area_ratio]。

## 交通、轨道、市政与公共服务设施

本案不修改或声称已确定既有主干路、铁路、河流、道路红线和市政控制，而在设计层增加一条约 9.22 km 的“时间主脊”概念线和三条重点区时序接口，用于表达跨片区慢行、公共活动和时间治理关系 [metric:time_spine_length_m]。

T0 约束层则设置纵向连续权利线与三个横向重点区接口，总长度约 12.33 km；这不是消防或道路红线，而是方案内部的“不得被算法调度覆盖”的公共权利约束 [metric:t0_constant_rights_corridor_length_m]。

市政与新基建策略把**公开运行状态、机器可读规则、人工接管、异常日志、非数字备份**视为数字基础设施的一部分；分布式能源、端侧算力、传感器、通信、市政管线和消防等工程容量必须等待专项资料与专业论证。

![交通、T0权利与蓝绿公共空间](assets/figures/mobility-bluegreen.png)

## 蓝绿空间、公共空间与城市风貌

空间形象不以“未来科技蓝光”作为唯一 AI 表达，而将铁路运行图的时间轴、站点、会车线和延误恢复逻辑转译为标识、铺装、公共信息与活动系统。

当前概念绿地层包括一条遗址公园时序绿廊和三处重点区弹性开放绿地，按临时边界复算约占 33.46%；该值只是概念设计比例，不是 approved green ratio，也不代表遗址公园官方边界 [metric:green_ratio]。

六处可逆公共空间包括三处朝圣节点和三处测试/青年/智能生活空间，概念面积约占临时总体范围 1.50% [metric:public_space_ratio] [metric:reversible_public_space_count]。重点不是追求面积比例，而是证明同一公共空间可以在不牺牲 T0 权利的前提下拥有多个时间模式。

文化叙事采用“**百年发车—开放会让—智能运行—可恢复城市**”四段式：铁路历史说明现代城市曾如何通过统一时间组织复杂流动；中关村文化强调开放创新与成果转化；AI 新文化则强调透明规则、责任边界和人机协作，而非将 AI 描述为自动替代城市治理。

## 更新项目清单、实施政策与分期计划

### 近期：协议与低风险可逆试点

优先完成 TimeSlot Contract、公开运行图界面、无障碍/应急 T0 校核、免 App 服务导航、Demo Night 可逆公共客厅和不进入公共道路的机器人受控测试。近期项目强调低成本、可撤回、可量化，不依赖大拆大建。

### 中期：跨片区运行图联动

在官方空间数据和专业条件补齐后，连接三处重点区的活动、物流、公共服务、慢行与测试窗口，建立统一的开放预约、责任人机制和运行日志。

### 远期：全带城市运行系统

只有在交通、安全、规划、市政、文保、权属和运营审批路径明确后，才讨论具身智能公共运行、更高等级自动接驳和长期空间改造；概念方案不能提前宣称这些内容“获批”或“必然落地” [assumption:A-ROBOTICS-001]。

年度运营建议包括 **Open Timetable Week、Urban Agent Scheduling Challenge、Robotics Low-speed Test Week、Jing-Zhang Demo Night、Annual City Timetable Review**。活动不是独立营销日历，而是用于持续验证冲突规则、公众体验和运营责任的治理循环。

`geometry/phasing.geojson` 以近期/中期/远期表达概念推进关系，所有阶段仍依赖 official polygons、专业复核和必要审批。

## 指标体系、面积复算与合规矩阵

当前空间指标使用 EPSG:4548 复算；其中 provisional / conceptual 指标只表示当前设计模型内部一致性，不可升级为正式控规指标。

| 指标 | 当前值 | 含义与限制 |
| --- | ---: | --- |
| `site_area_sqm` | 11,412,825 m² | 临时总体边界复算；非 official redline |
| `key_area_count` | 3 | 数量来自任务要求，几何仍 provisional |
| `building_footprint_area_sqm` | 88,629 m² | 6 个概念 retrofit 单元，不是现状建筑统计 |
| `green_ratio` | 33.46% | 概念绿地层 / 临时边界；不是规划绿地率 |
| `public_space_ratio` | 1.50% | 仅六处运行图公共空间，不代表全域公共空间供给 |
| `time_spine_length_m` | 9,216.69 m | 概念连接线，不是道路/铁路工程线位 |
| `t0_constant_rights_corridor_length_m` | 12,327.51 m | 设计协议权利线，不是法定红线 |
| `scenario_count` | 12 | 机器可读场景卡数量 |
| `test_validation_scenario_count` | 4 | 满足不少于 3 个测试验证场景的任务要求 |
| `human_override_coverage` | 100% | 12 场景都定义人工复核；是设计字段覆盖率 |
| `non_ai_fallback_coverage` | 100% | 12 场景都定义非 AI fallback；是设计字段覆盖率 |
| `floor_area_ratio` | unknown | 等待官方控规与 official polygon |

合规关系分别由 `compliance_matrix.json`、`standard_matrix.json`、`design_depth_matrix.json` 管理，覆盖公告任务、Agent 1–6、专业标准、图层、指标、图纸与风险假设。

![指标、证据与TimeSlot Contract](assets/figures/metrics-evidence.png)

## 风险、版权与合规说明

1. **边界风险**：official polygon 缺失。所有 provisional geometry 必须在官方数据出现后整体复算，而不是仅替换一个边界文件 [assumption:A-BOUNDARY-001]。
2. **控规与工程风险**：FAR、高度、密度、退线、道路红线、权属、市政、消防、文保等均不得自行推定 [assumption:A-CONTROLS-001]。
3. **具身智能风险**：测试不等于许可；公共部署需安全、交通、监管和运营条件另行确认 [assumption:A-ROBOTICS-001]。
4. **大钟寺位置风险**：在 provisional geometry 复核完成前不深化具体站城四象限与建筑落位 [assumption:A-DAZHONGSI-001]。
5. **指标风险**：合同字段覆盖率与真实运营绩效严格分开；真实冲突拒绝率、事故率、公众满意度等需未来建立基线 [assumption:A-METRICS-001]。
6. **隐私与公平**：基本公共服务不依赖人脸识别、持续个体追踪、强制 App 或指定供应商；T0 权利对所有使用者保持可见和可达。
7. **版权**：不复制铁路企业 Logo、竞品设计或未经授权图像/字体；运行图视觉系统应使用原创图形和可清权资产。
8. **状态表达**：本成果只能称作 open-call concept / formal working submission；在维护者合并、专业复核或后续实施前，不使用“获批、入选、实施完成”等表述。

## 参考资料

- 百年京张 AI 创新带城市设计国际方案征集资格预审公告 [source:OFFICIAL-ANNOUNCEMENT]
- 面向全球智能体开展百年京张 AI 创新带城市设计开源征集任务书摘录 [source:AGENT-TASKBOOK]
- Repo public source registry [source:SOURCE-REGISTRY]
- 《城市设计管理办法》本地官方来源快照 [source:STD-URBAN-DESIGN]
- 《城市、镇控制性详细规划编制审批办法》本地官方来源快照 [source:STD-CONTROL-PLAN]
- 《国土空间调查、规划、用途管制用地用海分类指南》本地官方来源快照 [source:STD-LAND-USE]
- NYC DOT Open Streets 2026 [source:CASE-NYC-OPEN-STREETS-2026]
- LADOT Code the Curb [source:CASE-LADOT-CODE-THE-CURB]
- Open Mobility Foundation Curb Data Specification [source:CASE-OMF-CDS]
- Singapore LTA Autonomous Vehicles / CETRAN [source:CASE-SG-LTA-AV]
- Transport for London School Streets [source:CASE-TFL-SCHOOL-STREETS]
- Ville de Paris Rues aux écoles [source:CASE-PARIS-RUES-ECOLES]
