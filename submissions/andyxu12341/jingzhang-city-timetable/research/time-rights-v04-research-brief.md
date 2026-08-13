# 京张时权 · JINGZHANG TIME RIGHTS — v0.4 Research Brief

## 1. 研究问题｜Research Question

传统城市设计主要通过土地使用、道路、公共空间和建筑形态分配**空间使用权**。但在人、机器人、低速自动接驳、物流、活动与公共服务共同使用街道和公共空间的 AI 城市中，冲突并不只发生在“哪里”，还发生在“什么时候”。

本研究提出：**城市设计应把“时间使用权 / temporal use rights”作为与空间使用权并列的规划变量。**

核心问题由此变为：

> 同一空间在不同时间允许谁进入、谁优先、冲突时谁退出、什么权利不可被算法覆盖、失败后如何回滚？

铁路“运行图”不再是方案的最终概念，而是 TIME RIGHTS 的运行机制：`THE CITY TIMETABLE`。

## 2. 核心命题｜From Spatial Rights to Time Rights

空间状态不由 AI 自主决定，而由公开的 **Space × Time × Rights Contract** 决定。

- **T0 Constant Rights / 恒定权利**：无障碍连续通行、应急、基本步行、必要非数字服务；不可预约、不可覆盖。
- **T1 Routine Rhythm / 日常节律**：通勤、学校、居民基本出入、日常商业与公园慢行。
- **T2 Flexible Reservation / 弹性预约**：机器人配送、低速接驳测试、课程、临时展陈、社区活动。
- **T3 Human-confirmed Event / 人工确认事件**：Demo Night、大型活动、特殊测试；必须具名人工责任。

AI 可预测冲突、提出排程，但无权删除 T0，也不能替代最终的人类责任角色。

参见：`assets/figures/time-rights-hero.svg`。

## 3. 数据证据分层｜Data Provenance

为避免“看起来有数据”却把合成值误当现状，本研究将输入分成五级：

- **A — Official public**：政府/官方公开事实，可在限定范围内支撑事实判断。
- **B — OSM / public mapped condition**：可用于研究现状背景，不能升级为法定红线或测绘成果。
- **C — Reproducible method**：可重跑模型、变量结构和验证方法；需要独立实现，不直接继承他人结论。
- **D — Synthetic / illustrative**：只能做敏感性分析或 proof-of-method，绝不作为本地真实基线。
- **E — Agent-generated design**：设计提案，不作为事实数据。

仓库审计见 `research/repo-data-audit.json`；图示见 `assets/figures/data-provenance.svg`。

## 4. v0.3 定量 Proof-of-Method｜12 Nodes × 96 Time Layers

第一阶段不是伪造现场数据，而是先验证方法在显式假设下是否具有可计算行为。

模型规模：

- 12 个概念公共空间/节点；
- 每日 96 个 15 分钟时间片；
- 共 1,152 个 space-time states；
- 显式设置人群高峰、机器服务窗口、T0/T1/T2/T3 权利约束。

比较：

1. **Baseline**：机器活动与人群高峰缺乏时序协调；
2. **TIME RIGHTS**：机器服务总量不减少，只重新分配时间窗，并受 T0/T1 权利约束。

在该概念实验中：

- 高峰人机冲突时长：`10 h → 3 h`，**-70%**；
- 高峰三处可逆空间可用率：`62.96% → 88.89%`，**+25.93 pp**；
- 30 分钟高峰时序可达机会：`3.701 → 3.912`，**+5.69%**；
- 机器服务总时长：`10 h/day → 10 h/day`，保持不变。

这些结果是**场景实验结果，不是现场绩效**。原始模型与脚本：`visual/assets/temporal_network.json`、`temporal_network_results.json`、`temporal_network_analysis.py`；图示见 `assets/figures/temporal-proof-results.svg`。

## 5. 从静态中心性到时序中心性｜Cᵢ → Cᵢ(t)

传统接近中心性可写为：

`C_i = (N-1) / Σ_j d_ij`

当道路、设施、活动与轨交服务随时间变化时，距离/阻抗应写为 `d_ij(t)`：

`C_i(t) = (N-1) / Σ_j d_ij(t)`

因此同一节点在 08:00、12:00、18:00、22:00 不再拥有一个固定中心性，而形成**中心性时序曲线**。

v0.4 的目标不是用人口把中心性“加权得更漂亮”，而是直接研究网络本身如何因为开放时间、运营时刻、空间切换和 T0–T3 权利发生变化。

方法图：`assets/figures/temporal-network-method.svg`。

## 6. 真实场地锚定｜Site Grounding

v0.4 将 competition provisional geometry 与研究基线分开处理。

