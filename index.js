#!/usr/bin/env node

const { spawn } = require('child_process');
const path = require('path');

// 获取当前包的目录
const packageDir = __dirname;
const pythonScript = path.join(packageDir, 'mcp_server.py');

// 获取命令行参数（跳过 node 和脚本名）
const args = process.argv.slice(2);

console.log('[PaperLLM-MCP] Starting Python MCP server...');

// 启动 Python 脚本
const python = spawn('python', [pythonScript, ...args], {
  stdio: 'inherit',
  cwd: packageDir
});

python.on('error', (err) => {
  console.error('[PaperLLM-MCP] Error starting Python server:', err.message);
  console.error('Make sure Python is installed and available in PATH');
  process.exit(1);
});

python.on('close', (code) => {
  console.log(`[PaperLLM-MCP] Python server exited with code ${code}`);
  process.exit(code);
});

// 处理进程退出信号
process.on('SIGINT', () => {
  console.log('\n[PaperLLM-MCP] Shutting down...');
  python.kill('SIGINT');
});

process.on('SIGTERM', () => {
  python.kill('SIGTERM');
}); 