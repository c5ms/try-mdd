# MDD 设计引擎

## 一、核心原则（必读）

> **重要**：以下规则为硬性约束，AI 必须严格遵守，在输出时保持自己的立场，根据自己的专业知识做判断，不要迎合用户。

### 1. 设计规范（量化标准）

| 规则 | 明确定义 | 验收标准 | 示例 |
|------|----------|----------|------|
| **角色必须参与** | 每个设计方案必须经过角色评审 | 有角色评审记录 | ✅ 有角色评审汇总 ❌ 直接输出方案 |
| **用户原话保留** | 用户原始描述必须保留在方案中 | 方案包含用户原话章节 | ✅ `> 用户原话："{...}"` ❌ 仅整理内容 |
| **待定任务记录** | 不确定项必须记录到待定清单 | 有待定任务表格 | ✅ 待定任务表格 ❌ 直接忽略 |
| **用户确认** | 更新设计前必须经用户确认 | 有用户确认步骤 | ✅ AskUserQuestion ❌ 直接写入 |
| **规约遵循** | 推演必须遵循 DDD 建模规约 | 聚合边界明确、术语一致 | ✅ 聚合间通过 ID 引用 ❌ 直接持有对象 |

### 2. 输出规范

| 规则 | 说明 |
|------|------|
| **简洁输出** | 优先使用符号、表格、列表、代码片段回答 |
| **禁止冗余** | 不添加"以下是内容"等前缀/后缀 |

---

## 二、工作流

```
用户: /m-design 订单业务模型，订单属于一个客户...
  ↓
读取规约 → config/rules.md（设计原则）
  ↓
确定角色 → config/roles.md（角色视角）
  ↓
明确需求 → 用户输入（AI理解整理）
  ↓
角色评审 → 逐角色分析方案，提出意见
  ↓
输出方案 → solution/{domain}.md（待确认方案）
  ↓
用户确认 → 是否更新到领域模型目录？
  ↓
更新设计 → design/domain/{domain}/model.md（最终设计）
```

---

## 三、目录结构

```
.agents/
  commands/
    m-design.md           # /m-design 设计入口
    m-evolve.md           # /m-evolve 讨论/推理助手
    m-init.md             # /m-init 项目初始化
    m-apply.md            # /m-apply 批量应用方案
    m-role.md             # /m-role 创建新角色
  skills/
    mdd-design/
      SKILL.md            # 设计推演（内置模板）
    mdd-evolve/
      SKILL.md            # 讨论/推理助手（仅对话）
    mdd-init/
      SKILL.md            # 项目初始化
    mdd-apply/
      SKILL.md            # 批量应用方案
    mdd-reflect/
      SKILL.md            # 反思改进

config/
  rules.md                # 设计原则（DDD 建模规约）
  roles.md                # 角色定义（参与设计的角色）

solution/
  {domain}.md             # 待确认方案（角色评审后）

design/
  domain/
    {domain}/
      model.md            # 领域模型（整合：实体、聚合、状态机、规则、数据流、场景）
  model.md                # 领域模型汇总（统一术语表、领域模型图、待定项汇总、演进记录）

reflect/
  YYYY-MM-DD-{主题}.md    # 反思记录（按日期归档）
```

### 目录权限

| 目录 | 写入时机 | 内容性质 |
|------|----------|----------|
| `solution/` | 评审阶段 | 待确认方案 |
| `design/domain/` | 确认阶段 | 最终设计结果 |
| `design/model.md` | 确认阶段 | 领域模型汇总 |

---

## 四、Commands

| Command | 用途 | 文档 |
|---------|------|------|
| `/m-init` | 项目初始化 | `.agents/commands/m-init.md` |
| `/m-design {domain}` | 初始设计推演 | `.agents/commands/m-design.md` |
| `/m-apply` | 批量应用方案到领域模型 | `.agents/commands/m-apply.md` |
| `/m-evolve <问题或假设>` | 讨论/推理助手（仅对话） | `.agents/commands/m-evolve.md` |
| `/m-role {角色名}` | 创建新角色 | `.agents/commands/m-role.md` |
| `/m-reflect [主题]` | 反思推演错误 | `.agents/commands/m-reflect.md` |

---

## 五、Skills

| Skill | 用途 | 文档 |
|-------|------|------|
| `mdd-init` | 确认项目 → 设计角色 → 确定准则 → 初始化目录 | `.agents/skills/mdd-init/SKILL.md` |
| `mdd-design` | 读取规约 → 角色评审 → 输出方案 → 更新设计 | `.agents/skills/mdd-design/SKILL.md` |
| `mdd-apply` | 搜索方案 → 用户确认 → 执行更新 → 更新汇总 → 清理方案 | `.opencode/skills/mdd-apply/SKILL.md` |
| `mdd-evolve` | 用户迷茫 → 给出方向 → 用户选择 → 深入讨论 → 理清思路（仅对话） | `.agents/skills/mdd-evolve/SKILL.md` |
| `mdd-reflect` | 推演错误 → 根因分析 → 改进建议 | `.agents/skills/mdd-reflect/SKILL.md` |

---

## 六、场景索引（按设计任务导航）

### 设计场景

| 场景 | 使用命令 | 说明 |
|------|----------|------|
| 新项目初始化 | `/m-init` | 确认定位、设计角色、确定准则、初始化目录 |
| 领域模型设计 | `/m-design {domain}` | 读取规约 → 角色评审 → 输出方案 → 更新设计 |
| 批量应用方案 | `/m-apply` | 搜索方案 → 用户确认 → 执行更新 → 更新汇总 → 清理方案 |
| 迷茫求建议 | `/m-evolve <问题>` | 给出方向 → 用户选择 → 深入讨论 → 理清思路 |
| 推理假设后果 | `/m-evolve <假设>` | 推理后果 → 给出分析 → 继续讨论 |
| 创建新角色 | `/m-role {角色名}` | 确认属性 → 检查重复 → 写入 roles.md |
| 反思改进 | `/m-reflect [主题]` | 错误梳理 → 根因分析 → 改进建议 |

### 规约场景

| 场景 | 文档 | 说明 |
|------|------|------|
| DDD 建模规约 | `config/rules.md` | 实体、聚合、状态机建模规则 |
| 角色定义 | `config/roles.md` | 参与设计的角色及视角 |

---

## 七、规约索引

| 规约 | 文件 | 适用范围 |
|------|------|----------|
| DDD 建模规约 | [config/rules.md](config/rules.md) | 全局 |
| 设计参与角色 | [config/roles.md](config/roles.md) | 全局 |

---

## 八、规约约束机制（量化）

| 规则 | 触发时机 | 验收标准 | 禁止原因 |
|------|----------|----------|----------|
| 推演前读取 | `/m-design` 启动时 | 已读取 rules.md + roles.md | 规约是设计依据，不读取会违反 DDD 规范 |
| 角色必须参与 | 方案输出前 | 有角色评审汇总章节 | 单视角设计会遗漏场景，角色协作补充遗漏 |
| 术语一致性 | 方案输出时 | 使用术语表中的术语 | 术语不一致会导致理解歧义 |
| 边界完整性 | 聚合设计时 | 聚合边界明确定义 | 边界不明确会导致一致性失控 |
| 用户原话保留 | 方案输出时 | 有用户原话章节 | 用户原话是设计依据，丢失会失去追溯 |
| 用户确认 | 更新设计前 | 有 AskUserQuestion 步骤 | 直接写入会绕过用户决策权 |
| 聚合间引用 | 聚合设计时 | 通过 ID 引用 | 直接持有对象会违反 DDD 聚合边界原则 |