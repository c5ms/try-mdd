---
description: 业务模型推演入口。用法：/m-design <领域名称>
---

领域名称：$ARGUMENTS

启动设计推演，读取用户对话记录，产出业务模型、状态机、规则、流程图。

---

## 输入

用户需要提供：
- 领域名称（如：订单、采购、库存）
- 或直接描述要设计的业务

如果未提供输入，使用 **AskUserQuestion** 询问：
> "你要推演什么业务领域？请描述核心实体和业务场景。"

---

## 步骤

### 1. 确认领域名称

- 如果用户提供了领域名称，确认并继续
- 如果未提供，询问用户

### 2. 检查输入文件

检查 `inputs/{domain}/input.md` 是否存在：
- 存在 → 读取对话记录，开始推演
- 不存在 → 使用 **AskUserQuestion** 询问是否创建新领域

### 3. 调用 mdd-design skill

使用 **Skill** 工具调用 `mdd-design` skill 执行推演流程。

### 4. 输出确认

推演完成后，告知用户：
- 产出文件路径（`outputs/domain/{domain}/`）
- 询问是否需要调整或补充

---

## 输出

完成后输出：
```
推演完成：
- outputs/domain/{domain}/model.md    —— 业务模型
- outputs/domain/{domain}/states.md   —— 状态机
- outputs/domain/{domain}/rules.md    —— 业务规则  
- outputs/domain/{domain}/flows.md    —— 用例流程图
```

---

## 约束

- 必须调用 mdd-design skill 执行推演
- 输入文件路径：`inputs/{domain}/input.md`
- 输出文件路径：`outputs/domain/{domain}/`