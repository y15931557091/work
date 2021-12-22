'''
功能描述：
编写人：yangyang
编写日期：
实现逻辑:
1.导包
2，初始化方法
    2.1配置邮件属性
3.获取最新报告
4.封装添加邮件正文附件
5.对外提供发邮件方法-登录并发送
'''
import time,os,smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
class ConfigEmail():
    def __init__(self):
        #配置邮箱属性
        #发送邮箱
        self.sender = '601875265@qq.com'
        #接受邮箱
        self.receiver = 'y15931557091@126.com'
        #邮件主题
        t = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime())
        self.subject = '自动化测试结果' + t
        #发送邮箱的服务器
        self.smtpserver = 'smtp.qq.com'
        #发送邮箱的用户名的密码
        self.username = '601875265'
        self.password = 'gnwykcjggffnbead'
        self.current_dir = os.path.dirname(os.path.dirname(__file__))

    def __config(self):
        file = os.listdir(self.current_dir + '/testReport/')[-1]
        with open(self.current_dir + '/testReport/' + file,'rb') as f:
            mail_body = f.read()
            #组装邮件内容和标题
            msg = MIMEMultipart()
            #添加附件内容
            att = MIMEText(mail_body,'plain','utf-8')
            att['Content-Type'] = 'application/octet-stream'
            att['Content-Disposition'] = f'attachment; filename={file}'
            msg.attach(att)
            #添加邮件文本内容
            content = '自动化测试报告详情，请查收邮件'
            msg.attach(MIMEText(content,'plain','utf-8'))
            msg['Subject'] = Header(self.subject,'utf-8')
            msg['From'] = self.sender
            msg['To'] = self.receiver
            return msg
    def send_mail(self):
        msg = self.__config()
        #登录并发送邮件
        try:
            s = smtplib.SMTP()
            s.connect(self.smtpserver)
            s.login(self.username,self.password)
            s.sendmail(self.sender,self.receiver,msg.as_string())
        except Exception as msg:
            print(u'邮件发送失败！%s'%msg)
        else:
            print(f'发送成功！')
if __name__ == '__main__':
    ce = ConfigEmail()
    ce.send_mail()



