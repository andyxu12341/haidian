# 方案迭代记录

## v0.4 - 2026-08-13 — SITE-GROUNDED TIME RIGHTS

- 建立 `research/repo-data-audit.json`，将仓库既有资料分为 A 官方事实、B OSM/公开现状、C 可重跑方法、D 合成模拟、E 他人设计五级，禁止把 synthetic / illustrative 数据冒充京张真实现状。
- 建立 `research/site-grounded-anchor-network.geojson`，整理大钟寺、知春路、五道口、清华东路西口、学知园、清河小营桥、清华园车站旧址等背景核验锚点，并明确非测绘/非红线/非实际轨道里程。
- 建立 `research/site-grounding-facts.json`：采用北京市园林绿化局公开事实，将京张铁路遗址公园一期“清华东路—知春路、约 2.5 km、16.8 ha、已开放”作为第一段真实研究锚点；OSM way/122348403 仅作公开地图交叉核验。
- 建立 `research/temporal-network-plan.json`，将 v0.3 的 12 节点 proof-of-method 升级路线定义为真实道路/步行/轨交网络 × 96 个 15 分钟时间层，并明确 POI、营业时间、运营时刻与需求数据的来源等级。
- 新增 7 张可编辑 SVG：TIME RIGHTS 主视觉、数据证据分层、场地锚点审计、Space × Time 方法、定量 proof、24h 街道剖面、三重点区 24h 时序矩阵。
- 以上研究增强已于 2026-08-13 正式并入 `main`，后续方案深化统一直接在 `main` 迭代并由 #2093 自动验证。

## v0.3 - 2026-08-12 — JINGZHANG TIME RIGHTS

- 主品牌由“京张运行图”升级为 **京张时权 · JINGZHANG TIME RIGHTS**；`THE CITY TIMETABLE` 保留为运行机制名，避免与仓库内同类“运行图”方案发生概念/命名混淆。
- 研究命题从“用运行图调度城市”进一步明确为 **从空间使用权到时间使用权**：时间成为与用地、空间同等重要的规划变量。
- 新增 6 组双语深化图件：TIME RIGHTS 主视觉、研究方法链、时间扩展网络、时序可达性实验、24h 街道剖面、三重点区 24h 时序矩阵；连同原 5 组双语核心图，形成 11 类 × 中英双语的图件体系。
- 新增 12 节点 × 96 个 15 分钟时片 = 1,152 个 space-time states 的 proof-of-method；保持机器服务时长不变的情况下，示范结果为高峰冲突 -70%、高峰可逆空间可用率 +25.9pp、30 分钟时序可达 +5.7%。所有结果均明确标注为 scenario-based proof，不是现场实测绩效。
- 新增 24h 可逆街道剖面：07:30 通勤优先、11:00 受控配送、19:30 青年/Demo 活动、23:00 安静与必要通行；T0 无障碍/应急权利在全部状态连续。
- 更新中英文 proposal、HTML、A3/A0 双语图册、visual index、metrics、assumptions、sources、copyright 与 manifest 的本地 v0.3 包。
- v0.3 完整二进制图件/PDF 已生成；自 v0.4 起不再维护平行工作分支，成熟内容直接进入 `main`。

## v0.2 - 2026-08-10

- 建立“京张运行图 / THE CITY TIMETABLE”时空治理母题。
- 完成 TimeSlot Contract、6 类画像、12 个场景卡与 4 个测试验证场景。
- 完成 9 类 GeoJSON、metrics、compliance / standard / design-depth matrices。
- 完成中英双语 proposal、10 张核心图、A3/A0 双语 PDF 与离线 HTML。
- 使用官方 `finalize_submission.py` 首轮成功进入 Review-ready package 状态，并依据 `self_check_submission.py` 修正 layer enums、green_ratio、visual markers 与 evidence anchors。
- 所有 provisional geometry 继续声明为非 official redline；官方 polygon 发布后须整体复算。

## v0.1 - 2026-08-10

- 创建投稿目录 `submissions/andyxu12341/jingzhang-city-timetable/` 与独立投稿分支。
- 确立 T0-T3 时间层、三处重点区角色、六类画像、十二个场景方向与三处朝圣地标。
- 添加 AI 生成披露与假设登记表。
- 首版仍为 concept working package，未打开上游 Pull Request。
