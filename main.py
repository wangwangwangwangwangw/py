
import os
import pytest

# split ='allure '+'generate '+'./report/result '+'-o '+'./report/html '+'--clean'

#os.system("allure serve reports  allure_results")
if __name__ == '__main__':


    os.system("pytest ./testcase/test_esshop.py --alluredir ./allure_result")
    os.system("allure  generate allure_result -o allure_report --clean")
    #os.system("allure serve allure_result -o allure_report --clean")