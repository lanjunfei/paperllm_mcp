#!/usr/bin/env node

const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

console.log('🧪 [PaperLLM-MCP] Running tests...\n');

// 测试1: 检查 Python 是否可用
function testPython() {
  return new Promise((resolve, reject) => {
    console.log('1️⃣  Checking Python installation...');
    const python = spawn('python', ['--version'], { stdio: 'pipe' });
    
    python.on('close', (code) => {
      if (code === 0) {
        console.log('✅ Python is available\n');
        resolve();
      } else {
        console.log('❌ Python not found in PATH\n');
        reject(new Error('Python not available'));
      }
    });
    
    python.on('error', () => {
      console.log('❌ Python not found in PATH\n');
      reject(new Error('Python not available'));
    });
  });
}

// 测试2: 检查必要文件
function testFiles() {
  console.log('2️⃣  Checking required files...');
  const requiredFiles = ['mcp_server.py', 'requirements.txt', 'paperllm.conf'];
  
  for (const file of requiredFiles) {
    if (fs.existsSync(file)) {
      console.log(`✅ ${file} exists`);
    } else {
      console.log(`❌ ${file} missing`);
      throw new Error(`Missing required file: ${file}`);
    }
  }
  console.log('');
}

// 测试3: 检查 Python 依赖
function testPythonDeps() {
  return new Promise((resolve, reject) => {
    console.log('3️⃣  Checking Python dependencies...');
    const python = spawn('python', ['-c', 'import requests, fastmcp; print("Dependencies OK")'], { stdio: 'pipe' });
    
    let output = '';
    python.stdout.on('data', (data) => {
      output += data.toString();
    });
    
    python.on('close', (code) => {
      if (code === 0 && output.includes('Dependencies OK')) {
        console.log('✅ Python dependencies are installed\n');
        resolve();
      } else {
        console.log('❌ Python dependencies missing');
        console.log('💡 Run: pip install -r requirements.txt\n');
        reject(new Error('Python dependencies not installed'));
      }
    });
  });
}

// 运行所有测试
async function runTests() {
  try {
    testFiles();
    await testPython();
    await testPythonDeps();
    
    console.log('🎉 All tests passed!');
    console.log('🚀 You can now run: npm start');
    process.exit(0);
  } catch (error) {
    console.log(`\n💥 Test failed: ${error.message}`);
    process.exit(1);
  }
}

runTests(); 