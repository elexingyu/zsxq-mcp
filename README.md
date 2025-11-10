# ZSXQ MCP Server

知识星球（Zhishixingqiu）MCP 服务器 - 通过 Model Context Protocol 自动发布内容到知识星球。

## 功能特性

- ✅ **发布主题**：发布文字内容到知识星球
- ✅ **图片上传**：支持上传并发布带图片的主题（已实现！）
- ✅ **文件读取**：从本地文件读取内容发布
- ✅ **灵活配置**：支持环境变量配置和参数传递
- ✅ **Cookie 认证**：使用浏览器 Cookie 进行身份验证

## 安装

### 方法一：使用 UVX 快速启动（推荐）

🚀 **无需预先安装依赖，一键启动！**

```bash
cd zsxq-mcp
./start_with_uvx.sh
```

或直接使用 uvx：
```bash
cd zsxq-mcp
uvx --from . python -m zsxq_mcp.server
```

> 📖 **详细说明**: 查看 [UVX_STARTUP.md](./UVX_STARTUP.md) 了解完整的 uvx 使用指南

### 方法二：传统安装

#### 1. 克隆或创建项目

```bash
cd zsxq-mcp
```

#### 2. 安装依赖

```bash
pip install -e .
```

## 配置

> 📖 **详细配置指南**: 查看 [CONFIGURATION.md](./CONFIGURATION.md) 获取完整的配置说明

### 快速配置步骤

#### 1. 获取知识星球 Cookie

1. 在浏览器中登录知识星球（https://wx.zsxq.com/）
2. 打开浏览器开发者工具（F12）
3. 进入 Network（网络）标签
4. 刷新页面，找到任意 API 请求
5. 在请求头中找到 `Cookie` 字段，复制完整的 Cookie 值

#### 2. 获取星球 ID

- 访问你的星球页面，URL 中包含星球 ID
- 例如：`https://wx.zsxq.com/group/28885518425541` 中的 `28885518425541` 就是星球 ID

#### 3. 配置 Claude Desktop

在 Claude Desktop 配置文件中添加：

**MacOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

**使用 uvx 启动（推荐）**：
```json
{
  "mcpServers": {
    "zsxq": {
      "command": "uvx",
      "args": [
        "--from",
        "/path/to/your/zsxq-mcp",
        "python",
        "-m",
        "zsxq_mcp.server"
      ],
      "env": {
        "ZSXQ_COOKIE": "your_cookie_value_here",
        "ZSXQ_GROUP_ID": "28885518425541"
      }
    }
  }
}
```

**传统方式启动**：
```json
{
  "mcpServers": {
    "zsxq": {
      "command": "python3",
      "args": ["-m", "zsxq_mcp.server"],
      "cwd": "/path/to/your/zsxq-mcp",
      "env": {
        "ZSXQ_COOKIE": "your_cookie_value_here",
        "ZSXQ_GROUP_ID": "28885518425541"
      }
    }
  }
}
```

**配置说明**：
- `command`: 使用 `uvx`（推荐）或 `python3` 命令
- `args[--from]`: 项目路径，修改为你的项目实际路径
- `cwd`: 仅在使用 `python3` 时需要，修改为你的项目实际路径
- `env.ZSXQ_COOKIE`: 粘贴你从浏览器复制的完整 Cookie 值
- `env.ZSXQ_GROUP_ID`: 填入你的星球 ID（可选，如果不设置则每次调用需要指定）

重启 Claude Desktop 后即可使用。

### 可用工具

#### 1. `publish_topic` - 发布文字主题 ✅

```python
# 使用配置文件中的默认星球ID
publish_topic(content="这是我的第一条动态！")

# 指定星球ID
publish_topic(
    content="这是我的第一条动态！",
    group_id="28885518425541"
)
```

#### 2. `publish_topic_from_file` - 从文件发布 ✅

```python
# 从文件读取内容并发布
publish_topic_from_file(
    file_path="/path/to/content.txt",
    group_id="28885518425541"  # 可选
)
```

