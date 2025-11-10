# 快速开始指南

## ✅ 测试结果

你的 ZSXQ MCP 服务器已经成功配置并测试通过!

- ✅ 依赖安装完成
- ✅ 配置文件已设置
- ✅ 5个工具已注册成功
- ✅ Cookie 和星球 ID 已配置

## 📋 已注册的工具

1. **publish_topic** - 发布文字主题
2. **publish_topic_from_file** - 从文件发布主题
3. **publish_topic_with_images** - 发布带图片的主题
4. **upload_image** - 上传图片
5. **get_group_info** - 获取星球信息

## 🚀 下一步：配置 Claude Desktop

### 1. 找到配置文件位置

**MacOS**:
```bash
open ~/Library/Application\ Support/Claude/
```

编辑 `claude_desktop_config.json`

### 2. 添加 MCP 服务器配置

在配置文件中添加（**重要：需要填入你的 Cookie 和星球 ID**）:

```json
{
  "mcpServers": {
    "zsxq": {
      "command": "python3",
      "args": ["-m", "zsxq_mcp.server"],
      "cwd": "/Users/chenxingyu/Desktop/zsxq-mcp",
      "env": {
        "ZSXQ_COOKIE": "从浏览器复制的完整Cookie值",
        "ZSXQ_GROUP_ID": "你的星球ID"
      }
    }
  }
}
```

**配置说明**：
- `cwd`: 修改为你的实际项目路径
- `env.ZSXQ_COOKIE`: 粘贴从浏览器复制的 Cookie（查看 [CONFIGURATION.md](./CONFIGURATION.md) 了解如何获取）
- `env.ZSXQ_GROUP_ID`: 填入你的星球 ID（可选）

### 3. 重启 Claude Desktop

完全退出 Claude Desktop 并重新打开。

### 4. 验证安装

在 Claude Desktop 中,你应该能看到 ZSXQ 工具可用。可以尝试:

```
帮我查看一下我的知识星球信息
```

或

```
帮我发布一条动态："测试 MCP 工具,一切正常!"
```

## 🧪 本地测试命令

### 测试服务器启动
```bash
cd /Users/chenxingyu/Desktop/zsxq-mcp
python3 -c "from zsxq_mcp.server import mcp; print('Server OK')"
```

### 查看配置
```bash
cat .env
```

## 📝 使用示例

### 示例 1: 发布简单文字
```python
publish_topic(content="这是我的第一条动态!")
```

### 示例 2: 从文件发布
```python
publish_topic_from_file(file_path="/path/to/article.txt")
```

### 示例 3: 发布带图片
```python
publish_topic_with_images(
    content="分享几张图片",
    image_paths=["/path/to/image1.jpg", "/path/to/image2.png"]
)
```

### 示例 4: 查看星球信息
```python
get_group_info()
```

## ⚠️ 注意事项

1. **Cookie 会过期** - 如果遇到认证错误,需要重新获取 Cookie 并更新 `.env` 文件

2. **星球 ID** - 你当前配置的星球 ID: `28888188458521`

3. **图片路径** - 使用绝对路径,确保文件存在

4. **API 端点验证** - 如果遇到 API 错误,可能需要验证实际的知识星球 API 端点

## 🐛 故障排除

### 问题: Cookie 失效
```bash
# 重新获取 Cookie 后更新 .env
nano .env
# 修改 ZSXQ_COOKIE= 的值
```

### 问题: 找不到模块
```bash
cd /Users/chenxingyu/Desktop/zsxq-mcp
python3 -m pip install -e .
```

### 问题: 权限错误
确保 Claude Desktop 配置中使用了正确的 Python 路径:
```bash
which python3
# 输出: /Users/chenxingyu/.pyenv/shims/python3
```

## 📚 更多信息

查看完整文档: [README.md](./README.md)

## 🎉 开始使用

现在你可以在 Claude Desktop 中使用这个工具了!

**试试说**: "帮我发布一条动态到知识星球,内容是:测试 MCP 成功!"
