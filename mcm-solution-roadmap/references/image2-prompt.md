# 总体解题路线图的 Image2 提示词

## 先核对材料，再填写三段内容

优先阅读用户给出的原题及建模报告，再用论文、结果报告与实际求解输出核对。按原题顺序列全明确小问，保留已有编号和嵌套层级。原题未编号时，在 `WHAT` 中提供与原文逐项对应的工作编号，注明仅供板块标识。每条公式、数值和连线都要能追溯到已有依据。区分题面给定条件、实测数据、假设和情景参数。缺项在相应位置用英文标明 `Not documented`。代表结果用已核实的数值卡表达，精确刻度和曲线由论文的数据图承载。


| 赛题内容字段                           | 英文内容                                                                                                                                                                   |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `WHAT` · Modeling problems           | 明确小问数量及标识，逐问列任务、对象、输入、参数与约束。列出真实共用的输入、数据、模型或接口、需要展示的系统实体、跨问关系和最终决策任务。 |
| `HOW_TO_MODEL` · Modeling methods    | 逐问列实际采用的主方法、必要扩展、核心公式、变量、参数、约束、假设、适用范围和模型间的输入输出。 |
| `HOW_TO_SOLVE` · Solution procedures | 逐问以实际顺序列数据处理、初始化、算法关键操作、参数优化、敏感性分析、仿真及直接验证该问的对照。列关键输出、已核验数值、验证判据、跨问传递和综合过程。无决策任务时写实际综合产出。 |

有未编号问询时，在 `WHAT` 的任务表前写明 `Use the task identifiers listed below for all numbered panels. Where the source has no number, the listed working identifier locates the original inquiry.` 各问只共享数据、符号、约束或接口时，在同一字段列出实际的共享项，并明确 `Use those documented inputs and interfaces in the shared region. Show the mathematical equations in their respective task panels.` 这两条按题面条件填写到 `WHAT`，母版固定文字照常使用。

先在逐问内容表核对「输入 → 模型 → 计算 → 结果 → 验证」各项，再用跨问连线表记录每条连接的起点、终点、传递内容和依据。只共用参数时从共享输入区分别连线，实际读取上游结果或约束时才连接两个小问。按实际工作填写算法与检验。步骤写成流程，并标明结果如何进入后续分析。

按 B 题样例的项目层级填写，每个独立输入、公式、约束、求解动作、结果或检验各占一行。比如，同一实验里的故障采样、容量更新、库存平衡、配对对照和压力测试要分别写出，并保留各自的条件、指标或样本量。「蒙特卡洛评估可靠性」只能用作标题。项目多少由题面及实际方法决定，文中各项有依据即可。

## 按母版装配一份提示词

将三项完整英文内容写入 UTF-8 JSON，每项为一段可含多行的字符串。另加入 `PALETTE` 对象，键为全局色板中实际使用的英文颜色语义，值为 `#RRGGBB` 色值。保留 `plan.md` 已确认的语义，例如将同一个风险颜色用于路线图的风险节点和数据图的风险情景。下例仅说明格式：

```json
{
  "PALETTE": {
    "Shared system and main structure": "#254C65",
    "Baseline comparison": "#517D87",
    "Risk and disruptions": "#A8542A"
  }
}
```

装配命令为：

```text
python scripts/render_image2_prompt.py path/to/content.json
```

脚本路径从 `mcm-solution-roadmap` 目录解析。脚本读取 [英文母版](image2-template.txt)，填入三个内容字段和全局配色段并输出一份英文提示词。三个内容字段只写本题事实与方法。布局、区域、箭头语义、字体、图示与质检条款由母版提供。中央网格按小问数量增减行数。原题的末问若本身就是综合输出，使用底部编号板块承载该问。仅复现旧提示词时，脚本兼容不含 `PALETTE` 的旧内容 JSON，并恢复旧母版的配色段。

提交前逐项检查：原题小问和编号齐全，模型及求解步骤与论文一致，公式、参数、单位和结果正确，跨问数据流有依据，配色段与全局色值和语义一致，母版固定文字完整。保留本次使用的内容 JSON、两张核对表和完整提示词。独立调用时只交付完整英文提示词。第四阶段拿到这份提示词后直接调用内置 Image2，成图按两张表、全局色板与母版逐项复核。

