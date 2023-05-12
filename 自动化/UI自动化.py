import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()#控制谷歌的driver
driver.get('https://www.baidu.com')#请求百度网址
el_1=driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys('百度')#输入文字
el_2=driver.find_element(By.XPATH,'//input[@id="kw"]').rect#获取元素的位置的 大小
print(el_2)#获取元素的位置的 大小
el_3=driver.find_element(By.XPATH,'//input[@id="kw"]').get_attribute('value')#获取元素输入框的内容
print(el_3)#获取元素输入框的内同
el_3=driver.find_element(By.XPATH,'//input[@id="kw"]').screenshot('ele.png')#给输入元素截图
# 强制等待
time.sleep(1)
# 隐示等待:只能判断元素是否存在，不能判断元素是否出现，传了一个参数并且大于零时候启用隐士等待 10秒以内定位到元素后结束，但是怎么才能定位到元素自己说了不算
driver.implicitly_wait(10)
# 显示等待:是个方法。允许设置复杂的条件
el5=WebDriverWait(driver,10).until(
    lambda  _: driver.find_element(By.XPATH,'//input[@id="kw"]')
)#lambda匿名函数就是没有方法名，lambda语句中，冒号前是参数，可以有多个，用逗号隔开，冒号右边的返回值

el_2=driver.find_element(By.XPATH,'//input[@id="su"]').click()#点击按钮

time.sleep(3)
driver.quit()

