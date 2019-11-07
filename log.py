from config import *

# create logger
logger_name = "qwh"
logger = logging.getLogger(logger_name) # 不加名称设置root logger
logger.setLevel(logging.DEBUG)

# create formatter
# fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
fmt = "%(asctime)s %(levelname)s %(message)s"
datefmt = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)

# create file handler
log_path = "./logging.log"
fh = logging.FileHandler(log_path)
fh.setLevel(logging.WARN)
fh.setFormatter(formatter)

# create input handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)


# add handler and formatter to logger
logger.addHandler(fh)
logger.addHandler(ch)

