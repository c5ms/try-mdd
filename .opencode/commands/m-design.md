---
description: 业务模型推演入口。用法：/m-design <领域名称> <业务描述>
---

领域名称：$ARGUMENTS

启动设计推演，理解用户输入 → 整理原始需求 → 推演设计结果。

---

## 输入

用户需要提供：
- 领域名称（如：订单、采购、库存）
- 业务描述（自然语言，如：订单属于一个客户，每个订单包含多个sku...）

如果未提供业务描述，使用 **AskUserQuestion** 询问：
> "请描述这个业务领域的核心实体、状态、规则。"

---

## 步骤

### 1. 理解整理

将用户的自然语言输入理解整理后，写入 `inputs/{domain}/input.md`：

```markdown
# 原始需求记录

## 领域名称
{domain}

## 核心实体
- {从用户描述提取的实体}

## 关联关系
- {从用户描述提取的关系}

## 状态定义
- {从用户描述提取的状态}

## 业务规则
- {从用户描述提取的约束}

## 用例场景
- {从用户描述提取的场景}

---
用户原话："{用户原始描述}"
```

### 2. 调用 mdd-design skill

使用 **Skill** 工具调用 `mdd-design` skill 执行推演。

### 3. 输出确认

推演完成后，告知用户：
- 原始需求记录：`inputs/{domain}/input.md`
- 设计结果：`outputs/domain/{domain}/`

---

## 输出

完成后输出：
```
推演完成：

原始需求记录：
- inputs/{domain}/input.md

设计结果：
- outputs/domain/{domain}/model.md    —— 业务模型
- outputs/domain/{domain}/states.md   —— 状态机
- outputs/domain/{domain}/rules.md    —— 业务规则
- outputs/domain/{domain}/flows.md    —— 用例流程图
```

---

## 约束

- `inputs/`：AI 整理用户输入后写入（原始需求记录）
- `outputs/`：AI 推演后写入（设计结果）
- 用户原话必须保留在 `input.md` 末尾