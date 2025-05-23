# PaperLLM MCP 本地服务端

本项目通过 [www.paperllm.com](https://www.paperllm.com) 官方 API，提供本地 MCP 工具服务，支持 stdio 和 SSE 两种通信模式。

### 功能特点

- **API 代理：** 将 MCP 工具请求转发到 PaperLLM 官方 API。
- **多模式支持：** 支持 stdio 和 SSE 两种通信方式。
- **易扩展：** 可方便地添加或扩展工具。
- **NPM 发布：** 已发布到 NPM，支持全局安装和 npx 直接运行。
- **跨平台：** 支持 Windows、macOS、Linux。

### 可用工具

| 工具名称 | 功能描述 | 参数 |
|---------|---------|------|
| `verify_key` | 验证 API Key 是否有效 | `api_key`（可选） |
| `query_papers` | 分页列出用户的论文 | `api_key`（可选）、`page`、`page_size` |
| `generate_paper` | 根据标题和关键词生成论文 | `title`、`keywords`、`api_key`（可选） |

---

## 安装方式

### 方式一：NPM 安装（推荐）

```bash
# 全局安装
npm install -g @lanjunfei/paperllm_mcp

# 或直接运行（无需安装）
npx @lanjunfei/paperllm_mcp --sse --port 8001
```

### 方式二：源码运行

```bash
# 克隆仓库
git clone https://github.com/lanjunfei/paperllm_mcp.git
cd paperllm_mcp

# 安装 Python 依赖
pip install -r requirements.txt

# 运行服务
python mcp_server.py --sse --port 8001
```

---

## 项目结构

```
.
├── .venv/                # Python 虚拟环境
├── mcp_server.py         # 主 MCP 服务端脚本
├── test_api.py           # API 测试脚本
├── index.js              # NPM 包入口文件
├── test.js               # NPM 测试脚本
├── package.json          # NPM 包配置
├── README_en.md
├── README_zh.md
├── requirements.txt
└── paperllm.conf         # PaperLLM MCP 服务端主配置文件
```

---

## paperllm.conf

`paperllm.conf` 是 PaperLLM MCP 服务端的主配置文件。可用于存放 API Key、服务端设置或其他自定义配置。

**示例内容：**

```ini
[paperllm]
api_key = 你的-paperllm-api-key
api_base_url = https://www.paperllm.com/api
server_port = 8001
debug = false
```

---

## 快速开始

### NPM 方式（推荐）

```bash
# 1. 直接运行（推荐）
npx @lanjunfei/paperllm_mcp --sse --port 8001

# 2. 或全局安装后运行
npm install -g @lanjunfei/paperllm_mcp
@lanjunfei/paperllm_mcp --sse --port 8001

# 3. 测试环境
npm test  # 检查 Python 环境和依赖
```

### Python 源码方式

#### 1. 环境准备

```bash
# 创建并激活虚拟环境（如未创建）
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

#### 2. 配置

可通过环境变量进行配置：

| 变量名         | 说明                         | 默认值                      |
|----------------|------------------------------|-----------------------------|
| `API_BASE_URL` | PaperLLM API 基础地址        | https://www.paperllm.com/api|
| `SERVER_PORT`  | SSE 模式监听端口             | 8001                        |
| `DEBUG`        | 是否开启调试输出             | false                       |

示例：
```bash
set API_BASE_URL=https://www.paperllm.com/api
set SERVER_PORT=8001
set DEBUG=true
```

#### 3. 启动服务

```bash
# SSE 模式
python mcp_server.py --sse --host 0.0.0.0 --port 8001

# stdio 模式（默认）
python mcp_server.py
```

---

## MCP 客户端配置示例

### Cursor 配置（windows系统）

```json
{
  "command": "C:\\Windows\\System32\\cmd.exe",
  "args": [
    "/c", 
    "npx", 
    "-y", 
    "@lanjunfei/paperllm_mcp"
  ]
}
```

### CherryStudio 配置（需要本地运行python mcp_server.py --sse --host 0.0.0.0 --port 8001）

```json
{
  "name": "paperllm_mcp",
  "type": "sse",
  "description": "www.paperllm.com的mcp server,提供HTTP/SSE下三个工具",
  "isActive": true,
  "baseUrl": "http://127.0.0.1:8001/sse"
}
```

### Claude Desktop 配置

```json
{
  "mcpServers": {
    "paperllm": {
      "command": "@lanjunfei/paperllm_mcp",
      "args": ["--sse", "--port", "8001"]
    }
  }
}
```

---

## 故障排除

### 常见问题

1. **Python 未找到**
   ```bash
   # 确保 Python 已安装并在 PATH 中
   python --version
   ```

2. **依赖缺失**
   ```bash
   # 安装 Python 依赖
   pip install -r requirements.txt
   ```

3. **API Key 无效**
   - 确认 API Key 在 paperllm.conf 中正确配置
   - 或通过环境变量 `PAPERLLM_API_KEY` 设置

4. **端口被占用**
   ```bash
   # 使用其他端口
   @lanjunfei/paperllm_mcp --sse --port 8002
   ```

### 调试模式

```bash
# 开启调试输出
@lanjunfei/paperllm_mcp --sse --port 8001
# 或设置环境变量
set DEBUG=true
```

---

## 许可

本项目用于对接 [PaperLLM](https://www.paperllm.com) 官方 API。  
API 及 SDK 使用请遵循官方文档及协议。

---

## 相关链接

- [NPM 包页面](https://www.npmjs.com/package/@lanjunfei/paperllm_mcp)
- [GitHub 仓库](https://github.com/lanjunfei/paperllm_mcp)
- [PaperLLM 官网](https://www.paperllm.com)

如需进一步帮助，请参考 PaperLLM 官方文档或联系技术支持。 