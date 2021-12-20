'''
功能描述：读取目标excel数据
编写人：yangyang
编写日期：
实现逻辑:
导包
 1.确定目标文件
 2.打开目标文件
 3.确定sheet页
 4.确定最大行和列数
 5.遍历读取所有行
    提前定义一个空列表
    5.1.将第一行作为字典key
    5.2.遍历剩余行作为字典value
    5.3.利用推导式合并字典
    5.4.将字典追加到列表中
    5.5.返回列表
'''
import xlrd,os
class ReadExcel():
    def __init__(self):
        #1.确定目标文件
        self.excel = os.path.dirname(os.path.dirname(__file__)) + r'\testData\data.xls'
        #2.打开目标excel
        self.wb = xlrd.open_workbook(self.excel)
        #3.确定sheet页
        self.sh = self.wb.sheet_by_index(0)
        #4.确定最大的行和列数
        self.rownum = self.sh.nrows
        self.colnum = self.sh.ncols

    def getData(self):
        #定义一个空列表
        data = []
        #遍历读取所有行
        # 将第一行作为字典的key
        keyList = self.sh.row_values(0)
        for i in  range(1,self.rownum):
            #遍历剩余行作为字典value
            valueList = self.sh.row_values(i)
            #利用推导式合并字典
            dict1 = {keyList[j]:valueList[j] for j in range(len(keyList))}
            #将组合后的字典追加到列表中
            data.append(dict1)
        #f返回列表
        return data

#自我调试
if __name__ == '__main__':
    re = ReadExcel()
    print(re.getData())
