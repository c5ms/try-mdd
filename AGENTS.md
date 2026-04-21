# MDD 设计引擎

## 工作流

```
用户: /m-design 订单业务模型，订单属于一个客户...
  ↓
理解整理 → inputs/{domain}/input.md（原始需求）
  ↓
推演设计 → outputs/domain/{domain}/（设计结果）

用户: /m-evolve 客户取消订单并赔偿...
  ↓
分析影响 → outputs/domain/{domain}/（追加变更）
  ↓
输出用例 → usecases/{domain}/{场景}.md（场景记录）
```

---

## 目录结构

```
.agents/
  commands/
    m-design.md           # /m-design 设计入口
    m-evolve.md           # /m-evolve 推演入口
  skills/
    mdd-design/
      SKILL.md            # 设计推演
      references/         # 产出模板
    mdd-evolve/
      SKILL.md            # 场景推演

inputs/
  {domain}/
    input.md              # 原始需求记录（AI整理）

outputs/
  domain/
    {domain}/
      model.md            # 业务模型（AI推演，追加变更）
      states.md           # 状态机（AI推演，追加变更）
      rules.md            # 业务规则（AI推演，追加变更）
      flows.md            # 用例流程图（AI推演，追加变更）

usecases/
  {domain}/
    {场景}.md             # 场景用例（推演输出）
```

---

## 权限

| 目录 | 写入时机 | 内容性质 |
|------|----------|----------|
| `inputs/` | 设计阶段 | 原始需求记录 |
| `outputs/` | 设计/推演阶段 | 设计结果（追加变更） |
| `usecases/` | 推演阶段 | 场景用例记录 |

---

## Commands

| Command | 用途 |
|---------|------|
| `/m-design {domain}` | 初始设计推演 |
| `/m-evolve {场景}` | 场景推演，更新设计 |
| `/m-reflect [主题]` | 反思推演错误，改进系统 |

---

## Skills

| Skill | 用途 |
|-------|------|
| `mdd-design` | 原始需求 → 初始设计 |
| `mdd-evolve` | 新场景 → 变更设计 + 输出用例 |
| `mdd-reflect` | 推演错误 → 根因分析 → 改进建议 |

---

## 目录结构（完整）

```
.agents/
  commands/
    m-design.md           # /m-design 设计入口
    m-evolve.md           # /m-evolve 推演入口
    m-reflect.md          # /m-reflect 反思入口
  skills/
    mdd-design/
      SKILL.md            # 设计推演
      references/         # 产出模板
    mdd-evolve/
      SKILL.md            # 场景推演
    mdd-reflect/
      SKILL.md            # 反思改进

inputs/
  {domain}/
    input.md              # 原始需求记录（AI整理）

outputs/
  domain/
    {domain}/
      model.md            # 业务模型（追加变更）
      states.md           # 状态机（追加变更）
      rules.md            # 业务规则（追加变更）
      flows.md            # 用例流程图（追加变更）

usecases/
  {domain}/
    {场景}.md             # 场景用例（推演输出）

reflect/
  YYYY-MM-DD-{主题}.md    # 反思记录（按日期归档）
```