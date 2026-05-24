# AIToy 淘宝自动上架系统安装说明

## 1. 安装环境

建议使用：

- Python 3.10+
- Windows 10/11 或 Linux 服务器
- 淘宝开放平台应用
- 淘宝店铺授权 SessionKey

---

## 2. 安装步骤

### 第一步：下载项目

```bash
git clone https://github.com/woyaoshuij123/-2D-.git
cd -2D-/aitoy-taobao-auto-listing
```

### 第二步：创建虚拟环境

Windows：

```bash
python -m venv .venv
.venv\Scripts\activate
```

Mac / Linux：

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 第三步：安装依赖

```bash
pip install -r requirements.txt
```

### 第四步：配置淘宝 API

复制配置文件：

```bash
copy .env.example .env
```

Mac / Linux：

```bash
cp .env.example .env
```

然后填写：

```env
TAOBAO_APP_KEY=你的AppKey
TAOBAO_APP_SECRET=你的AppSecret
TAOBAO_SESSION_KEY=你的SessionKey
TAOBAO_GATEWAY=https://eco.taobao.com/router/rest
DEFAULT_STATE=浙江
DEFAULT_CITY=金华
DEFAULT_CATEGORY_ID=你的毛绒玩具类目ID
DEFAULT_SHIPPING_TEMPLATE_ID=你的运费模板ID
```

不要把 `.env` 上传到 GitHub。

---

## 3. 运行测试

```bash
python src/main.py
```

系统会读取 `data/product_example.json`，生成淘宝上架参数，并执行风险检测。

默认不会直接发布正式商品。第一版建议只创建草稿或打印 API 参数。

---

## 4. AIToy 第一版功能

- 毛绒玩具商品资料标准化
- 淘宝标题生成
- 商品详情生成
- SKU 生成
- 侵权词/风险词检测
- 淘宝 TOP API 签名
- 商品发布接口骨架
- 图片上传接口骨架

---

## 5. 真实发布前必须准备

- 淘宝开放平台 App Key
- 淘宝开放平台 App Secret
- 店铺授权 SessionKey
- 商品发布接口权限
- 图片空间上传权限
- 商品类目 ID
- 必填属性 props
- 运费模板 ID
- 发货地

---

## 6. 安全建议

建议先自动创建草稿，人工确认后再发布。不要直接发布带有未授权 IP、明星名、影视动漫游戏角色名的商品。