#此处使用python自带的logging模块，用来作为测试日志，记录测试中系统产生的信息。
import logging,os
log_file = os.path.join(os.getcwd(),'log/sas.log')
log_format = '[%(asctime)s] [%(levelname)s] %(message)s'     #配置log格式
logging.basicConfig(format=log_format, filename=log_file, filemode='w', level=logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(log_format)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)