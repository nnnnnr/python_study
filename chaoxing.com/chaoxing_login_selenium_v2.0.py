# 在原先基础上改进了验证码识别 使用尖叫数据接口进行识别
# encoding: utf-8
from selenium import webdriver
import time
from PIL import Image
import base64
import requests

driver_path = r'D:\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.maximize_window()
driver.get('http://passport2.chaoxing.com/login')

def GetCode():
    url = 'http://apigateway.jianjiaoshuju.com/api/v_1/yzm.html'
    with open('VerCode.png','rb') as fp:
        data = fp.read()
        pic = base64.b64encode(data)
    pic = pic
    PostData = {
        'v_type':'n4',
        'v_pic':pic
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'AppKey': '',
        'AppSecret': '',
        'AppCode': ''
    }
    response = requests.post(url = url,data = PostData,headers = headers)
    result = response.json()
    code = result['v_code']
    return code




def GetCodeImage():
    # 这块用其他方法定位截图一直行不通 只能一步一步这样调试了
    driver.save_screenshot('code.png')
    code = driver.find_element_by_id('numVerCode')
    left = code.location['x'] + code.size['width'] +50
    top = code.location['y'] + code.size['height'] +50
    right = left + 130
    bottom = top + 40
    image = Image.open('code.png')
    image = image.crop((left,top,right,bottom))
    image.save('VerCode.png')
    # image.show('VerCode.png')
    img_code = GetCode()
    return img_code

def login(username,password):
    username = username
    password = password
    code_input = driver.find_element_by_id('numcode')
    code = GetCodeImage()
    code = code
    # print(code)
    code_input.send_keys(code)
    time.sleep(1)
    username_input = driver.find_element_by_id('unameId')
    username_input.send_keys(username)
    time.sleep(1)
    password_input = driver.find_element_by_class_name('zl_input2')
    password_input.send_keys(password)
    time.sleep(1)
    login_button = driver.find_element_by_class_name('zl_btn_right')
    login_button.click()
    return driver.current_url

if __name__ == '__main__':
    # data = login()
    username = input("请输入用户名:")
    password = input("请输入密码:")
    index_url = login(username,password)
    print(index_url)
    # http://i.mooc.chaoxing.com/space/index?t=1590658121199
    if 'http://i.mooc.chaoxing.com/space/index' in index_url:
        print('登陆成功!')
    else:
        print('登录失败!')
