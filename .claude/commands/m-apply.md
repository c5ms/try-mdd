---
description: 批量应用方案到领域模型。用法：/m-apply
---

批量将 solution 目录中的方案更新到 domain 目录。

---

## 流程

```
搜索方案 → 用户确认 → 执行更新 → 清理方案
```

---

## 步骤

### 1. 搜索所有方案

搜索 `solution/` 目录下所有的方案文件：

```
solution/{domain}/solution.md
```

列出所有待应用的方案。

---

### 2. 用户确认

使用 **AskUserQuestion** 询问用户：

> 发现以下待应用方案，请选择要更新到 domain 目录的方案：

**选项**：多选，列出所有方案目录名

---

### 3. 执行更新

对用户确认的每个方案：

1. 读取 `solution/{domain}/solution.md`
2. 调用 `mdd-apply` skill 生成 `domain/{domain}/model.md`
3. 删除 `solution/{domain}/solution.md`

---

### 4. 输出结果

```
应用完成：

已更新：
- domain/{domain1}/model.md    —— {领域1} 领域模型
- domain/{domain2}/model.md    —— {领域2} 领域模型

已清理：
- solution/{domain1}/solution.md
- solution/{domain2}/solution.md
```

---

## 约束

- 用户必须确认后才执行更新
- 更新成功后才删除方案文件
- 方案目录保留（仅删除 solution.md）