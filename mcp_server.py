#!/usr/bin/env python3
"""
PaperLLM ⇄ MCP server  (fastmcp 2.x)

• 默认从 paperllm.conf 读取 api_key / api_base_url
• 支持 stdio（默认）和 --sse/--host/--port
"""

from __future__ import annotations
import argparse, asyncio, configparser, json, os, sys
from pathlib import Path
from typing import Dict, List, Any

import requests
from fastmcp import FastMCP


# ────────────────────────── 读取配置 ────────────────────────── #
def load_conf() -> tuple[str, str]:
    """返回 (API_BASE_URL, DEFAULT_API_KEY)"""
    conf_path = Path(os.getenv("PAPERLLM_CONF", "paperllm.conf")).expanduser().resolve()
    if not conf_path.exists():
        # 找不到配置文件就以空值返回，后面再判错
        return "https://www.paperllm.com/api", ""

    cp = configparser.ConfigParser()
    cp.read(conf_path, encoding="utf-8")

    sec = cp["paperllm"] if "paperllm" in cp else {}
    api_base = sec.get("api_base_url", "https://www.paperllm.com/api").rstrip("/")
    default_key = sec.get("api_key", "").strip()
    return api_base, default_key


API_BASE_URL, DEFAULT_API_KEY = load_conf()
DEBUG = os.getenv("DEBUG", "0") in ("1", "true", "yes")

# ────────────────────────── REST 封装 ───────────────────────── #
class PaperLLM:
    UA = "PaperLLM-MCP/1.0"

    @staticmethod
    def _post(endpoint: str, key: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{API_BASE_URL}/{endpoint}"
        r = requests.post(
            url,
            json=payload,
            headers={"X-API-Key": key, "User-Agent": PaperLLM.UA},
            timeout=120,
        )
        r.raise_for_status()
        return r.json()

    verify   = staticmethod(lambda k:         PaperLLM._post("verify_key",     k, {}))
    papers   = staticmethod(lambda k,p,ps:    PaperLLM._post("query_papers",   k, {"page":p,"page_size":ps}))
    generate = staticmethod(lambda k,t,kw:    PaperLLM._post("generate_paper", k, {"title":t,"keywords":kw}))

# ────────────────────────── MCP server ─────────────────────── #
mcp = FastMCP("PaperLLM-MCP")

def _json(obj: Any) -> str:
    return obj if isinstance(obj, str) else json.dumps(obj, ensure_ascii=False, indent=2)

# ---------- 工具 ----------
@mcp.tool()
def verify_key(api_key: str | None = None) -> str:
    """验证 API Key 是否有效"""
    key = api_key or DEFAULT_API_KEY or _missing()
    return _json(PaperLLM.verify(key))

@mcp.tool()
def query_papers(api_key: str | None = None, page: int = 1, page_size: int = 10) -> str:
    """分页列出论文"""
    key = api_key or DEFAULT_API_KEY or _missing()
    return _json(PaperLLM.papers(key, page, page_size))

from pydantic import Field

@mcp.tool()
def generate_paper(
    title: str    = Field(..., description="论文标题"),
    keywords: str = Field(..., description="关键词，逗号分隔"),
    api_key: str | None = None,
) -> str:
    """根据标题与关键词生成论文"""
    key = api_key or DEFAULT_API_KEY or _missing()
    return _json(PaperLLM.generate(key, title, keywords))

# ---------- 辅助 ----------
def _missing() -> None:  # 统一抛错
    raise ValueError("Missing API Key (配置文件没有 api_key 且调用参数也未提供)")

# ────────────────────────── 启动 ───────────────────────────── #
if __name__ == "__main__":
    if not DEFAULT_API_KEY:
        print("⚠️  [WARN] 配置文件里没找到 api_key；客户端必须显式传入 api_key 参数", file=sys.stderr)

    ap = argparse.ArgumentParser()
    ap.add_argument("--sse", action="store_true", help="使用 SSE 而非 stdio")
    ap.add_argument("--host", default="0.0.0.0")
    ap.add_argument("--port", type=int, default=8001)
    args = ap.parse_args()

    if args.sse:
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        mcp.run()  # 默认 stdio
