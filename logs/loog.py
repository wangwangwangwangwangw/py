'''
#!/usr/bin/python3
# author: Hwei
# 2023Y05M08D
# Email: xxx@qq.com
'''
import logging
import os

import logging
from loguru import logger
import logging
from logging.handlers import RotatingFileHandler

# 创建日志记录器
logger = logging.getLogger()
# 设置日志级别
logger.setLevel(logging.DEBUG)
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("/test.log", maxBytes=1024 * 1024 * 100, backupCount=10)
# 创建日志记录的格式
formatter = logging.Formatter('%(levelname)s %(asctime)s %(filename)s:第%(lineno)d行: %(message)s')
# 设置日志记录格式
file_log_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()  # 往屏幕上输出
# 添加日志记录器
logging.getLogger().addHandler(file_log_handler)
logging.getLogger().addHandler(stream_handler)
logging.debug("这条日志是debug级别")
logging.info("这条日志是info级别")
logging.warning("这条日志是warning级别")
logging.error("这条日志是error级别")
logging.critical("这条日志是critical级别")
