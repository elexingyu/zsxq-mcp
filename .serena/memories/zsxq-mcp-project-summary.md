# ZSXQ MCP Server 项目完整记录

## 项目概述
- **项目名称**: zsxq-mcp
- **功能**: 知识星球（Zhishixingqiu）MCP 服务器，支持通过 Model Context Protocol 自动发布内容到知识星球
- **核心功能**: 
  - 发布文字主题
  - 上传和发布图片
  - 从文件读取内容发布
  - 灵活的配置管理
  - Cookie 认证

## 技术栈
- **核心框架**: FastMCP (v2.13.0.2)
- **HTTP 客户端**: httpx (v0.28.1)
- **配置管理**: python-dotenv
- **构建工具**: uv / setuptools
- **Python 版本**: >= 3.10

## 项目结构
```
zsxq-mcp/
├── src/zsxq_mcp/
│   ├── __init__.py         # 包初始化，版本号: 0.1.0
│   ├── server.py          # FastMCP 服务器和工具定义，包含 main() 入口点
│   ├── client.py          # ZSXQ API 客户端
│   ├── config.py          # 配置管理
│   └── __main__.py        # 模块执行入口
├── pyproject.toml         # 完整的包配置，包含元数据和依赖
├── README.md              # 项目文档，支持多种安装方式
├── LICENSE                # MIT 许可证
├── MANIFEST.in            # 包文件包含配置
├── start_with_uvx.sh      # uvx 启动脚本
├── .github/workflows/publish.yml  # GitHub Actions 自动发布
├── PACKAGE_INSTALLATION.md  # 详细安装指南
├── PUBLISHING_GUIDE.md    # 发布操作指南
├── CONFIGURATION.md       # 配置说明
├── UVX_STARTUP.md         # uvx 使用指南
└── dist/                  # 构建输出目录
```

## 关键配置信息

### pyproject.toml 核心配置
```toml
[project]
name = "zsxq-mcp"
version = "0.1.0"
description = "MCP server for publishing content to Zhishixingqiu (知识星球)"
license = {text = "MIT"}
requires-python = ">=3.10"
dependencies = [
    "fastmcp>=0.2.0",
    "httpx>=0.27.0", 
    "python-dotenv>=1.0.0",
]

[project.scripts]
zsxq-mcp = "zsxq_mcp.server:main"
```

### 环境变量配置
```env
ZSXQ_COOKIE=your_complete_cookie_value_here
ZSXQ_GROUP_ID=your_group_id_here
```

## 安装和使用方式

### 1. pip 安装（推荐）- 发布后可用
```bash
pip install zsxq-mcp
zsxq-mcp
```

### 2. uvx 临时运行 - 发布后可用
```bash
uvx zsxq-mcp
```

### 3. 本地 uvx 启动
```bash
cd zsxq-mcp
uvx --from . python -m zsxq_mcp.server
# 或使用脚本
./start_with_uvx.sh
```

### 4. Claude Desktop 配置
```json
{
  "mcpServers": {
    "zsxq": {
      "command": "zsxq-mcp",
      "env": {
        "ZSXQ_COOKIE": "your_cookie_value_here",
        "ZSXQ_GROUP_ID": "28885518425541"
      }
    }
  }
}
```

## 发布配置

### GitHub Actions 自动发布
- 触发条件: Tag push (v*) 和 Release 发布
- 测试矩阵: Python 3.10, 3.11, 3.12, 3.13
- 自动构建包并发布到 PyPI
- 需要配置 GitHub Secret: `PYPI_API_TOKEN`

### 发布步骤
1. 推送到 GitHub: `git push origin main`
2. 创建 tag: `git tag v0.1.0 && git push origin v0.1.0`
3. 创建 GitHub Release (可选)
4. 自动发布到 PyPI

## 可用工具

### MCP 工具集
- `publish_topic(content, group_id, cookie)` - 发布文字主题
- `publish_topic_from_file(file_path, group_id, cookie)` - 从文件发布
- `publish_topic_with_images(content, image_paths, group_id, cookie)` - 发布带图片主题
- `upload_image(image_path, cookie)` - 上传图片
- `get_group_info(group_id, cookie)` - 获取星球信息

## 技术实现要点

### 图片上传流程
1. 获取上传令牌: `POST https://api.zsxq.com/v2/uploads`
2. 上传到七牛云: `POST https://upload-z1.qiniup.com/`
3. 发布主题: `POST https://api.zsxq.com/v2/groups/{group_id}/topics`

### 配置管理
- 支持环境变量配置
- 支持 .env 文件配置
- 支持运行时参数覆盖

## 构建和测试验证

### 本地构建
```bash
uv build  # 生成 dist/zsxq_mcp-0.1.0-py3-none-any.whl
```

### 本地测试
```bash
uv venv test-env
source test-env/bin/activate
uv pip install dist/zsxq_mcp-0.1.0-py3-none-any.whl
zsxq-mcp --help  # 验证安装成功
```

## 文档结构
- **README.md**: 项目主页，快速开始
- **PACKAGE_INSTALLATION.md**: 详细安装指南
- **CONFIGURATION.md**: 完整配置说明
- **UVX_STARTUP.md**: uvx 使用指南
- **PUBLISHING_GUIDE.md**: 发布操作指南
- **QUICKSTART.md**: 快速开始指南
- **TEST_RESULTS.md**: 测试结果记录

## 版本信息
- 当前版本: 0.1.0
- Python 兼容性: 3.10-3.13
- 许可证: MIT
- 状态: 发布就绪

## 注意事项
- Cookie 值包含登录凭证，需要安全保管
- .env 文件已添加到 .gitignore，不会提交到仓库
- 图片上传功能已完全实现并测试通过
- 支持 uvx 零安装启动
- GitHub Actions 配置完成，支持自动发布

## 重要文件位置
- 服务器入口: `src/zsxq_mcp/server.py`
- 包配置: `pyproject.toml`
- 启动脚本: `start_with_uvx.sh`
- 发布工作流: `.github/workflows/publish.yml`
- 安装指南: `PACKAGE_INSTALLATION.md`
- 发布指南: `PUBLISHING_GUIDE.md`