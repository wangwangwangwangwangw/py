from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome()
# 需要输入的163邮箱的点击和输入的元素属性
url = 'https://mail.163.com/'
driver.get(url)
driver.get_screenshot_as_png()

print(driver.current_url)
driver.maximize_window()
# time.sleep(500)
iframe = driver.find_element(By.XPATH, '//iframe[@frameborder="0"]')  # 定位到新iframe中
driver.switch_to.frame(iframe)
driver.implicitly_wait(10)
#
input_username = driver.find_element(By.XPATH, '//input[@name="email"]').send_keys(1)
sleep(2)
input_password = driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(2)
click = driver.find_element(By.XPATH, '//*[@id="dologin"]').click()
