'''
#!/usr/bin/python3
# author: Hwei
# 2023年05月06日
# Email: xxx@qq.com
'''
import logging
from time import sleep
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v111 import debugger
from core.test_Attribute import swag, shangzhiyi
from core.data import read_csv, read_excel
from selenium.webdriver.support.wait import WebDriverWait
import logging

# logger.add("file.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {message}")
@pytest.mark.skip#
@pytest.mark.skipif( 1==1 ,reason="debug模式下不执行")

@pytest.mark.parametrize("username,password",read_csv('ddt_test_login.csv'))
def test_login(driver,username,password):
    driver.get(swag.url)
    driver.find_element(By.XPATH,swag.el_username).send_keys(username)
    driver.find_element(By.XPATH,swag.el_password).send_keys(password)
    driver.find_element(By.XPATH, swag.el_btu).click()

@allure.step("The sum of two numbers")
def test_shop(driver_user):
    driver_user.get(shangzhiyi.url)
    driver_user.find_element(By.XPATH,shangzhiyi.el_user).send_keys('test03')
    logging.info(test_shop)
    driver_user.find_element(By.XPATH,shangzhiyi.el_pwd).send_keys('test03')
    driver_user.find_element(By.XPATH,shangzhiyi.el_btu).click()
    driver_user.implicitly_wait(10)
    frame=driver_user.find_element(By.XPATH,shangzhiyi.el_ddframe)
    driver_user.switch_to.frame(frame)
    driver_user.find_element(By.XPATH,shangzhiyi.el_hygl).click()
    driver_user.find_element(By.XPATH,shangzhiyi.el_tjhy).click()
#是
@pytest.mark.parametrize('username,Email,phone,pwdd,pwddd'
    ,read_excel('ddt_xinzenghuiyuan.xlsx'))
def test_add(driver_user,username,pwdd,Email,phone,pwddd):
    logging.info(test_add)
    driver_user.switch_to.parent_frame()
    a=driver_user.find_element(By.XPATH,shangzhiyi.el_frame2)
    driver_user.switch_to.frame(a)
    driver_user.find_element(By.XPATH,shangzhiyi.el_membname).send_keys(username)
    driver_user.find_element(By.XPATH,shangzhiyi.el_email).send_keys(Email)
    driver_user.find_element(By.XPATH,shangzhiyi.el_phone).send_keys(phone)
    driver_user.find_element(By.XPATH,shangzhiyi.el_pwdd).send_keys(pwdd)
    driver_user.find_element(By.XPATH,shangzhiyi.el_pwddd).send_keys(pwddd)

def test_api():
    a=1
    b="2"
    assert a == 1
    assert  b in "123"










