'''
功能描述：定义公共的日志输出模块，供其他模块调用
编写人：yangyang
编写日期：
实现逻辑:
1.导包
2.定制basicConfig参数
3.获取日志记录器
4.返回 return
'''
import logging
def log():
    logging.basicConfig(level=logging.INFO,format='%(name)s-%(asctime)s-%(levelname)s-%(message)s')
    logger = logging.getLogger('InterfaceTest')
    return logger

logger = log()
if __name__ == '__main__':

    logger.info('这是我的log调用日志')