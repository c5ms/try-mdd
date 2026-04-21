# 订单领域 - 销售订单模型

> 最后更新：2026-04-21

---

## 一、术语表

| 术语 | 英文名 | 定义 | 关联术语 |
|------|--------|------|----------|
| 销售订单 | SalesOrder | 客户下达的成衣大货订单 | 客户、订单明细、SKU |
| 订单明细 | OrderLine | 订单中的具体SKU条目，包含颜色尺码 | 订单、SKU |
| SKU | SKU | 具体的颜色尺码组合 | 订单明细、产品 |
| 成衣 | Garment | 服装产品的统称 | SKU、订单 |
| 大货订单 | BulkOrder | 大批量生产的正式订单 | 订单 |

---

## 二、实体定义

### 销售订单（聚合根）

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | string | ✓ | 唯一标识 |
| orderNo | string | ✓ | 订单编号（系统自动生成） |
| customerId | string | ✓ | 客户ID（聚合间引用） |
| orderType | enum | ✓ | 订单类型（大货订单） |
| productCategory | string | ✓ | 产品类别（成衣类型） |
| totalQuantity | int | ✓ | 总数量 |
| totalAmount | decimal | ✓ | 订单总金额（明细累加） |
| currency | string | ✓ | 订单币种 |
| deliveryDate | date | ✓ | 交货日期 |
| inspectionRequirement | InspectionRequirement | | 验货要求 |
| factoryAuditRequirement | FactoryAuditRequirement | | 验厂要求 |
| paymentStatus | enum | | 付款状态 |
| remark | string | | 备注 |
| attachments | string[] | | 附件列表（PO文档等） |
| productionId | string | | 生产单ID（关联生产管理聚合） |
| status | enum | ✓ | 订单状态（待定） |
| createdBy | string | ✓ | 创建人（业务员） |
| createdAt | datetime | ✓ | 创建时间 |
| updatedAt | datetime | | 更新时间 |

### 订单明细

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | string | ✓ | 唯一标识 |
| orderId | string | ✓ | 订单ID（聚合内引用） |
| skuCode | string | ✓ | SKU编码 |
| color | string | ✓ | 颜色 |
| size | string | ✓ | 尺码 |
| quantity | int | ✓ | 数量 |
| unitPrice | decimal | ✓ | 单价 |
| totalPrice | decimal | ✓ | 小计金额（数量×单价） |

---

## 三、值对象

### 验货要求（继承客户领域）

| 属性 | 类型 | 说明 |
|------|------|------|
| requirementType | string | 要求类型 |
| description | string | 具体要求描述 |

### 验厂要求（继承客户领域）

| 属性 | 类型 | 说明 |
|------|------|------|
| auditType | string | 审核类型 |
| description | string | 具体要求描述 |

---

## 四、聚合边界

**聚合：订单聚合**

- 聚合根：销售订单
- 内部实体：订单明细（可多个）
- 值对象：验货要求、验厂要求

**聚合间引用**：

| 聚合A | 聚合B | 引用方式 |
|-------|-------|----------|
| 订单聚合 | 客户聚合 | customerId |
| 订单聚合 | 生产聚合 | productionId |
| 订单聚合 | 财务聚合 | orderId（双向） |

---

## 五、状态机

> 待用户研究确认订单状态流转

---

## 六、业务规则

| 规则ID | 规则描述 | 来源 | 适用场景 |
|--------|----------|------|----------|
| R01 | 订单金额 = SUM(明细数量 × 单价) | 用户确认 | 创建/修改订单 |
| R02 | 订单创建需校验客户信用额度 | 财务主管 | 创建订单 |
| R03 | 订单编号系统自动生成 | 系统架构师 | 创建订单 |
| R04 | 客户状态为暂停合作时不能下新订单 | 客户管理规约 | 创建订单 |
| R05 | 验货验厂要求默认继承客户设置 | 业务经理 | 创建订单 |
| R06 | 订单明细数量和单价修改需同步更新总金额 | 系统架构师 | 修改订单 |

---

## 七、数据流图

> 待补充

---

## 八、业务场景

> 待补充

---

## 九、补充文件

> 大模型判断：状态机待定、数据流图待补充、业务场景待补充，不拆分补充文件

| 文件 | 内容 | 状态 |
|------|------|------|
| order-state.md | 状态机 | 合并在主文件（待用户确认） |
| order-flow.md | 数据流图 | 合并在主文件（待补充） |
| order-scene.md | 业务场景 | 合并在主文件（待补充） |