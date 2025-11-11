# 🚀 ZSXQ MCP Server 发布指南

## 📋 发布前检查清单

- [x] 项目结构完整
- [x] pyproject.toml 配置完善
- [x] README.md 更新
- [x] LICENSE 文件添加
- [x] MANIFEST.in 配置
- [x] GitHub Actions 工作流配置
- [x] 本地构建测试通过
- [ ] Git 仓库推送到 GitHub
- [ ] 创建 PyPI 账户和 token
- [ ] 配置 GitHub Secrets
- [ ] 创建发布 tag
- [ ] 验证 PyPI 发布

## 🏗️ 已完成的配置

### 1. 项目元数据
```toml
[project]
name = "zsxq-mcp"
version = "0.1.0"
description = "MCP server for publishing content to Zhishixingqiu (知识星球)"
license = {text = "MIT"}
authors = [...]
maintainers = [...]
keywords = [...]
classifiers = [...]
requires-python = ">=3.10"
dependencies = [...]

[project.scripts]
zsxq-mcp = "zsxq_mcp.server:main"
```

### 2. GitHub Actions 自动发布
- ✅ 测试矩阵：Python 3.10-3.13
- ✅ 自动构建和检查
- ✅ PyPI 自动发布（需要配置 token）
- ✅ Release 触发和 Tag 触发

### 3. 文档完善
- ✅ README.md - 多种安装方式
- ✅ PACKAGE_INSTALLATION.md - 详细安装指南
- ✅ CONFIGURATION.md - 配置说明
- ✅ UVX_STARTUP.md - uvx 使用指南

## 📤 发布步骤

### 第一步：推送到 GitHub

```bash
# 添加远程仓库（替换为你的仓库地址）
git remote add origin https://github.com/yourusername/zsxq-mcp.git

# 推送到 GitHub
git push -u origin main
```

### 第二步：创建 PyPI Token

1. 访问 [PyPI](https://pypi.org/)
2. 登录或创建账户
3. 前往 [Account Settings](https://pypi.org/manage/account/)
4. 在 "API tokens" 部分点击 "Add API token"
5. 选择 " Entire account" 范围
6. 复制生成的 token

### 第三步：配置 GitHub Secrets

1. 在你的 GitHub 仓库中，前往 `Settings` > `Secrets and variables` > `Actions`
2. 点击 `New repository secret`
3. 添加以下 secret：
   - **Name**: `PYPI_API_TOKEN`
   - **Value**: 你从 PyPI 复制的 token

### 第四步：创建发布 Tag

```bash
# 创建版本 tag
git tag v0.1.0

# 推送 tag
git push origin v0.1.0
```

### 第五步：创建 GitHub Release（可选）

1. 在 GitHub 仓库页面，点击 "Releases"
2. 点击 "Create a new release"
3. 选择刚推送的 tag (v0.1.0)
4. 添加发布说明
5. 点击 "Publish release"

### 第六步：验证发布

GitHub Actions 会自动：
1. 运行测试套件
2. 构建包
3. 发布到 PyPI

验证发布：
```bash
# 检查 PyPI 页面
pip search zsxq-mcp

# 或直接安装测试
pip install zsxq-mcp
```

## 🔧 手动发布（备用方案）

如果自动发布失败，可以手动发布：

```bash
# 构建包
python -m build

# 上传到 PyPI
python -m twine upload dist/*
```

## 📱 用户使用方式

发布成功后，用户可以通过以下方式使用：

### 1. pip 安装（推荐）
```bash
pip install zsxq-mcp
```

### 2. uvx 运行
```bash
uvx zsxq-mcp
```

### 3. Claude Desktop 配置
```json
{
  "mcpServers": {
    "zsxq": {
      "command": "zsxq-mcp",
      "env": {
        "ZSXQ_COOKIE": "your_cookie_value_here",
        "ZSXQ_GROUP_ID": "your_group_id_here"
      }
    }
  }
}
```

## 🎯 发布后维护

### 版本更新
1. 修改 `pyproject.toml` 中的版本号
2. 更新 `CHANGELOG.md`
3. 创建新的 tag
4. 推送到 GitHub

### 问题处理
- 监控 GitHub Actions 运行状态
- 关注 PyPI 下载统计
- 处理用户反馈和 issues

## 📚 相关资源

- [PyPI 文档](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)
- [GitHub Actions 文档](https://docs.github.com/en/actions)
- [FastMCP 文档](https://gofastmcp.com/)
- [uvx 文档](https://docs.astral.sh/uv/guides/tools/)