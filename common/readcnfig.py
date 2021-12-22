'''
功能描述：读取config。ini文件，获取目标参数，供其他模块使用
编写人：yangyang
编写日期：
实现逻辑:
1.导包
2.准备目标文件
3.创建对象，调用read方法读取
4.对外提供读取xxsection下的键值对的方法
'''
import configparser,os
from common.logs import logger
class ReadConfig():
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.file = os.path.dirname(os.path.dirname(__file__)) + r'/config.ini'
        self.conf.read(self.file,encoding='utf-8-sig')
        logger.info(f'config.ini文件的路径为：{self.file}')

    def get_data(self,section):
        try:
            result = self.conf.items(section)
            logger.info(result)
        except Exception as msg:
            logger.error(f'系统提示：{msg}')

if __name__ == '__main__':
    re = ReadConfig()

    re.get_data('redis')