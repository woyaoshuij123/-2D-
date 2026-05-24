# 毛绒玩具全自动上架 API 系统方案

## 目标
通过 API 把毛绒玩具产品从图片与基础资料自动生成商品草稿，并推送到电商平台。

推荐先做“自动创建草稿商品”，人工确认后再发布，避免平台风控、类目错误、价格错误、侵权词误用。

---

## 系统流程

```text
产品图片 + 基础参数
  ↓
AI 生成商品资料
  ↓
图片上传到平台图片空间 / 云存储
  ↓
生成标题、卖点、详情页、SKU、关键词
  ↓
调用平台商品 API 创建商品草稿
  ↓
人工审核
  ↓
发布商品
```

---

## 必备模块

1. `product_input`
   - 接收产品图片、尺寸、价格、库存、材质、发货地、包装方式。

2. `ai_listing_generator`
   - 生成中文标题、英文标题、卖点、详情页、短视频脚本、关键词、SKU。

3. `image_uploader`
   - 上传主图、详情图、白底图、视频封面到平台图片空间或云存储。

4. `platform_adapter`
   - 对接淘宝、抖店、TikTok Shop、拼多多等平台 API。

5. `risk_checker`
   - 检查侵权词、敏感词、未授权 IP、明星姓名、影视游戏角色名称。

6. `publish_controller`
   - 先创建草稿，再审核发布。

---

## 通用商品 JSON

```json
{
  "title": "国风少年将军毛绒玩具 Q版银甲武将公仔 古风棉花娃娃",
  "category": "plush_toy",
  "brand": "",
  "description": "这是一款国风少年将军造型毛绒玩具，整体采用Q版软萌比例设计...",
  "main_images": [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg"
  ],
  "detail_images": [
    "https://example.com/detail1.jpg"
  ],
  "attributes": {
    "material": "短毛绒 + PP棉",
    "size": "20cm",
    "color": "白银色",
    "style": "国风 / Q版 / 软萌",
    "package": "OPP袋"
  },
  "skus": [
    {
      "sku_name": "普通款",
      "price": 89,
      "stock": 100,
      "seller_sku": "PLUSH-WARRIOR-20CM-NORMAL"
    },
    {
      "sku_name": "礼盒款",
      "price": 129,
      "stock": 50,
      "seller_sku": "PLUSH-WARRIOR-20CM-GIFT"
    }
  ],
  "shipping": {
    "warehouse": "默认仓",
    "delivery_days": 2,
    "weight_kg": 0.35
  },
  "risk_status": "need_manual_review"
}
```

---

## API 目录结构建议

```text
plush-auto-listing-api/
  README.md
  .env.example
  src/
    app.py
    config.py
    ai_listing_generator.py
    risk_checker.py
    image_uploader.py
    adapters/
      base.py
      tiktok_shop.py
      douyin_shop.py
      taobao.py
      pinduoduo.py
    data/
      product_example.json
```

---

## .env.example

```env
OPENAI_API_KEY=你的AI接口Key
PLATFORM=TIKTOK_SHOP
SHOP_ID=你的店铺ID
APP_KEY=平台AppKey
APP_SECRET=平台AppSecret
ACCESS_TOKEN=平台AccessToken
REFRESH_TOKEN=平台RefreshToken
IMAGE_BUCKET=你的图片空间或对象存储
DEFAULT_WAREHOUSE_ID=默认仓库ID
DEFAULT_CATEGORY_ID=平台毛绒玩具类目ID
```

---

## 平台接入重点

### TikTok Shop
需要：
- TikTok Shop 开发者账号
- App Key / App Secret
- 店铺授权
- Access Token
- 类目 ID
- 商品创建接口
- 图片上传接口
- 库存与价格接口

建议流程：
1. 上传图片
2. 获取图片 URL 或 URI
3. 查询类目属性
4. 创建商品草稿
5. 设置 SKU、价格、库存
6. 提交审核

### 抖店
需要：
- 抖店开放平台应用
- 店铺授权
- 商品发布接口
- 图片素材接口
- 类目属性接口
- 运费模板 ID

### 淘宝 / 天猫
需要：
- 淘宝开放平台应用
- 店铺授权
- 商品 API 权限
- 图片空间接口
- 类目属性接口

### 拼多多
需要：
- 拼多多开放平台应用
- 店铺授权
- 商品发布接口
- SKU 接口
- 图片上传接口

---

## 风控建议

全自动发布不要直接一步发布，建议先创建草稿。必须检查：

- 是否包含未授权 IP 名称
- 是否包含明星、运动员、影视剧、动漫、游戏角色名字
- 是否使用别人商品图
- 是否写了虚假材质或虚假尺寸
- 是否价格、库存、运费模板正确
- 是否符合平台类目要求

安全命名示例：
- 国风少年将军
- 银甲小武将
- 古风弓箭少年
- Q版将军毛绒玩偶

不建议直接写具体影视、动漫、游戏、明星或运动员名称，除非有授权。

---

## 下一步实施

要真正跑起来，需要确认你要先接哪个平台：

1. TikTok Shop
2. 抖店
3. 淘宝 / 天猫
4. 拼多多
5. 1688
6. Shopify / 独立站

确认平台后，需要拿到：

- 开放平台应用 App Key
- App Secret
- 店铺授权 Token
- 图片上传接口权限
- 商品发布接口权限
- 平台类目 ID
- 运费模板 ID
- 默认仓库 ID

拿到这些后，就可以写正式代码，实现自动生成商品草稿。
