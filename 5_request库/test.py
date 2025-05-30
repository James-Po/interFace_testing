import requests
import pytest
# 假设这是你的登录API地址
login_url = "https://service-his-test.dahuangf.com/his-user/login/doLogin"

# 用户登录所需的信息
payload = {
    'loginName': '杨江坡',
    'password': 'yjp123456',
    'verificationCode': '12345'
}

# 发送登录请求
response = requests.post(login_url, json=payload)

# 检查请求是否成功
if response.status_code == 200:
    # 假设token位于响应的json中的 'token' 字段
    token = response.json().get('token')
    print(f"获取的token是: {token}")
    print(token)

    # 接下来你可以用这个token进行其他需要授权的请求
    headers = {'Authorization': f'Bearer {token}'}
    # 示例：访问受保护的资源
    protected_resource_url = "https://example.com/api/protected-resource"
    resource_response = requests.get(protected_resource_url, headers=headers)
    print(resource_response.text)
else:
    print("无法登录，状态码:", response.status_code)