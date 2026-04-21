# 客户领域 - 客户模型

> 最后更新：2026-04-21

---

## 一、术语表

| 术语 | 英文名 | 定义 | 关联术语 |
|------|--------|------|----------|
| 客户 | Customer | 国外客户，购买服装大货订单的贸易对象 | 订单、联系人、银行账户 |
| 联系人 | Contact | 客户公司的业务对接人 | 客户 |
| 银行账户 | BankAccount | 客户收款银行账户信息 | 客户、币种 |
| 验货要求 | InspectionRequirement | 客户对产品质量的检验要求 | 客户、订单 |
| 验厂要求 | FactoryAuditRequirement | 客户对工厂的社会责任审核要求 | 客户 |
| 信用额度 | CreditLimit | 客户可用的信用额度上限 | 客户、订单 |

---

## 二、实体定义

### 客户（聚合根）

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | string | ✓ | 唯一标识 |
| code | string | ✓ | 客户编码（系统自动生成，CUST001） |
| fullName | string | ✓ | 客户全称 |
| fullNameEn | string | | 英文全称 |
| shortName | string | ✓ | 简称 |
| country | string | ✓ | 国家 |
| phone | string | | 电话 |
| companyType | string | | 公司类型（品牌公司/贸易公司/零售商） |
| address | Address | | 地址（值对象） |
| addressEn | Address | | 英文地址（值对象） |
| developChannel | string | | 开发渠道 |
| customerLevel | enum | | 客户等级（VIP/普通/潜在） |
| paymentTerms | string | | 价格条款（FOB/CIF/DDP等） |
| paymentMethod | string | | 付款方式（T/T/L/C等） |
| selfOwnedBrand | boolean | | 是否自营品牌 |
| brandList | string[] | | 自营品牌列表 |
| remark | string | | 备注 |
| status | enum | ✓ | 客户状态 |
| createdAt | datetime | ✓ | 创建时间 |

### 联系人

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | string | ✓ | 唯一标识 |
| customerId | string | ✓ | 客户ID（聚合内引用） |
| name | string | ✓ | 联系人姓名 |
| phone | string | | 联系电话 |
| email | string | ✓ | 联系人邮箱 |
| isPrimary | boolean | | 是否主联系人 |

### 银行账户

| 属性 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | string | ✓ | 唯一标识 |
| customerId | string | ✓ | 客户ID（聚合内引用） |
| bankName | string | ✓ | 收款银行 |
| accountNo | string | ✓ | 账号 |
| swiftCode | string | | Swift Code |
| bankAddress | Address | | 银行地址（值对象） |
| currency | string | | 结算币种 |
| isDefault | boolean | | 是否默认账户 |

---

## 三、值对象

### 地址（Address）

| 属性 | 类型 | 说明 |
|------|------|------|
| street | string | 街道地址 |
| city | string | 城市 |
| state | string | 省/州 |
| postcode | string | 邵编 |
| country | string | 国家 |

### 验货要求（InspectionRequirement）

| 属性 | 类型 | 说明 |
|------|------|------|
| requirementType | string | 要求类型 |
| description | string | 具体要求描述 |

### 验厂要求（FactoryAuditRequirement）

| 属性 | 类型 | 说明 |
|------|------|------|
| auditType | string | 审核类型 |
| description | string | 具体要求描述 |

### 保险信息（InsuranceInfo）

| 属性 | 类型 | 说明 |
|------|------|------|
| isInsured | boolean | 是否投保 |
| buyerCode | string | 买方代码 |
| insuredRatio | decimal | 投保比例 |
| effectiveLimit | decimal | 生效额度 |

---

## 四、聚合边界

**聚合：客户聚合**

- 聚合根：客户
- 内部实体：联系人（可多个）、银行账户（可多个）
- 值对象：地址、验货要求、验厂要求、保险信息

**聚合间引用**：

| 聚合A | 聚合B | 引用方式 |
|-------|-------|----------|
| 订单聚合 | 客户聚合 | customerId |
| 客户聚合 | 基础数据聚合 | currencyId, countryId |

---

## 五、业务规则

| 规则ID | 规则描述 | 来源 | 适用场景 |
|--------|----------|------|----------|
| R01 | 客户编码系统自动生成 | 用户确认 | 创建客户 |
| R02 | 客户必须有至少一个主联系人 | 业务规则 | 创建客户 |
| R03 | 客户必须有至少一个银行账户 | 财务规则 | 首次下单前 |
| R04 | 客户状态为暂停合作时不能下新订单 | 业务规则 | 创建订单 |
| R05 | 客户注销前必须无未完成订单 | 业务规则 | 注销客户 |

---

## 六、数据流图

> 待补充

---

## 七、业务场景

> 待补充

---

## 八、补充文件

> 大模型判断：状态机已定义且涉及信用问题等复杂流转，拆分独立文件

| 文件 | 内容 | 状态 |
|------|------|------|
| customer-state.md | 状态机 | 已拆分 |
| customer-flow.md | 数据流图 | 合并在主文件（待补充） |
| customer-scene.md | 业务场景 | 合并在主文件（待补充） |