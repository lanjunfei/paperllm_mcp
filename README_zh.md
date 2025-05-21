# PaperLLM MCP 本地服务端

本项目通过 [www.paperllm.com](https://www.paperllm.com) 官方 API，提供本地 MCP 工具服务，支持 stdio 和 SSE 两种通信模式。

### 功能特点

- **API 代理：** 将 MCP 工具请求转发到 PaperLLM 官方 API。
- **多模式支持：** 支持 stdio 和 SSE 两种通信方式。
- **易扩展：** 可方便地添加或扩展工具。

---

## 项目结构

```
.
├── .venv/                # Python 虚拟环境
├── mcp_server.py         # 主 MCP 服务端脚本
├── test_api.py           # API 测试脚本
├── README_en.md
├── README_zh.md
├── requirements.txt
├── MCP_SERVER_CONFIG.md
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

### 1. 环境准备

```bash
# 创建并激活虚拟环境（如未创建）
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# 安装依赖
pip install -r requirements.txt
# （已省略 MCP SDK 安装说明，直接使用 requirements.txt 安装全部依赖）
```

### 2. 配置

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

### 4. 启动服务

```bash
python mcp_server.py --sse --host 0.0.0.0 --port 8001
```


---

## MCP 客户端配置示例

cherrystudio配置如下：

{
      "name": "paperllm_mcp",
      "type": "sse",
      "description": "www.paperllm.com的mcp server,提供HTTP/SSE下三个工具",
      "isActive": true,
      "baseUrl": "http://127.0.0.1:8001/sse"
    },

## 许可

本项目用于对接 [PaperLLM](https://www.paperllm.com) 官方 API。  
API 及 SDK 使用请遵循官方文档及协议。

---

如需进一步帮助，请参考 PaperLLM 官方文档或联系技术支持。 