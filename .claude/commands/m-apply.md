---
description: 批量应用方案到领域模型。用法：/m-apply
---

批量将 draft 目录中的草稿更新到 design 目录。

---

## 流程

```
搜索方案 → 用户确认 → 执行更新 → 清理方案
```

---

## 步骤

### 1. 搜索所有方案

搜索 `draft/` 目录下所有的草稿文件：

```
draft/{domain}.md
```

列出所有待应用的草稿。

---

### 2. 用户确认

使用 **AskUserQuestion** 询问用户：

> 发现以下待应用方案，请选择要更新到 domain 目录的方案：

**选项**：多选，列出所有方案目录名

---

### 3. 执行更新

对用户确认的每个草稿：

1. 读取 `draft/{domain}.md`
2. 调用 `mdd-apply` skill 生成 `design/domain/{domain}.md`
3. 删除 `draft/{domain}.md`

---

### 4. 输出结果

```
应用完成：

已更新：
- design/domain/{domain1}.md    —— {领域1} 领域模型
- design/domain/{domain2}.md    —— {领域2} 领域模型

已清理：
- draft/{domain1}.md
- draft/{domain2}.md
```

---

## 约束

- 用户必须确认后才执行更新
- 更新成功后才删除草稿文件