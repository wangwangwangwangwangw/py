import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from core.test_Attribute import Test_qqkongjian

def test_login(driver):
    driver.get(Test_qqkongjian.url)
    ifm=driver.find_element(By.XPATH,Test_qqkongjian.iframe)
    driver.delete_all_cookies()
    driver.switch_to.frame(ifm)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,Test_qqkongjian.mimadenglu).click()
    WebDriverWait(driver,10).until(
        lambda _: driver.find_element(By.XPATH,'//input[@class="inputstyle"]')
    )
    driver.find_element(By.XPATH,Test_qqkongjian.zhanghao).send_keys('930320012')
    driver.find_element(By.XPATH,Test_qqkongjian.mima).send_keys('199711.14')
    driver.find_element(By.XPATH,Test_qqkongjian.login).click()
    time.sleep(5)






