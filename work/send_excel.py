import requests
import json
import datetime

current_date = datetime.datetime.now().strftime('%-m.%d')
output_file = f'/Users/zyy/Downloads/合并数据_{current_date}.xlsx'

def get_access_token(corpid, corpsecret):
    url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'
    response = requests.get(url)
    data = response.json()
    return data['access_token']

def upload_file(access_token, file_path):
    upload_url = f'https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={access_token}&type=file'
    with open(file_path, 'rb') as f:
        files = {'media': f}
        response = requests.post(upload_url, files=files)
    data = response.json()
    print(data)  # 添加这行代码以打印响应数据
    return data['media_id']

def send_file(access_token, user, media_id):
    url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
    data = {
        'touser': user,
        'msgtype': 'file',
        'agentid': 1000002,  # 请使用您的应用ID
        'file': {
            'media_id': media_id
        }
    }
    response = requests.post(url, data=json.dumps(data, ensure_ascii=False).encode('utf-8'))
    return response.json()

corpid = 'wwa0fc2c4525c60e5f'
corpsecret = 'SWdT1LrekJprUAxN4xDIwgd8S0jppbVBZuf61uDQma0'
user = 'GaoMengJie'

access_token = get_access_token(corpid, corpsecret)
media_id = upload_file(access_token, output_file)
send_result = send_file(access_token, user, media_id)

print(send_result)
