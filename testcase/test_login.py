# from time import sleep
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from core.test_Attribute import LoginPage
#
# @pytest.fixture(scope='module')
# def driver():
#     driver=webdriver.Chrome()
#     driver.implicitly_wait(10)
#     yield #yield上面的代码是测试用例之前执行 下面的代码是 测试用例执行之后执行
#     driver.quit()
#     yield driver
# def test_login(driver):
#
#     driver.get(LoginPage.url)
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     ifm=driver.find_element(By.XPATH,LoginPage.iframe)
#     driver.switch_to.frame(ifm)
#     driver.find_element(By.XPATH,LoginPage.input_username).send_keys('w15632325857')
#     driver.find_element(By.XPATH,LoginPage.input_password).send_keys('199711.14w')
#     driver.find_element(By.XPATH,LoginPage.click).click()
#     '''sleep(3)
#     driver.implicitly_wait(10)
#     ifm=driver.find_element(By.XPATH,'//iframe[@id="ifrmHis1683342853868"]')#进入iframe
#     driver.switch_to.frame(ifm)
#     WebDriverWait(driver,10).until(
#         lambda _: driver.find_element(By.XPATH,'//span[@class="nui-tips-text"]')
#
#     )#lambda匿名函数就是没有方法名，lambda语句中，冒号前是参数，可以有多个，用逗号隔开，冒号右边的返回值
#     assert '登录成功' #添加断言'''
