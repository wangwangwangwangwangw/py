'''
#!/usr/bin/python3
# author: Hwei
# 2023Y05M12D
# Email: xxx@qq.com
'''

import os
import json
from pathlib import Path

from bs4 import BeautifulSoup
data_path=Path(__file__).parent/'allure_report/widgets/index.html'

with open('D:\py\\allure_report\index.html', 'r', encoding='utf-8')as f:
    print(f)