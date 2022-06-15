# coding=utf-8
import  time
import  logging
import logging.handlers

# 1.创建日志器
logger = logging.getLogger()
# 2.设置日志器级别
logger.setLevel(level=logging.DEBUG)

# 3.1创建日志输出到控制台的处理器
streamHandler = logging.StreamHandler()

# 3.2创建日志输出到文件的处理器
flHandler = logging.handlers.TimedRotatingFileHandler(
    "./log/log.log", when = "S", interval=2, backupCount=3 )
# 4.设置处理器的级别
streamHandler.setLevel(logging.DEBUG)
flHandler.setLevel(logging.INFO)

# 5.创建格式器
strFmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
fmter = logging.Formatter(fmt=strFmt)

# 6.格式器添加到处理器钟
streamHandler.setFormatter(fmter)
flHandler.setFormatter(fmter)

# 7.处理器添加到日志器
logger.addHandler(streamHandler)
logger.addHandler(flHandler)

# 8.输出日志信息
i =0
while True:
    if i< 20:
        time.sleep(2)
        logging.info("this's info log")
        logging.warning("this's warning log")
        i+=1
    else:
        # 日志输出到控制台的处理器会输出该log
        logging.debug("this's debug log")
        break