## 局部修订与覆盖检查

1. 以上一版完整内容为基准。若只保留了旧提示词，按 A、B、C 原有边界逐字恢复三个字段。若上一版使用旧母版，保留三个字段的全部内容，用当前母版重新装配。普通美化、重试和排版调整复用同一份完整提示词。用户确认更换全局色板时，复制原 JSON 并只更新 `PALETTE` 后重新装配。需要释放空间时，优先调整板块尺寸、分组和单个标签的长度。
2. 修改事实或术语时，给脚本提供 JSON 修订清单。每条包含 `field`、`before` 和 `after`，`before` 必须逐字对应字段中唯一的一行。替换文本须非空。补充新项目时，可在保留原行的基础上追加新行。脚本输出一份完整提示词，并另存本次内容 JSON。

```text
python scripts/render_image2_prompt.py content.json --patch changes.json --save-content content-v2.json
```

3. 用两张表逐项对照前后版本。确认每小问原有的输入、假设、公式、约束、实际求解步骤、验证数据、关键数值、单位和跨问传递仍可定位。核对本次修改确实符合用户要求或原文。无关项目及其细节保持原样，独立求解步骤分别保留。若有误删、归并导致信息丢失或新编内容，恢复原项后再出图。成图遗漏细节时修订成图，保留完整提示词作为核对基准。

## 完整提示词示例 · 2026 MCM B 题

下方保留提炼母版时参考的实测提示词全文，用于了解逐问描述和跨问连线的详细程度。日常生成按上方三项内容字段和已确认的全局色板装配。

````text
Create a single, publication-quality scientific workflow diagram for the 2026 MCM Problem B (Lunar Settlement Transportation and Infrastructure). The figure must comprehensively represent all five numbered subproblems, their mathematical models, computational methods, intermediate results, validation criteria, and actual dependencies.

## 1. Overall composition

- Landscape orientation, approximately 1.85:1 aspect ratio, suitable for a full-width academic paper figure (159 mm wide).
- **Do not include an overall title.**
- Divide the figure into a shared-input/network region, four independent analytical panels, and one final synthesis panel.
- Arrange the four analytical panels in a balanced 2×2 grid:
  - Upper left: 01 Ideal Construction
  - Upper right: 02 Reliability and Buffer Optimization
  - Lower left: 03 Water Supply
  - Lower right: 04 Environmental Impact
- Place 05 MCM Agency Recommendation as a full-width synthesis panel at the bottom.
- Each subproblem must have its own clearly delineated boundary, numbered heading, internal workflow, and identifiable output area.
- Each analytical panel should follow a consistent visual logic:
  **Inputs → Mathematical Model → Computational Procedure → Results → Validation**
- Use compact, well-aligned nodes. Allocate space according to information density rather than forcing identical internal layouts.

## 2. Shared inputs and transportation network

Place a shared system-definition region above the four analytical panels.

Include two distinct transportation routes:

**Route A: Space Elevator Transportation**
Earth → Electric Lift → Apex Storage → Feeder Flight → Moon

**Route B: Direct Rocket Transportation**
Earth Launch Sites → Direct Lunar Flight → Moon

Illustrate the Earth, three Galactic Harbor ports, orbital apex, Moon, and the two transportation routes using a clean scientific mechanism illustration.

Distinguish the transportation stages using consistent colors:
- Electric Lift: steel blue
- Feeder Flight: teal
- Direct Lunar Flight: amber

Show the three ports as parallel transportation systems, with separate apex inventories.

Include a compact shared-input module:

- Total dry cargo demand: D = 100 Mt
- Transportation starts: 2050
- Number of ports: 3
- Main lift capacity: 179 kt/port/year
- Main feeder capacity: 160 kt/port/year
- Direct rocket payload: 125 t/launch
- Launch capacity: 3,200 launches/site/year
- Candidate launch sites: 10

Show the effective port capacity as:

k_h = min(L_h, A_h)

