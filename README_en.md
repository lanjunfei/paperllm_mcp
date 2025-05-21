# PaperLLM MCP Server

This project provides a local MCP Server that acts as a bridge to the [www.paperllm.com](https://www.paperllm.com) API, exposing MCP tool services via stdio and SSE modes.

## Features

- **API Proxy:** Forwards MCP tool requests to PaperLLM's official API.
- **Multiple Modes:** Supports both stdio and SSE communication modes.
- **Extensible:** Easily add new tools or extend existing ones.

---

## Project Structure

```
.
├── .venv/                # Python virtual environment
├── mcp_server.py         # Main MCP server script
├── test_api.py           # API endpoint test script
├── README_en.md
├── README_zh.md
├── requirements.txt
├── MCP_SERVER_CONFIG.md
└── paperllm.conf         # Main configuration file for PaperLLM MCP server
```

---

## paperllm.conf

`paperllm.conf` is the main configuration file for the PaperLLM MCP server. You can use it to store API keys, server settings, or other custom configurations required by your MCP server.

**Example:**

```ini
[paperllm]
api_key = your-paperllm-api-key
api_base_url = https://www.paperllm.com/api
server_port = 8001
debug = false
```

---

## Quick Start

### 1. Environment Setup

```bash
# Create and activate virtual environment (if not already)
python -m venv .venv
# On Windows
.\.venv\Scripts\activate
# On Linux/Mac
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
# (You must also install the correct MCP SDK, see below)
```

### 2. Configuration

You can configure the server via environment variables:

| Variable         | Description                                 | Default                      |
|------------------|---------------------------------------------|------------------------------|
| `API_BASE_URL`   | PaperLLM API base URL                       | https://www.paperllm.com/api |
| `SERVER_PORT`    | Port for SSE mode                           | 8001                         |
| `DEBUG`          | Enable debug output (`1`/`true`/`yes`)      | false                        |

Example:
```bash
set API_BASE_URL=https://www.paperllm.com/api
set SERVER_PORT=8001
set DEBUG=true
```

### 3. Run the Server

```bash
python mcp_server.py --sse --host 0.0.0.0 --port 8001
```

- The server will try to start  SSE mode.

---

## MCP Server Configuration (for MCP Client)

cherrystudio use the following configuration:

```json
{
      "name": "paperllm_mcp",
      "type": "sse",
      "description": "www.paperllm.com的mcp server,提供HTTP/SSE下三个工具",
      "isActive": true,
      "baseUrl": "http://127.0.0.1:8001/sse"
    },
```
- For stdio mode, the client should launch the server as a subprocess and communicate via stdin/stdout.
- For SSE mode, connect to the specified `server_url`.

---

## License

This project is for integration with [PaperLLM](https://www.paperllm.com).  
Please refer to the official PaperLLM documentation for API and SDK usage terms. 