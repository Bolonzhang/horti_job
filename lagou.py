import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
url="https://www.lagou.com/"
driver=webdriver.Chrome()
driver.get(url)

driver.find_element_by_xpath('//*[@id="cboxClose"]').click()
time.sleep(0.3)
driver.find_element_by_xpath('//*[@id="search_input"]').send_keys('园艺',Keys.ENTER)

Cal=1
print('=========================================================')
alist=driver.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li/div[1]/div[1]/div[1]/a/h3')
#//*[@id="s_position_list"]/ul/li[13]/div[1]/div[1]/div[1]
#//*[@id="s_position_list"]/ul/li[14]/div[1]/div[1]/div[1]
num=len(alist)
print('Total',num)
for a in range(num):
    #alist[a].click()
    element=alist[a]
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[-1])
    job_disc1=driver.find_element_by_xpath('/html/body/div[6]/div/div[1]').text
    job_disc2=driver.find_element_by_xpath('//*[@id="container"]/div[1]').text
    print('This is',Cal,'\n')
    Cal+=1
    print(job_disc1,'\n',job_disc2)
    print('=========================================================')
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
#下一页
print("下一页")
print('=========================================================')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="s_position_list"]/div[2]/div/span[5]').click()
time.sleep(4)
alist=driver.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li/div[1]/div[1]/div[1]/a/h3')
num=len(alist)
print('second page',num)
time.sleep(1)
for a in range(num):
    #alist[a].click()
    element=alist[a]
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[-1])
    job_disc1=driver.find_element_by_xpath('/html/body/div[6]/div/div[1]').text
    job_disc2=driver.find_element_by_xpath('//*[@id="container"]/div[1]').text
    print('This is',Cal,'\n')
    Cal += 1
    print(job_disc1,'\n',job_disc2)
    print('=========================================================')
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
#下一页
print("下一页")
print('=========================================================')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="s_position_list"]/div[2]/div/span[5]').click()
time.sleep(4)
alist=driver.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li/div[1]/div[1]/div[1]/a/h3')
num=len(alist)
print('second page',num)
time.sleep(1)
for a in range(num):
    #alist[a].click()
    element=alist[a]
    driver.execute_script("arguments[0].click();",element)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[-1])
    job_disc1=driver.find_element_by_xpath('/html/body/div[6]/div/div[1]').text
    job_disc2=driver.find_element_by_xpath('//*[@id="container"]/div[1]').text
    print('This is',Cal,'\n')
    Cal += 1
    print(job_disc1,'\n',job_disc2)
    print('=========================================================')
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
print('**结束**')
print('=========================================================')
print('一共爬取',Cal,'条招聘信息')
driver.close()