### 6.1 官方事实锚点

北京市园林绿化局公开信息确认：京张铁路遗址公园一期位于**清华东路至知春路**，总长度约 **2.5 km**，总面积 **16.8 ha**，并已全面建成开放。

该事实用于把中段研究锚定到一个真实已开放公共空间段，但不替代竞赛官方边界、道路红线或地籍数据。登记见 `research/site-grounding-facts.json`。

### 6.2 站点/遗产背景锚点

仓库多份独立提交对公开地图锚点进行了交叉核验。本研究只把这些坐标作为**背景锚点**并标记 `formal_claim=false`，包括：

- 大钟寺站；
- 知春路站；
- 五道口站；
- 清华东路西口站；
- 学知园站；
- 清河小营桥站；
- 清华园车站旧址。

见 `research/site-grounded-anchor-network.geojson` 和 `assets/figures/site-anchor-audit.svg`。

### 6.3 一个重要发现

公开地图交叉核验显示，仓库提供的 competition provisional polygon 与部分真实地理锚点存在显著偏移。因此：

- **比赛 formal package**：继续尊重官方仓库 provisional constraint，并明确“非官方红线”；
- **研究/作品集模型**：以独立公开现状网络和官方事实重新构建分析底图，不把 provisional polygon 当成真实地理现状。

这两层必须分开，不能互相冒充。

## 7. 24h 空间原型｜Spatial Translation

TIME RIGHTS 必须落到空间，而不是只停在规则表。

### 7.1 24h 可逆街道剖面

同一剖面在一天中经历：

- **07:30**：T1 通勤优先，机器活动退出；
- **11:00**：T2 受控配送进入弹性区；
- **19:30**：T3 Demo Night / 青年公共客厅，人工确认；
- **23:00**：恢复安静、必要通行和基础服务。

四个状态下 T0 无障碍和应急连续线不改变。

图示：`assets/figures/street-section-24h.svg`。

### 7.2 三重点区 × 24h

- **众智园**：测试“AI 什么时候必须停”，重点是受控测试、人工接管、日志与公共观察。
- **AI 原点社区**：测试 24h 共创与居民安静、基本服务、非 App 等价路径之间的边界。
- **大钟寺**：测试轨道高峰、低峰物流、夜间文化消费之间的错峰共享。

三处不是复制相同 AI 装置，而是在同一 TIME RIGHTS 语法下验证三种不同城市问题。

图示：`assets/figures/key-areas-24h.svg`。

## 8. 设计验证逻辑｜Validation / Stop / Rollback

每个动态空间状态必须回答：

1. 谁负责确认？
2. 什么时候允许开始？
3. 什么权利必须始终连续？
4. 哪些条件触发 STOP？
5. 失败后回到哪一个 baseline？
6. 是否保留非 AI fallback？
7. 是否留下可审计日志？

典型 STOP 条件包括：T0 连续性中断、异常拥挤、传感器/通信降级、人工停止请求。

Rollback：**撤销机器/事件状态 → 恢复 T0/T1 → 记录事件 → 人工复核后才允许再次启动**。

## 9. v0.4 真实时间扩展网络｜Next Empirical Layer

下一阶段将 v0.3 的 12 节点概念图升级为真实场地网络：

`OSM walk/road network + crossings + station anchors + POI/opening hours + transit operating windows + T0–T3 rights`

并生成至少四组时序分析：

- 08:00 Temporal Closeness / Accessibility；
- 12:00 Temporal Closeness / Accessibility；
- 18:00 Temporal Closeness / Accessibility；
- 22:00 Temporal Closeness / Accessibility。

重点比较：

- 节点中心性随时间的跃迁；
- T0 约束对弱势使用者绕行/可达性的影响；
- 机器时窗与人流高峰的冲突分钟数；
- 在机器服务总量不减少时，重新排程能否降低冲突；
- 公共空间可用时长是否增加。

升级契约见 `research/temporal-network-plan.json`。

## 10. 对考研/研究表达的最终定位

这个项目不应只被描述为“AI 城市设计竞赛”。其研究型标题可以是：

> **从空间规划到时空规划——基于时间使用权的 AI 时代公共空间动态共享研究**

英文：

> **From Spatial Planning to Temporal Planning: Time-Use Rights for Dynamic Public-Space Sharing in the AI City**

研究链条为：

**Research Question → Data Provenance → Time Rights → Machine-readable Contract → Time-expanded Network → Quantitative Proof → 24h Spatial Prototype → Site Grounding → Empirical Recalculation**

这使作品同时具备城市设计、城市网络分析、AI 治理与可复现研究方法四个层次。
