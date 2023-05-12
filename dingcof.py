# 获取jenkins构建信息和本次报告地址
import base64
import hashlib
import hmac
import os
import time
import urllib
from pathlib import Path
import requests
import jenkins #安装pip install python-jenkins
import json
import urllib3


# jenkins登录地址
jenkins_url = "http://localhost:8080/"
# 获取jenkins对象
server = jenkins.Jenkins(jenkins_url, username='hongwei', password='199711.14w') #Jenkins登录名 ，密码
# job名称
job_name = "job/test1/" #Jenkins运行任务名称
# job的url地址
job_url = jenkins_url + job_name
# 获取最后一次构建
job_last_build_url = server.get_info(job_name)['lastBuild']['url']
# 报告地址
report_url = job_last_build_url + 'allure' #'allure'为我的Jenkins全局工具配置中allure别名

'''
钉钉推送方法：
读取report文件中"prometheusData.txt"，循环遍历获取需要的值。
使用钉钉机器人的接口，拼接后推送text
'''

def DingTalkSend():
    d = {}
    # 获取项目绝对路径
    # path = os.path.abspath(os.path.dirname((__file__)))
    data_path = Path(__file__).parent / "allure_report/export/prometheusData.txt"
    print(data_path)
    # 打开prometheusData 获取需要发送的信息
    f = open(data_path ,'r')
    for lines in f:
        for c in lines:
            launch_name = lines.strip('\n').split(' ')[0]
            num = lines.strip('\n').split(' ')[1]
            d.update({launch_name: num})
    print(d)
    f.close()
    retries_run = d.get('launch_retries_run')  # 运行总数
    print('运行总数:{}'.format(retries_run))
    status_passed = d.get('launch_status_passed')  # 通过数量
    print('通过数量：{}'.format(status_passed))
    status_failed = d.get('launch_status_failed')  # 不通过数量
    print('失败数量：{}'.format(status_failed))

    # 钉钉推送
    timestamp = str(round(time.time() * 1000))
    secret = 'SECcdd8b5ae26c36fc576c42bd368e6018e3c9692236d2f7b512b407a920e426a2b'
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code =hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    print(sign)
    print(timestamp)
    url = 'https://oapi.dingtalk.com/robot/send?access_token=622ee84c0b11e5a8d77614f543ddcd1b358d5b42eb2fcc87b829d8699f451d76'+'&timestamp='+timestamp+'&sign='+sign# webhook
    print(url)
    con = {"msgtype": "text",
           "text": {
               "content": "Pytest_Allure_Demo自动化脚本执行完成。"
                          "\n测试概述:"
                          "\n运行总数:" + retries_run +
                          "\n通过数量:" + status_passed +
                          "\n失败数量:" + status_failed +
                          "\n构建地址：\n" + job_url +
                          "\n报告地址：\n" + report_url
           }
           }
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    jd = json.dumps(con)
    jd = bytes(jd, 'utf-8')
    headers = {
        'Content-Type': 'application/json',
        "Charset": "utf-8"
    }

    res=requests.post(url, data=jd, headers=headers)
    print(res.text)


if __name__ == '__main__':
    DingTalkSend()