Add a small sensitivity note distinguishing the interpretation of 179 kt as per-port versus system-wide capacity, and feeder capacity scenarios of 120–179 kt/year.

Explicitly distinguish measured problem specifications from scenario assumptions. Do not portray assumed prices, launch availability, failure probabilities, or environmental intensities as measured observations.

Draw clear outgoing connections from this common region to Problems 01–04, labeled with relevant shared information such as:
"Route Capacities", "Transportation Costs", "Demand", "Lead Times", and "Scenario Parameters".

## 3. Problem 01 — Ideal Construction

Panel heading: **01 | Ideal Construction**

Represent the following workflow:

**Input**
- Total cargo demand D
- Route capacities
- Transportation costs
- Construction deadline T
- Optional emissions budget B

**Mathematical model**

Define:
- x_h: cargo transported through ports
- x_i: cargo transported through launch sites
- k_h = min(L_h, A_h)
- k_i = N_i p

Show the main optimization problem:

Minimize:

Σ c_j x_j

Subject to:

0 ≤ x_j ≤ T k_j

Σ x_j = D

Optional emissions constraint:

Σ e_j x_j ≤ B

**Computational procedure**

1. Calculate theoretical transportation-capacity lower bounds.
2. Solve the unconstrained cost-minimization problem using cheapest-route-first allocation.
3. Introduce emissions constraints and solve using Linear Programming.
4. Sweep construction deadlines T.
5. Generate the cost–completion-time Pareto frontier.
6. Round direct rocket launches to integer flight counts and verify discretization error.

**Output**

Show compact result cards:

- Fastest hybrid construction: 113.636 years
- Fastest hybrid cost: $2,724.66 billion
- 130-year minimum-cost solution: $2,248.86 billion
- 50-year completion: Infeasible under nominal capacity

Include a miniature cost–time frontier plot as an internal mechanism illustration.

**Validation**
- Total cargo mass conservation
- Route capacity constraints
- Monotonic cost–time frontier
- Integer launch-count verification
- Feasibility checks

## 4. Problem 02 — Reliability and Buffer Optimization

Panel heading: **02 | Reliability & Buffer Optimization**

**Input**
- Shared nominal transportation network
- Annual common port disruptions
- Port-specific lift failures
- Port-specific feeder disruptions
- Binomial rocket launch failures
- Buffer capacity B

**Mechanism illustration**

Include a prominent, clearly readable inventory mechanism:

Lift → Apex Stock S → Feeder Flight

Show:
- Inventory accumulation
- Limited storage capacity
- Delayed transportation
- Dashed feedback loop indicating inventory carried over to the next year
- Independent inventory at each port
- No inventory borrowing between ports

Include the inventory constraints:

0 ≤ S ≤ B

x_lift ≤ L

x_feeder ≤ A

x_feeder ≤ S + x_lift

**Computational procedure**

1. Generate shared and independent annual failure events.
2. Update effective transportation capacities.
3. Simulate failed rocket launches and lost cargo.
4. Apply annual inventory balance and capacity constraints.
5. Perform paired Monte Carlo simulations with 2,500 paths.
6. Compare B = 0 against B = 40 kt/port.
7. Evaluate completion-time distributions, P50/P95, and additional costs.
8. Conduct compound-stress testing.

**Output**

Present a compact comparison:

| Metric | No Buffer | 40 kt Buffer |
|---|---:|---:|
| P50 completion | 128 years | 125 years |
| P95 completion | 130 years | 127 years |

Additional result:
- Average completion-time improvement: 2.73 years.
- Stress scenario: Years 51–55, 75% lift-capacity reduction and complete ground-launch suspension.
- Buffered stress-case P95: 131 years.

**Validation**
- Annual inventory conservation
- Storage capacity limits
- Launch-count limits
- Independent random seeds
- Paired-scenario comparison
- Total delivered cargo verification

## 5. Problem 03 — Water Supply

Panel heading: **03 | Water Supply & Operational Readiness**

**Input**
- Population N
- Daily per-capita water consumption q
- Water recycling rate r
- Transportation capacities
- Route-specific delivery lead times
- 30-day emergency reserve
- 45-day interruption scenario

