import requests
import base64

headers = {
    'Referer': 'http://passport2.chaoxing.com/login?fid=23476&role=16&refer=http://i.mooc.chaoxing.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}


def login(username,password):
    PostData = {
        'fid':'-1',
        't':'true',
        'uname':username,
        'password':password,
        'refer':'http://i.chaoxing.com'
    }
    login_url = 'https://passport2.chaoxing.com/fanyalogin'

    response = requests.post(url=login_url,data=PostData)
    return response.json()

if __name__ == '__main__':
    username = input("请输入你的账号:")
    password = input("请输入你的密码:")
    password = str(password).encode('utf-8')
    password = base64.b64encode(password)
    # print(password)
    data = login(username,password)
    print(data['status'])
    if data:
        print(data)
        print('登陆成功!')
    else:
        print('登录失败!')