'''
功能描述：接受testCase传入的接口请求测试数据，根据具体的请求逻辑完成接口测试，将接口返回的关键结果返回给接口
编写人：yangyang
编写日期：
实现逻辑:
1.接受testCase传入的测试数据
2.提取测试数据中的请求方式
3.根据methond进行判断
    3.1如果是get就用get请求
    3.2如果是post就用post请求
4.从接口请求的结果中，提取需要断言的字段ErrorCode
'''
import requests
from common.logs import logger
class ConfigHttp():
    def __init__(self,url,value,method):
        self.url = url
        self.value = value
        self.method = method
        self.header = {}
        logger.debug(f'configHttp模块的初始化方法被调用了,{self.method}')

    def run(self):
        if self.method.lower() == 'get':
            return self.__get()
        elif self.method.lower() == 'post':
            return self.__post()
        elif self.method.lower() == 'put':
            return self.__put()
    def __get(self):
        result = requests.get(url=self.url,params=eval(self.value),headers=self.header)
        realErrorCode = result.json()['errorCode']
        statusCode = result.status_code
        return statusCode,realErrorCode
    def __post(self):
        logger.debug(f'__post方法请求参数为：url={self.url},parmas={self.value},method={self.method},header={self.method}')
        result = requests.post(url=self.url,data=eval(self.value),headers=self.header)
        realErrorCode = result.json()['errorCode']
        statusCode = result.status_code
        logger.info(f'返回的status_code：{statusCode},realErrorCode:{realErrorCode}')
        return statusCode,realErrorCode
    def __put(self):
        result = requests.put(url=self.url,data=eval(self.value),headers=self.header)
        realErrorCode = result.json()['errorCode']
        statusCode = result.status_code
        return statusCode,realErrorCod
if __name__ == '__main__':
    list1 = [{'id': '1', 'interfaceUrl': 'https://www.wanandroid.com/user/login', 'name': 'login', 'method': 'post', 'value': "{'username':'liangchao','password':'123456'}", 'expect': '0', 'real': '', 'status': ''}, {'id': '2', 'interfaceUrl': 'https://www.wanandroid.com/user/register', 'name': 'register', 'method': 'post', 'value': "{'username':'liangchao03','password':'123456','repassword':'123456'}", 'expect': '0', 'real': '', 'status': ''}, {'id': '3', 'interfaceUrl': 'https://www.wanandroid.com/user/logout/json', 'name': 'logout', 'method': 'get', 'value': "{'username':'liangchao'}", 'expect': '0', 'real': '', 'status': ''}]
    url = list1[0]['interfaceUrl']
    value = list1[0]['value']
    method = list1[0]['method']
    ch = ConfigHttp(url,value,method)
    print(ch.run())