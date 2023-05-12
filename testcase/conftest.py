'''
#!/usr/bin/python3
# author: Hwei
# 2023年05月06日
# Email: xxx@qq.com
'''
import logging

import allure
from selenium import webdriver

import os.path
import time
import pytest
from selenium.webdriver.chrome.options import Options

driver = None

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()


    # 以下为实现异常截图的代码：
    # rep.when可选参数有call、setup、teardown，
    # call表示为用例执行环节、setup、teardown为环境初始化和清理环节
    # 这里只针对用例执行且失败的用例进行异常截图
    if rep.when == "call" and rep.failed:
        # 检查driver对象是否包含get_screenshot_as_png方法
        if hasattr(driver, "get_screenshot_as_png"):
            # get_screenshot_as_png实现截图并生成二进制数据
            # allure.attach直接将截图二进制数据附加到allure报告中
            allure.attach(driver.get_screenshot_as_png(), "异常截图", allure.attachment_type.PNG)

@pytest.fixture()
def driver_ecshop():
   global driver #全局变量
   driver=webdriver.Chrome(r'D:\python3.10.0\Scripts\chromedriver.exe')
   yield driver
   driver.quit()





# pytest可以直接获取rootdir路径，他是去寻找pytest.ini文件，找到的位置就默认为根目录
def get_rootdir(request):
    # 根目录
    rootdir = request.config.rootdir
    return rootdir

@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    log_name = 'logs/' + now + '.logs'

    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(os.path.join(get_rootdir(request),log_name))
