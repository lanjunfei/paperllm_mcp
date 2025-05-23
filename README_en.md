# PaperLLM MCP Server

This project provides a local MCP Server that acts as a bridge to the [www.paperllm.com](https://www.paperllm.com) API, exposing MCP tool services via stdio and SSE modes.

## Features

- **API Proxy:** Forwards MCP tool requests to PaperLLM's official API.
- **Multiple Modes:** Supports both stdio and SSE communication modes.
- **Extensible:** Easily add new tools or extend existing ones.
- **NPM Published:** Available on NPM with global installation and npx support.
- **Cross-Platform:** Supports Windows, macOS, and Linux.

### Available Tools

| Tool Name | Description | Parameters |
|-----------|-------------|------------|
| `verify_key` | Verify if API Key is valid | `api_key` (optional) |
| `query_papers` | List user's papers with pagination | `api_key` (optional), `page`, `page_size` |
| `generate_paper` | Generate paper based on title and keywords | `title`, `keywords`, `api_key` (optional) |

---

## Installation

### Method 1: NPM Installation (Recommended)

```bash
# Global installation
npm install -g paperllm_mcp

# Or run directly (no installation needed)
npx paperllm_mcp --sse --port 8001
```

### Method 2: Source Code

```bash
# Clone repository
git clone https://github.com/lanjunfei/paperllm_mcp.git
cd paperllm_mcp

# Install Python dependencies
pip install -r requirements.txt

# Run server
python mcp_server.py --sse --port 8001
```

---

## Project Structure

```
.
├── .venv/                # Python virtual environment
├── mcp_server.py         # Main MCP server script
├── test_api.py           # API endpoint test script
├── index.js              # NPM package entry point
├── test.js               # NPM test script
├── package.json          # NPM package configuration
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

### NPM Method (Recommended)

```bash
# 1. Run directly (recommended)
npx paperllm_mcp --sse --port 8001

# 2. Or install globally then run
npm install -g paperllm_mcp
paperllm_mcp --sse --port 8001

# 3. Test environment
npm test  # Check Python environment and dependencies
```

### Python Source Method

#### 1. Environment Setup

```bash
# Create and activate virtual environment (if not already)
python -m venv .venv
# On Windows
.\.venv\Scripts\activate
# On Linux/Mac
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 2. Configuration

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

#### 3. Run the Server

```bash
# SSE mode
python mcp_server.py --sse --host 0.0.0.0 --port 8001

# stdio mode (default)
python mcp_server.py
```

---

## MCP Client Configuration Examples

### Cursor Configuration

```json
{
  "mcpServers": {
    "paperllm": {
      "command": "npx",
      "args": ["-y", "paperllm_mcp", "--sse", "--port", "8001"],
      "env": {
        "PAPERLLM_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

### CherryStudio Configuration

```json
{
  "name": "paperllm_mcp",
  "type": "sse",
  "description": "MCP server for www.paperllm.com with 3 tools via HTTP/SSE",
  "isActive": true,
  "baseUrl": "http://127.0.0.1:8001/sse"
}
```

### Claude Desktop Configuration

```json
{
  "mcpServers": {
    "paperllm": {
      "command": "paperllm_mcp",
      "args": ["--sse", "--port", "8001"]
    }
  }
}
```

---

## Troubleshooting

### Common Issues

1. **Python not found**
   ```bash
   # Ensure Python is installed and in PATH
   python --version
   ```

2. **Missing dependencies**
   ```bash
   # Install Python dependencies
   pip install -r requirements.txt
   ```

3. **Invalid API Key**
   - Confirm API Key is correctly configured in paperllm.conf
   - Or set via environment variable `PAPERLLM_API_KEY`

4. **Port already in use**
   ```bash
   # Use a different port
   paperllm_mcp --sse --port 8002
   ```

### Debug Mode

```bash
# Enable debug output
paperllm_mcp --sse --port 8001
# Or set environment variable
set DEBUG=true
```

---

## License

This project is for integration with [PaperLLM](https://www.paperllm.com).  
Please refer to the official PaperLLM documentation for API and SDK usage terms.

---

## Related Links

- [NPM Package](https://www.npmjs.com/package/paperllm_mcp)
- [GitHub Repository](https://github.com/lanjunfei/paperllm_mcp)
- [PaperLLM Official Website](https://www.paperllm.com)

For further assistance, please refer to the official PaperLLM documentation or contact technical support. 