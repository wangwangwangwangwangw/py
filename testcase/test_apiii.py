'''
#!/usr/bin/python3
# author: Hwei
# 2023Y05M11D
# Email: xxx@qq.com
'''
import json
import logging
import os

import requests
from core.test_Attribute import yfb_mis

def test_mis_api():
    req = requests.get(yfb_mis.url,cookies=yfb_mis.cookie)
    logging.info(req.text)
