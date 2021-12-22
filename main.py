'''
功能描述：查找所有的测试用例，执行测试用，并生成报告，实现自动清理报告
编写人：yangyang
编写日期：
实现逻辑:
1.导包unittest，HTMLTestRunner
2.使用TestLoder查找测试用例，生成测试套件
3.使用HTMLTestRunner执行测试用例，并生成报告
4.实现自动清理报告（1.自动判断报告数量2.每次运行前删除以前的旧报告；二选一即可）
5.自动将生成的报告添加到邮件并发送
'''
import unittest,os,time
from HTMLTestRunner import HTMLTestRunner
from common.logs import logger
from common.configEmail import ConfigEmail

def create_suite():
    case_dir = os.path.dirname(__file__) + '/testCase'
    suite = unittest.defaultTestLoader.discover(start_dir=case_dir,pattern='test*.py',top_level_dir=None)
    return suite

#实现自动清理报告
# def auto_clear():
#     #方法1-每次运行前，删除旧报告
#     #1.1.获取目标目录下所有文件名
#     filelist = os.listdir(os.path.dirname(__file__) +'/testReport/')
#     logger.info(f'report下面的所有文件：{filelist}')
#     #2，遍历删除
#     for i in filelist:
#         os.remove(os.path.dirname(__file__) +'/testReport/' + i)

    #方法2-自动判断报告数量

    # 1.获取目标目录下所有文件名
    # 2.判断个数，是否超过5个
    #     2.1.不超过5个，不需要任何操作
    #     2.2超过5个
    #         2.2.1.获取每个文件的创建时间
    #         2.2.2按照时间排序
    #         2.2.3.把超过的数量按照时间排序后的结果删除

def auto_clear2():
    filelist2 = os.listdir(os.path.dirname(__file__) + '/testReport')
    if len(filelist2) > 5:
        for i in range(len(filelist2)-5):
            logger.debug(f'{i}')
            os.remove(os.path.dirname(__file__)  + '/testReport/'  + filelist2[i])


if __name__ == '__main__':
    auto_clear2()
    suite = create_suite()
    current_time = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime())
    report = os.path.dirname(__file__) + '/testReport/' + current_time + 'report.html'
    fp = open(report,'wb')
    runner = HTMLTestRunner(stream=fp,title='玩安卓接口测试',description='玩安卓接口测试报告')
    runner.run(suite)
    fp.close()
    ce = ConfigEmail()
    ce.send_mail()

