###发送邮件
##1导包
import smtplib
from email.mime.text import MIMEText

subject ="天天生鲜"
content ="好好学习"
sender="2633295130@qq.com"
recver ="""2633295130@qq.com"""
password ="wjyieiyparlkeaac"   ###授权码


##2构建发送的邮件内容
message=MIMEText(content,'plain','utf-8')
"""
 _text,  邮件内容 
 _subtype='plain', 内容类型  文本
  _charset=None   字符编码   utf-8
"""
message["Subject"] = subject ##主题
message["From"] = sender  ##发件人
message["To"] = recver ##收件人


##3登录邮件服务器并发送邮件
smtp = smtplib.SMTP_SSL("smtp.qq.com",465)
#登录
smtp.login(sender,password)
smtp.sendmail(sender,recver.split(","),message.as_string())
# sender   发件人
# recver   收件人  可以是一个列表
# message  邮件内容
## as_string() 方法，和json方法类似，序列化的功能，用于在发送邮件中发送邮件内容

##4退出登录
smtp.close()







