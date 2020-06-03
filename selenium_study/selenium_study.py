# 安装 pip install selenium
# chromedriver

# # 基础操作
# from selenium import webdriver
# driver_path = r'D:\chromedriver_win32\chromedriver.exe'
# # 打开浏览器
# driver = webdriver.Chrome(executable_path=driver_path)
# # 打开网页
# driver.get('https://www.baidu.com')
# print('当前页面title:',driver.title)
# print('当前页面url',driver.current_url)
# print('当前页面源码:',driver.page_source)
# # 关闭当前页面
# driver.close()
# # 关闭整个浏览器
# driver.quit()

# # 查找元素  填充数据  清除数据
# from selenium import webdriver
# import time
# driver_path = r'D:\chromedriver_win32\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('https://www.baidu.com/')
#
# # 定位到百度的搜索输入框  还有n种方法  不一一举例
# SearchInput = driver.find_element_by_id('kw')
# time.sleep(1)
# # 填充数据
# SearchInput.send_keys('selenium')
# time.sleep(1)
# # 清除数据
# SearchInput.clear()

# checkbox   点击事件
# from selenium import webdriver
# import time
# driver_path = r'D:\chromedriver_win32\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('http://xxxxx.cn/login.php')
# # 选中复选框checkbox
# rememberBtn = driver.find_element_by_id('manager_login')
# # 两次取消选中
# rememberBtn.click()
# # 选中提交按钮
# but1 = driver.find_element_by_id('login_bt')
# # 点击按钮
# but1.click()

# 操作select选择框
# selenium专门为select标签提供了一个类selenium.webdriver.support.ui.select
# 将获取到的元素当成参数传到这个类中,创建这个对象,以后就可以使用这个对象进行选择
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# driver_path = r'D:\chromedriver_win32\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('http://www.xxx.com')
# # 选中这个标签,然后使用select创建对象
# selectBtn =driver.find_element_by_id('sel1')
# # 根据索引选择
# selectBtn.select_by_index(1)
# # 根据值选择
# selectBtn.select_by_value("value")
# # 根据可视的文本选择
# selectBtn.select_by_visible_text('content')
# # 取消选中所有项
# selectBtn.deselect_all()

# 行为链
# 有时候在页面上的操作可能分为很多步,那么这时候可以使用鼠标行为链类 ActionChains来完成,比如现在要将鼠标移动到某个元素上并执行点击事件
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import  ActionChains
# driver_path = r'D:\chromedriver_win32\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('https://www.baidu.com/')
# inputTag = driver.find_element_by_id('kw')
# submitBtn = driver.find_element_by_id('su')
# actions = ActionChains(driver)
# # 鼠标移动到元素上
# actions.move_to_element(inputTag)
# actions.send_keys_to_element(inputTag,'python')
# actions.move_to_element(submitBtn)
# actions.click(submitBtn)
# actions.perform()
#
# # click_and_hold(element)  点击但不松开鼠标
# # context_click(element)   右键点击
# # double_click(element)   双击

# 操作Cookie
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# driver_path = r'D:\chromedriver_win32\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('https://www.baidu.com/')
# # 获取所有的cookie:
# for cookie in driver.get_cookies():
#     print(cookie)
# # 根据cookie的key获取value
# value = driver.get_cookie(key)
# # 删除所有的cookie
# driver.delete_all_cookies()
# # 删除某个cookie
# driver.delete_cookie(key)

# 页面等待
# 现在网页越来越多采用Ajax技术,这样程序不能确定何时某个元素完全加载出来了,如果实际页面等待事件过长导致某个dom元素未加载出来,但是代码直接使用了这个webElement,那么就会抛出异常
# 为了解决此问题,Selenium提供两种等待方式:隐式等待,显示等待

# 隐式等待
# 调用driver.implicitly_wait。那么在获取不可用元素之前,会先等待10秒时间
# encoding: utf-8
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# driver_path = r'D:\chromedriver_win32\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('https://www.douban.com/')
# driver.implicitly_wait(10)
# driver.find_element_by_id('asdasdsadf')

# 显式等待
# 显式等待是表明某个条件成立后才执行获取元素的操作,也可以在等待的时候指定一个最大的是看,如果超过这个事件就会抛出一个异常。显示等待应该是用selenium.webdriver.support.excepted_conditions期待的条件和selenium.webdriver.support.ui.WebDriverWait来配合完成

# encoding: utf-8
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# driver_path = r'D:\chromedriver_win32\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('https://www.douban.com/')
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.ID,'fafasfas'))
#
# )

# 一些其他等待条件
# presence_of_element_located 某个元素已经加载完毕了
# presence_of_all_element_located 网页中所有满足条件的元素都加载完毕了
# element_to_be_cliable 某个元素是可以点击了

# 切换页面
# 通常我们在一个浏览器打开多个标签页 在不同的标签页之间切换要用到switch_to.window
# selenium提供了一个叫做switch_to.window来进行切换，具体切换到哪个页面,可以从driver.window_handles中找到
# 未知原因:
# 这里有一个报错 switch_to_window => switch_to.window 即可完成
# encoding: utf-8
# from selenium import webdriver
# driver_path = r'D:\chromedriver_win32\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('https://www.baidu.com/')
# driver.execute_script("window.open('https://www.douban.com/')")
# print(driver.current_url)
# driver.switch_to.window(driver.window_handles[1])
# print(driver.current_url)
# 此时虽然浏览器显示的是第二个页面
# 但是在代码层次他还是在第一个页面上
# print(driver.current_url) 验证

# 设置代理IP
# encoding: utf-8
# from selenium import webdriver
# options = webdriver.ChromeOptions()
# options.add_argument("--proxy-server=http://203.110.164.139:52144")
# driver_path = r'D:\chromedriver_win32\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path,options=options)
# driver.get('http://httpbin.org/ip')

# WebElement元素
# from selenium.webdriver.remote.webelement import WebElement类是每个获取出来的元素的所属类
# 有一些常用的属性
# get_attribute 这个标签的某个属性的值
# screentshot 获取当前页面的截图 这个方法只能在driver上使用
# driver的对象类也是继承自WebElement
# encoding: utf-8
# from selenium import webdriver
# from selenium.webdriver.remote.webelement import WebElement
# import time
# driver_path = r'D:\chromedriver_win32\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('https://www.baidu.com/')
# input1 = driver.find_element_by_id('kw')
# submitBtn = driver.find_element_by_id('su')
# input1.send_keys('python')
# submitBtn.click()
# time.sleep(3)
# driver.save_screenshot('bp.png')
# print(type(submitBtn))
# print(submitBtn.get_attribute("value"))









