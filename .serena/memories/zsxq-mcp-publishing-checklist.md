# ZSXQ MCP Server 发布检查清单

## 发布前检查清单 ✅

### 项目配置
- [x] 项目结构完整
- [x] pyproject.toml 配置完善（包含完整元数据、依赖、脚本入口）
- [x] README.md 更新（支持多种安装方式）
- [x] LICENSE 文件添加（MIT许可证）
- [x] MANIFEST.in 配置（确保文件正确包含）
- [x] 版本号设置：0.1.0

### 代码质量
- [x] 添加 main() 入口点函数
- [x] 包初始化文件配置
- [x] 依赖版本固定（fastmcp>=0.2.0, httpx>=0.27.0, python-dotenv>=1.0.0）
- [x] Python 兼容性声明（>=3.10）

### 自动化发布
- [x] GitHub Actions 工作流配置（.github/workflows/publish.yml）
- [x] 多版本测试矩阵（Python 3.10-3.13）
- [x] 自动构建和检查流程
- [x] PyPI 发布配置

### 文档完善
- [x] README.md - 项目主页和快速开始
- [x] PACKAGE_INSTALLATION.md - 详细安装指南
- [x] CONFIGURATION.md - 配置说明
- [x] UVX_STARTUP.md - uvx 使用指南
- [x] PUBLISHING_GUIDE.md - 发布操作指南

### 本地测试验证
- [x] 本地构建成功（`uv build`）
- [x] 包文件生成（dist/zsxq_mcp-0.1.0-py3-none-any.whl）
- [x] 本地安装测试通过
- [x] 命令行工具测试通过（`zsxq-mcp --help`）
- [x] uvx 运行测试验证

## 发布操作清单 🚧

### 第一步：GitHub 仓库设置
- [ ] 创建 GitHub 仓库
- [ ] 添加远程仓库地址：`git remote add origin https://github.com/yourusername/zsxq-mcp.git`
- [ ] 推送到 GitHub：`git push -u origin main`

### 第二步：PyPI 配置
- [ ] 创建 PyPI 账户（https://pypi.org/）
- [ ] 生成 API token（Account Settings > API tokens）
- [ ] 配置 GitHub Secret：`PYPI_API_TOKEN`

### 第三步：发布操作
- [ ] 创建版本 tag：`git tag v0.1.0`
- [ ] 推送 tag：`git push origin v0.1.0`
- [ ] 创建 GitHub Release（可选）

### 第四步：发布验证
- [ ] 检查 GitHub Actions 运行状态
- [ ] 验证 PyPI 发布成功
- [ ] 测试 pip 安装：`pip install zsxq-mcp`
- [ ] 测试 uvx 运行：`uvx zsxq-mcp`

## 发布后维护 📋

### 版本管理
- [ ] 更新 CHANGELOG.md
- [ ] 监控下载统计
- [ ] 处理用户反馈和 issues

### 推广和文档
- [ ] 更新项目描述和标签
- [ ] 创建使用示例和教程
- [ ] 收集用户反馈

## 重要提醒

1. **PyPI Token 安全**：仅在 GitHub Secrets 中配置，不要在代码中硬编码
2. **版本控制**：每次发布前更新版本号和更新日志
3. **测试验证**：发布前确保所有测试通过
4. **文档同步**：确保文档与代码版本同步
5. **备份策略**：保留本地备份，以防发布失败

## 紧急回滚方案

如果发布出现问题：
1. 从 PyPI 删除有问题的版本
2. 修复问题并重新发布
3. 通知用户更新版本
4. 分析问题原因并改进流程