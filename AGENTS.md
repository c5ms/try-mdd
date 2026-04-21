# MDD 设计引擎

## 工作流

```
用户: /m-design 订单业务模型，订单属于一个客户...
  ↓
command: .agents/commands/m-design.md
  ↓
skill: .agents/skills/mdd-design/SKILL.md
  ↓
读取: inputs/{domain}/input.md
  ↓
产出: outputs/domain/{domain}/
```

---

## 目录结构

```
.agents/
  commands/
    m-design.md           # /m-design 命令入口
  skills/
    mdd-design/
      SKILL.md            # 推演流程
      references/         # 产出模板

inputs/
  {domain}/
    input.md              # 用户对话记录（人写，AI禁改）

outputs/
  domain/
    {domain}/
      model.md            # 业务模型（AI写）
      states.md           # 状态机（AI写）
      rules.md            # 业务规则（AI写）
      flows.md            # 用例流程图（AI写）
```

---

## 权限

| 目录 | 权限 |
|------|------|
| `inputs/` | 用户写，AI 只读 |
| `outputs/` | AI 写，每次覆盖 |

---

## Commands

| Command | 用途 |
|---------|------|
| `/m-design {domain}` | 启动设计推演 |

---

## Skills

| Skill | 用途 |
|-------|------|
| `mdd-design` | 读取对话 → 分析推演 → 产出文档 |