#### 3. `publish_topic_with_images` - 发布带图片的主题 ✅

```python
# 发布带图片的主题
publish_topic_with_images(
    content="分享几张图片",
    image_paths=[
        "/path/to/image1.jpg",
        "/path/to/image2.png"
    ],
    group_id="28885518425541"  # 可选
)
```

#### 4. `upload_image` - 单独上传图片 ✅

```python
# 上传图片获取image_id（可用于后续发布）
upload_image(image_path="/path/to/image.jpg")
```

#### 5. `get_group_info` - 获取星球信息 ✅

```python
# 查看星球信息
get_group_info(group_id="28885518425541")  # 可选
```

## 在 Claude 中使用示例

与 Claude 对话时，你可以这样说：

```
帮我发布一条动态到知识星球："今天学习了 MCP 的使用方法，非常有趣！"
```

```
把这个文件的内容发布到知识星球：/Users/xxx/article.txt
```

```
帮我发布一条带图片的动态，内容是"分享今天的成果"，图片路径：/Users/xxx/screenshot.png
```

## 项目结构

```
zsxq-mcp/
├── src/
│   └── zsxq_mcp/
│       ├── __init__.py      # 包初始化
│       ├── server.py         # FastMCP 服务器和工具定义
│       ├── client.py         # ZSXQ API 客户端
│       └── config.py         # 配置管理
├── pyproject.toml            # 项目依赖配置
├── .env.example              # 环境变量示例
├── .gitignore               # Git 忽略文件
└── README.md                # 项目文档
```

## 安全提醒

- ⚠️ **请勿分享你的 Cookie**：Cookie 包含你的登录凭证，泄露后他人可以操作你的账号
- 🔒 **`.env` 文件已被 gitignore**：不会被提交到 Git 仓库
- 🔄 **定期更新 Cookie**：Cookie 可能会过期，过期后需要重新获取

## 技术实现

### 图片上传流程

✅ **图片上传已实现！** 通过逆向分析知识星球 Web 端，成功实现了完整的图片上传功能。

**上传流程**：

1. **获取上传令牌**
   ```
   POST https://api.zsxq.com/v2/uploads
   Body: {"req_data": {"type": "image", "size": file_size, "name": "", "hash": ""}}
   Response: {"upload_token": "..."}
   ```

2. **上传到七牛云**
   ```
   POST https://upload-z1.qiniup.com/
   Multipart Form Data:
   - file: 图片文件
   - token: 从步骤1获取的 upload_token
   Response: {"image_id": 123456}
   ```

3. **发布主题**
   ```
   POST https://api.zsxq.com/v2/groups/{group_id}/topics
   Body: {"req_data": {"type": "topic", "text": "...", "image_ids": [123456]}}
   ```

知识星球使用七牛云作为图片存储服务，通过先获取临时上传令牌，再上传到七牛云的方式实现图片上传。

## 故障排除

### Cookie 失效

如果遇到认证错误，通常是 Cookie 过期导致的，请重新获取 Cookie。

### 星球 ID 错误

确保星球 ID 正确，可以通过 `get_group_info` 工具验证。

### .env 文件格式错误

确保 Cookie 值在同一行：
```bash
# 正确格式
ZSXQ_COOKIE=your_very_long_cookie_value_here

# 错误格式（换行）
ZSXQ_COOKIE=
your_cookie_value
```

## 开发

### 运行测试

```bash
pip install -e ".[dev]"
pytest
```

### 调试

直接运行服务器：

```bash
python -m zsxq_mcp.server
```

## 技术栈

- **FastMCP**: MCP 服务器框架
- **httpx**: 异步 HTTP 客户端
- **python-dotenv**: 环境变量管理

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

## 更新日志

### v0.1.0 (2025-01-10)
- ✨ 初始版本
- ✅ 支持发布文字主题
- ✅ 支持上传图片
- ✅ 支持从文件读取内容
- ✅ 灵活的配置方式
