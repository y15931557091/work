'''
功能描述：拿到testCase的断言结果，写入到data。xls中
编写人：yangyang
编写日期：
实现逻辑:
1.导包
2.定义写入的数据类
 2.1定义初始化方法
  2.1.1准备写入的Exel文件
  2.1.2确定sheet页
 2.2.定义写入数据的方法
  2.2.1准备写入的数据（real，status）
  2.2.2准备写入的目标单元格的行和列
  2.2.3开始写入
'''
import xlrd,os
from xlutils.copy import copy
from common.logs import logger
class WriteExcel():
    def __init__(self):
        #准备写入的excel
        self.excel = os.path.dirname(os.path.dirname(__file__)) + r'/testData/data.xls'
        logger.info(f'写入excel的路径为：{self.excel}')
        self.rb = xlrd.open_workbook(self.excel)
        self.wb = copy(self.rb)
        #确定sheet页
        self.sh = self.wb.get_sheet(0)
    def writeData(self,x,y,real,status):
        self.sh.write(int(x),y,real)
        self.sh.write(int(x),y+1,status)
        self.wb.save(self.excel)
if __name__ == '__main__':
    we = WriteExcel()
    we.writeData(1,6,'happy','newyear')