**Mathematical model**

Show the net water demand equation:

D_w = 365Nq(1-r)

Use a 95% recycling scenario as the baseline.

**Computational procedure**

1. Calculate daily gross water consumption.
2. Calculate unrecovered water losses.
3. Determine annual replenishment requirements.
4. Establish the 30-day reserve requirement.
5. Use the shared transportation network to calculate minimum-cost and minimum-time delivery plans.
6. Simulate daily water inventory.
7. Compare independent water delivery against water transportation concurrent with construction.
8. Evaluate a 45-day interruption scenario.

**Output**

Highlight the actual baseline results:

- Net water loss: 250 t/day
- Annual replenishment: 91,250 t
- 30-day reserve: 7,500 t
- Total initial water provision: 98,750 t
- 45-day interruption requirement: 11,250 t

Include a small daily water-inventory curve or storage-tank mechanism illustration.

Show three transportation alternatives:
- Port economic solution: 135.09 days
- Hybrid fastest solution: 80.05 days
- Direct rocket fastest solution: 104.11 days

**Validation**
- Daily inventory balance
- No daily stockout
- 365-day coverage
- Final inventory verification
- 45-day interruption resilience

Include a small scope note: food-embedded water and initial filling are excluded.

## 6. Problem 04 — Environmental Impact

Panel heading: **04 | Environmental Impact & Carbon Optimization**

**Input**
- Electricity-grid carbon intensity g
- Port transportation emissions
- Site-specific rocket emissions
- Construction deadline T
- Emissions budget
- Ground-launch restrictions

**Mathematical model**

Show the port emissions intensity:

e_h = 20g + 1.2

Unit: t CO₂e/t cargo.

Use site-specific emission intensities for direct rocket transportation.

**Computational procedure**

1. Calculate route-specific operating emissions.
2. Construct a fixed-deadline emissions-minimization Linear Programming model.
3. Solve the minimum-cost problem under an emissions cap.
4. Perform electricity-grid carbon-intensity sensitivity analysis.
5. Compare different emissions budgets.
6. Evaluate launch-count restrictions and local ecological constraints.
7. Identify cost–emissions trade-offs and grid break-even thresholds.

**Output**

Include:
- Total operational CO₂e
- Cost–emissions Pareto trade-off
- Minimum feasible emissions
- Carbon-budget feasibility
- Electricity-grid break-even thresholds

Show the 130-year construction scenario:

- Low-carbon grid: 614.65 Mt CO₂e
- High-carbon grid: 1,188.73 Mt CO₂e

Grid break-even values:
- 0.375 t CO₂e/MWh
- 0.560 t CO₂e/MWh

**Validation**
- Emissions unit consistency
- Route-specific emission accounting
- Carbon-budget feasibility
- Launch-count constraints
- Sensitivity boundary checks

Add a small environmental mechanism illustration distinguishing electricity-related emissions from direct rocket-related atmospheric and ecological impacts.

Do not convert high-altitude black carbon and ozone effects into an invented universal emissions coefficient.

## 7. Problem 05 — MCM Agency Recommendation

Panel heading: **05 | MCM Agency Recommendation**

Make this a visually distinct synthesis panel at the bottom.

Show four incoming information streams from Problems 01–04.

**From Problem 01**
- Cost–time Pareto frontier
- Construction schedule
- Optimal route allocation

**From Problem 02**
- Reliability distributions
- P95 completion time
- Buffer optimization

**From Problem 03**
- Initial water requirements
- Emergency reserves
- Operational readiness

**From Problem 04**
- Carbon constraints
- Grid sensitivity
- Environmental trade-offs

**Decision synthesis**

Organize the recommendation workflow:

1. Validate independent transportation throughput.
2. Verify electricity-grid conditions.
3. Prioritize port-based transportation conditionally.
4. Adopt a 124-year internal scheduling target.
5. Prepare a 132-year stress-case construction plan.
6. Maintain three independent port buffers.
7. Secure candidate backup ground-launch windows.
8. Require verified lunar water inventory before settlement occupancy.

**Final output**

