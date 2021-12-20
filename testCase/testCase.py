'''
功能描述：拿到测试数据，根据接口的请求方式判断进行请求，断言请求结果
编写人：yangyang
编写日期：
实现逻辑:
1.获取测试数据，调用readexcel内部的getdata方法
2.提取测试数据内部的method方法
3.根据methond进行判断
    3.1如果是get就用get请求
    3.2如果是post就用post请求
4.从接口请求的结果中，提取需要断言的字段errorCode
5.将实际提取的errorCode和excel中的预期进行比较
    5.1相同即通过，success
    5.2不同则失败，fail
6.将接口断言得到的结果写入excel中
'''
import unittest,requests
from common.readexcel import ReadExcel
from ddt import ddt,data,unpack
#获取测试数据，调用readexcel内部的getdata方法
re = ReadExcel()
testdata = re.getData()

@ddt

class TestCase(unittest.TestCase):

    @data(*testdata)
    @unpack
    #提取测试数据内部的method方法
    def test_run(self,id,interfaceUrl,name,method,value,expect,real,status):


        method = method
        #准备请求参数
        url = interfaceUrl
        value = eval(value)
        expect = expect
        id = id
        #根据methond进行判断
        if method == 'get':
            result = requests.get(url=url,params=value)
            print('result',result.json())
        elif method == 'post':
            result = requests.post(url=url,data=value)
            print('result',result.json())

            #从接口请求的结果中，提取需要断言的字段errorCode
        real = result.json()['errorCode']
            #将实际提取的errorCode和excel中的预期进行比较
        try:
            self.assertEqual(str(real),str(expect))
            status = 'success'
        except AssertionError as msg:
            print('系统提示：',msg)
            status = 'fail'
            #将接口断言得到的结果写入excel中
        finally:
            pass
if __name__ == '__main__':
    unittest.main(verbosity=2)