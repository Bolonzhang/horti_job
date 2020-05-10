from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,csv

class lgSpider(object):
    #设置
    def __init__(self):
        self.url="https://www.lagou.com/"
        #self.page=0
        self.Cal = 0
        self.browser=webdriver.Chrome()
    #打开页面
    def get_page(self):
        self.browser.get(self.url)
        self.browser.find_element_by_xpath('//*[@id="cboxClose"]').click()
        time.sleep(0.5)
        self.browser.find_element_by_xpath('//*[@id="search_input"]').send_keys('园艺',Keys.ENTER)
        time.sleep(1)
    #准备csv文件，写入标题栏
    def pre_csv(self):
        with open('lagou_jobs.csv','w',encoding='utf-8') as file:
            writer=csv.writer(file)
            header=['公司','职位','工资','位置','经验要求','学历要求','职位诱惑','职位描述']
            writer.writerow(header)
    #提取页面信息
    def parse_page(self):
        self.lists = self.browser.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li/div[1]/div[1]/div[1]/a/h3')
        self.num = len(self.lists)
        for list in self.lists:
            self.Cal+=1
            print('已爬取',self.Cal,'条招聘信息')
            self.browser.execute_script('arguments[0].click();',list)
            time.sleep(1)
            self.browser.switch_to.window(self.browser.window_handles[-1])
            #开始到网页内提取文字内容了
            a=self.browser.find_element_by_xpath('/html/body/div[6]/div/div[1]/div/h4').text[:-2]
            b=self.browser.find_element_by_xpath('/html/body/div[6]/div/div[1]/div/h1').text
            c=self.browser.find_element_by_xpath('/html/body/div[6]/div/div[1]/dd/h3/span[1]').text
            d=self.browser.find_element_by_xpath('/html/body/div[6]/div/div[1]/dd/h3/span[2]').text[1:3]
            e=self.browser.find_element_by_xpath('/html/body/div[6]/div/div[1]/dd/h3/span[3]').text[:-2]
            f=self.browser.find_element_by_xpath('/html/body/div[6]/div/div[1]/dd/h3/span[4]').text[:-2]
            g=self.browser.find_element_by_xpath('//*[@id="job_detail"]/dd[1]').text[5:]
            h=self.browser.find_element_by_xpath('//*[@id="job_detail"]/dd[2]').text[5:]
            job_disc=[a,b,c,d,e,f,g,h]
            with open('lagou_jobs.csv', 'a', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(job_disc)
            self.browser.close()
            self.browser.switch_to.window(self.browser.window_handles[0])
            time.sleep(1)

    def main(self):
        self.get_page()
        self.pre_csv()
        self.parse_page()
        while True:
            try:
                self.browser.find_element_by_xpath('//*[@id="s_position_list"]/div[2]/div/span[5]').click()
                time.sleep(2)
                self.parse_page()
            except Exception as wrong:
                self.browser.quit()
                break
        self.browser.close()

if __name__=='__main__':
    spider=lgSpider()
    spider.main()
