---
description: 业务模型推演入口。用法：/m-design <领域名称> <业务描述>
---

领域名称：$ARGUMENTS

启动设计推演：读取规约 → 确定角色 → 明确需求 → 角色评审 → 输出方案 → 用户确认 → 更新设计。

---

## 输入

用户需要提供：
- 领域名称（如：订单、采购、库存）
- 业务描述（自然语言，如：订单属于一个客户，每个订单包含多个sku...）

如果未提供业务描述，使用 **AskUserQuestion** 询问：
> "请描述这个业务领域的核心实体、状态、规则。"

---

## 步骤

### 1. 读取规约

读取设计规约：
- `config/rules.md` —— DDD 建模规约（设计原则）
- `config/roles.md` —— 角色定义（参与设计的角色）

### 2. 调用 mdd-design skill

使用 **Skill** 工具调用 `mdd-design` skill 执行推演。

### 3. 输出确认

推演完成后，告知用户：
- 待确认方案：`solution/{domain}/solution.md`
- 设计结果：`domain/{domain}/model.md`（如用户确认）

---

## 输出

完成后输出：
```
推演完成：

待确认方案：
- solution/{domain}/solution.md

设计结果（如已确认）：
- domain/{domain}/model.md    —— 领域模型（实体、聚合、状态机、规则、数据流、场景）
```

---

## 约束

- 用户原话必须在方案中保留
- 每个方案必须经过角色评审
- 设计输出整合到单文件 `model.md`