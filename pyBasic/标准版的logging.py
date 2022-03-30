import logging
from logging import handlers
import time
rh = handlers.RotatingFileHandler('myapp.log', maxBytes=1024*1024,backupCount=5) # 按照大小做切割
fh = handlers.TimedRotatingFileHandler(filename='x2.log', when='H', interval=5, encoding='utf-8')

sh = logging.StreamHandler()
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s[line:%(lineno)d] -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level = logging.DEBUG,
    handlers = [rh, fh, sh],
)
for i in range(1,10):
    time.sleep(1)
    logging.error('KeyboardInterrupt error %s'%str(i))