# encoding: utf-8
from selenium import webdriver
from lxml import etree
import re
import time
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LagouSpider(object):
    driver_path = r'D:\chromedriver_win32\chromedriver.exe'

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self.positions = []

    def run(self):
        time.sleep(10)
        self.driver.get(self.url)
        while True:
            # 获取当前页面源码
            source = self.driver.page_source
            # 等待下一页元素加载成功再继续执行
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='pager_container']/span[last()]"))
            )
            self.parse_list_page(source)
            try:
                next_btn = self.driver.find_element_by_xpath("//div[@class='pager_container']/span[last()]")
                # 如果 pager_next_disable存在下一页按钮class属性中代表是最后一页
                if "pager_next_disabled" in next_btn.get_attribute("class"):
                    break
                else:
                    next_btn.click()
            except:
                print(source)
            time.sleep(2)
    # 解析第一页 获取所有职位详情页链接
    def parse_list_page(self, source):
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            self.request_detail_page(link)
            time.sleep(1)

    def request_detail_page(self, url):
        # 打开新的标签页
        self.driver.execute_script("window.open('%s')"%url)
        # 切换页面指向新的页面
        self.driver.switch_to.window(self.driver.window_handles[1])
        # 等待改元素加载完毕
        WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//h4[@class='company']"))
        )
        source = self.driver.page_source
        self.parse_detail_page(source)
        # 关闭当前详情页
        self.driver.close()
        # 切换为职位列表页
        self.driver.switch_to.window(self.driver.window_handles[0])
    # 取出详情页面的数据
    def parse_detail_page(self, source):
        html = etree.HTML(source)
        position_name = html.xpath("//h4[@class='company']/text()")[0]
        job_request_spans = html.xpath("//dd[@class='job_request']//span")
        salary_span = job_request_spans[0]
        salary = salary_span.xpath('.//text()')[0].strip()
        city = job_request_spans[1].xpath(".//text()")[0].strip()
        city = re.sub(r"[\s/]]", "", city)
        work_years = job_request_spans[2].xpath(".//text()")[0].strip()
        work_years = re.sub(r"[\s/]]", "", work_years)
        education = job_request_spans[3].xpath(".//text()")[0].strip()
        education = re.sub(r"[\s/]]", "", education)
        # desc = "".join(html.xpath("//dd[@class='job_bt']/text()")).strip()
        desc = "".join(html.xpath("//div[@class='job-detail']//text()")).strip()
        position = {
            'name': position_name,
            'salary': salary,
            'city': city,
            'work_years': work_years,
            'education': education,
            'desc': desc
        }
        self.positions.append(position)
        print(position)
        print("=" * 40)


if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()








