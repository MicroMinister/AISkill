import requests
import json

# 用你的API密钥替换YOUR_API_KEY
api_key = "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"

# API请求的headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# API的URL
url = "https://api.openai.com/v1/engines/text-davinci-003/completions"

# 发送消息的函数
def send_message(prompt):
    data = {
        "prompt": f"You are ChatGPT, a helpful assistant. User: {prompt}",
        "max_tokens": 50,
        "temperature": 0.8
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response_data = response.json()
        return response_data["choices"][0]["text"]
    else:
        print(f"Error: {response.status_code}")
        return None

# 主程序
if __name__ == "__main__":
    while True:
        user_input = input("你：")
        if user_input.lower() == "退出":
            break
        response = send_message(user_input)
        if response:
            print(f"ChatGPT：{response.strip()}")