A one-page MCM Agency recommendation letter containing:
- Conditional construction schedule
- Transportation priorities
- Reliability safeguards
- Water-readiness requirements
- Environmental policy conditions
- Residual uncertainties and risks

Include a small final decision/approval gate symbol indicating that settlement occupancy is permitted only after actual water-stock verification.

## 8. Inter-panel relationships and arrows

The relationships between panels must accurately represent the actual modeling dependencies.

Use a common-input distribution structure:

Shared Transportation Network & Scenario Inputs
→ Problems 01, 02, 03, 04.

Add the following specific connections:

- Problem 01 → Problem 02:
  "Nominal Dispatch Baseline"
  Indicate that reliability experiments use the shared nominal transportation framework.

- Problem 01 → Problem 03:
  "Construction Capacity Occupancy"
  Show that concurrent water transportation consumes port capacity otherwise available for construction cargo.

- Problem 01 → Problem 05:
  "Cost–Time Frontier & Construction Schedule"

- Problem 02 → Problem 05:
  "P95 Reliability & Buffer Strategy"

- Problem 03 → Problem 05:
  "Water Reserve & Occupancy Readiness"

- Problem 04 → Problem 05:
  "Carbon Constraints & Grid Policy"

Do not create artificial sequential dependencies between Problems 02, 03, and 04. They are distinct analytical investigations sharing common transportation assumptions.

Use a dedicated convergence bus above Problem 05 to collect the four analytical outputs. Keep the lines orthogonal, route them through the spacing between panels, and avoid crossings through node interiors.

Use solid arrows for direct information transfer and dashed arrows for scenario references or sensitivity relationships. Add short English labels to important connections.

## 9. Visual design and academic style

Adopt the visual language of high-quality CVPR, AAAI, and ICLR research-paper figures.

**Visual characteristics**
- White or very light neutral background.
- Clean vector-infographic appearance.
- Precise geometric alignment.
- Thin, consistent borders.
- Rounded rectangular process nodes.
- Restrained use of color.
- Clear distinction between inputs, models, computation, results, and validation.
- Consistent arrowheads and line weights.
- Strong visual hierarchy without oversized headings.
- Generous negative space.
- No decorative elements that do not communicate information.

**Color palette**

Use a restrained aerospace-engineering palette:
- Deep navy: shared system and primary structure.
- Steel blue: ideal construction and electric lift.
- Teal: feeder transportation and water.
- Muted amber: direct rocket transportation and optimization results.
- Muted coral: reliability failures and risk.
- Desaturated green: environmental analysis and validation.
- Light gray: secondary information and assumptions.

Keep the same meaning for each color throughout the figure.

**Typography**
- Professional sans-serif typography similar to Inter, Helvetica, or Arial.
- All diagram labels in English.
- Preserve formulas, subscripts, symbols, numerical values, and units accurately.
- Use concise node descriptions rather than paragraphs.
- Main panel headings should be clearly distinguishable from internal node labels.
- Ensure all text remains readable when the figure is printed at approximately 159 mm width.
- Target approximately 8–10 pt equivalent typography.
- Do not sacrifice readability to fit excessive content.

**Important restrictions**
- No overall figure title.
- No unnecessary legends.
- No unrelated space illustrations.
- No cartoon aesthetic.
- No photorealistic backgrounds.
- No excessive gradients, shadows, or 3D effects.
- No arbitrary extra processes or invented model dependencies.
- No missing numbered subproblems.
- No overlapping arrows or text.
- No illegible microtext.

## 10. Final quality requirements

The finished figure must communicate the complete mathematical modeling workflow at a glance:

1. A shared lunar transportation system and common assumptions.
2. Four independently identifiable analytical subproblems.
3. The actual mathematical models and computational methods used in each problem.
4. The important intermediate mechanisms and optimization procedures.
5. Actual quantitative outputs and validation criteria.
6. Correct information transfer between the analytical problems.
7. A final evidence-based recommendation to the MCM Agency.

Prioritize scientific accuracy, information completeness, structural clarity, and publication-level visual balance over decorative beauty.

The result should look like a carefully designed, professionally typeset research-paper methodology figure, not a generic business-process flowchart.
````
