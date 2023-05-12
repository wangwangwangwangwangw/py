'''
#!/usr/bin/python3
# author: Hwei
# 2023Y05M10D
# Email: xxx@qq.com
'''
import datetime
import logging
import os


import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from core.data import read_esshop
# from testcase.conftest import pytest_runtest_makereport


@pytest.mark.parametrize('username,password,msg',read_esshop('ddt_xinzenghuiyuan.xlsx'),)
def test_login(driver_ecshop,username,password,msg):
	url1 = 'http://115.28.108.130/newecshop/admin/index.php'
	driver_ecshop.get(url1)
	user_ele = driver_ecshop.find_element(By.NAME, 'username')
	password_ele = driver_ecshop.find_element(By.NAME, 'password')
	btn = driver_ecshop.find_element(By.XPATH, "/html/body/div[1]/form/table/tbody/tr/td/table/tbody/tr[4]/td/input")
	user_ele.send_keys(username)
	password_ele.send_keys(password)
	btn.click()
	logging.info('日志')
	#assert (msg==driver_ecshop.current_url or  driver_ecshop.switch_to.alert.text=='- 管理员用户名不能为空!')
	#当msg 不为空 时候 比较msg 否则看出不出现弹窗
	if msg is not None:
		assert msg==driver_ecshop.current_url
	else:
		assert driver_ecshop.switch_to.alert is not None



if __name__ == '__main__':
	os.system("pytest ./testcase/test_esshop.py --alluredir ./allure_result")
	os.system("allure  generate allure_result -o allure_report --clean")
# os.system("allure serve allure_result -o allure_report --clean")

