---
description: 业务场景推演入口。用法：/m-evolve <场景描述>
---

场景描述：$ARGUMENTS

基于现有设计，推演新场景对业务模型的影响。

---

## 工作流

```
用户: /m-evolve 客户取消订单并赔偿...
  ↓
读取现有设计 outputs/domain/{domain}/
  ↓
推演场景影响 → 更新设计
  ↓
输出场景用例 usecases/{domain}/
```

---

## 输入

用户需要提供：
- 场景描述（如：客户随时可能取消订单，需要赔偿处理）

如果未指定领域，使用 **AskUserQuestion** 询问：
> "这个场景属于哪个业务领域？"

---

## 步骤

### 1. 确定领域

- 读取 `inputs/{domain}/input.md` 获取领域上下文
- 如果不明确，询问用户

### 2. 读取现有设计

读取当前设计状态：
- `outputs/domain/{domain}/model.md`
- `outputs/domain/{domain}/states.md`
- `outputs/domain/{domain}/rules.md`

### 3. 调用 mdd-evolve skill

使用 **Skill** 工具调用 `mdd-evolve` skill 执行推演。

### 4. 输出确认

将推演结论更新到 `outputs/domain/{domain}/`：

- 在文件末尾追加「推演变更记录」章节
- 标注变更来源（场景推演）
- 保留原设计内容

### 5. 输出场景用例

将场景作为用例写入 `usecases/{domain}/`：

- 文件命名：`{场景关键词}.md`
- 包含：场景描述、前置条件、流程、影响分析

---

## 输出

完成后输出：
```
推演完成：

设计变更：
- outputs/domain/{domain}/model.md    —— +{变更内容}
- outputs/domain/{domain}/states.md   —— +{变更内容}
- outputs/domain/{domain}/rules.md    —— +{变更内容}

场景用例：
- usecases/{domain}/{场景}.md
```

---

## 约束

- 推演变更追加到现有设计末尾，不覆盖原内容
- 每个变更标注来源和推演依据
- 场景用例独立存储，便于追溯