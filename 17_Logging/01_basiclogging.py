import logging
# logging中默认的日志级别为WARNING级别，
logging.debug("这是一条调试信息")   # 不会打印出来
logging.info("这是一条普通信息")    # 不会打印出来
logging.warning("这是一条警告信息")
logging.error("这是一条错误信息")
logging.critical("这是一条严重错误信息")