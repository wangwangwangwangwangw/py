
import os
import pytest

# split ='allure '+'generate '+'./report/result '+'-o '+'./report/html '+'--clean'

#os.system("allure serve reports  allure_results")
if __name__ == '__main__':
    os.system("pytest ./testcase/test_apiii.py --alluredir ./allure_result")
