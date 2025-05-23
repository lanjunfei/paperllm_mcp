import requests
import json

# 尝试多种可能的API端点格式
#API_BASE_URL = "http://127.0.0.1:8000"
#API_KEY = "6b030150-42de-442e-bf2a-411ff6c5c4dd:50838941ac0196c999eabf91fd73aac9df6b1574b8447e65353b3425fb059e1d"  # 替换为您的API密钥
API_BASE_URL = "https://www.paperllm.com"
API_KEY = "ee77fa74-8d51-4ab4-9099-6fb369f73a73:3a71adfe02c9ead5710c16e7bfb7d1b49f9af9fea65212a16503e2d0751abc78"  # 替换为您的API密钥

headers = {
    "X-API-Key": API_KEY,
    "Content-Type": "application/json"
}

def check_endpoint(url, payload=None, method="POST"):
    """检查API端点是否可访问"""
    try:
        print(f"尝试访问: {url} ({method})")
        if method == "GET":
            response = requests.get(url, headers=headers)
        else:
            response = requests.post(url, headers=headers, json=payload)
            
        print(f"状态码: {response.status_code}")
        print(f"响应头: {dict(response.headers)}")
        
        if response.status_code != 404:
            print("找到可能有效的端点!")
            try:
                response_json = response.json()
                print(f"响应: {json.dumps(response_json, indent=2, ensure_ascii=False)}")
                if 200 <= response.status_code < 300:
                    return True, response
            except json.JSONDecodeError:
                content_type = response.headers.get('Content-Type', '')
                if 'html' in content_type.lower():
                    print(f"响应为HTML内容，可能是网页而非API")
                    print(f"HTML内容片段: {response.text[:200]}...")
                else:
                    print(f"响应内容不是有效的JSON: {response.text[:200]}")
        else:
            print("端点不存在 (404)")
        
        print("-" * 50)
        return False, response
    except requests.exceptions.RequestException as e:
        print(f"请求异常: {e}")
        return False, None

def test_all_possible_endpoints():
    """测试所有真实存在的API端点"""
    possible_endpoints = [
        f"{API_BASE_URL}/api/verify_key",
        f"{API_BASE_URL}/api/query_papers",
        f"{API_BASE_URL}/api/generate_paper",
    ]
    print("扫描所有API端点...")
    for url in possible_endpoints:
        check_endpoint(url)
    # 可选：尝试GET方法访问API根目录（一般无必要）
    # get_endpoints = [f"{API_BASE_URL}/api"]
    # for url in get_endpoints:
    #     check_endpoint(url, method="GET")

def check_website_status():
    """检查网站状态"""
    print("\n检查网站主页状态...")
    check_endpoint(API_BASE_URL, method="GET")

def run_mcp_server_test():
    """测试MCP服务器的可能路径"""
    print("\n测试MCP服务器可能的路径...")
    
    mcp_endpoints = [
        f"{API_BASE_URL}/api/sse",
        f"{API_BASE_URL}/sse",
    ]
    
    for url in mcp_endpoints:
        # 测试SSE连接
        headers_sse = {
            "X-API-Key": API_KEY,
            "Accept": "text/event-stream",
            "Content-Type": "application/json"
        }
        
        try:
            print(f"尝试SSE连接到: {url}")
            response = requests.get(url, headers=headers_sse, stream=True, timeout=5)
            print(f"状态码: {response.status_code}")
            print(f"响应头: {dict(response.headers)}")
            
            if response.status_code != 404:
                print("找到可能的SSE端点!")
                
                # 尝试读取一些SSE数据
                try:
                    for i, line in enumerate(response.iter_lines()):
                        if line:
                            print(f"SSE行 {i}: {line.decode('utf-8')}")
                        if i >= 5:  # 只读取前5行
                            break
                    print("成功读取SSE数据")
                except Exception as e:
                    print(f"读取SSE数据时出错: {e}")
            
            print("-" * 50)
        except requests.exceptions.RequestException as e:
            print(f"SSE连接请求异常: {e}")
            print("-" * 50)

if __name__ == "__main__":
    print("开始API端点检查...\n")
    
    # 首先检查网站状态
    check_website_status()
    
    # 测试所有可能的API端点
    test_all_possible_endpoints()
    
    # 测试MCP服务器
    run_mcp_server_test()
    
    print("\nAPI端点检查完成。")
    
    print("\n总结：")
    print("1. 如果以上测试中没有找到有效的API端点，请确认：")
    print("   - API服务是否已部署并正常运行")
    print("   - API的正确基础URL和路径")
    print("   - 您的API密钥是否有效")
    print("2. 如果网站主页可以访问但API端点不可用，可能是API服务配置问题")
    print("3. 考虑联系网站管理员确认正确的API端点和使用方法")