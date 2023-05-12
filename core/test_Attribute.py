import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait






class Test_qqkongjian():
    url ='https://i.qq.com/'
    iframe='//iframe[@id="login_frame"]'
    mimadenglu='//a[@id="switcher_plogin"]'
    zhanghao='//input[@class="inputstyle"]'
    mima ='//input[@class="inputstyle password"]'
    login ='//a[@class="login_button"]'

class swag():
    url='https://www.saucedemo.com'
    el_username='//input[@id="user-name"]'
    el_password='//input[@id="password"]'
    el_btu='//input[@type="submit"]'

class shangzhiyi():
    url = 'http://115.28.108.130/newecshop/admin/index.php'
    el_user= '//input[@name="username"]'
    el_pwd = '//input[@name="password"]'
    el_btu = '//input[@class="button2"]'
    el_phone = '//a[@onclick="clear_cache_mobile()"]'
    el_ddframe= '//frame[@id="menu-frame"]'
    # el_ddgl = '//em[@id="h1_04_order"]'
    # el_hbdd ='//*[@id="04_order"]/ul/li[4]/a'
    el_hygl = '//em[@id="h1_08_members"]'
    el_tjhy ='//*[@id="08_members"]/ul/li[2]/a'
    el_frame2='//*[@id="main-frame"]'
    el_membname= '/html/body/div[2]/form/table/tbody/tr[1]/td[2]/input'
    el_email = '/html/body/div[2]/form/table/tbody/tr[1]/td[2]/input'
    el_phone = '//*[@id="mobile_phone"]'
    el_pwdd ='//*[@id="mobile_phone"]'
    el_pwddd = '/html/body/div[2]/form/table/tbody/tr[5]/td[2]/input'

class yfb_mis():
    url = 'http://mis.yfb.qianlima.com/a/sys/menu/jsonTree'
    cookie = {'Cookie':'yfbsite.session.id=db711a48f62d4cfd9e8704998f92091e; tabmode=1; Hm_lvt_82116c626a8d504a5c0675073362ef6f=1683783868,1683822453,1683830737,1683879746; Hm_lpvt_82116c626a8d504a5c0675073362ef6f=1683879746; JSESSIONID=DEE62AD85E259DB56A80B1A28042AF4D'}
    user = 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36X-Requested-With: XMLHttpRequest'