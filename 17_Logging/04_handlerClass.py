# coding=utf-8
import logging
import logging.handlers
import time
logger = logging.getLogger("myLogger")  # 通过logging创建logger日志器
logger.setLevel(logging.DEBUG)          # 设置日志器的级别

# 创建输出日志到文件的处理器，件按时间来切割
# 每隔5秒钟进行备份，总共备份3次
handler = logging.handlers.TimedRotatingFileHandler("log/test.log", when='S', interval=5, backupCount=3)
handler.setLevel(logging.INFO)

# 将处理器添加到日志器
logger.addHandler(handler)

i = 0
while True:
    #  输出日志信息
    if i < 10 :
        time.sleep(2)
        logger.info("这是一条信息级别的日志!")
        i+=1
    else :
        logger.error("this is an error log")
        break
