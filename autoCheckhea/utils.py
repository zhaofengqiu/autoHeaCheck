import smtplib
import re
import time
import os
from email.parser import Parser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import encoders
from email.mime.base import MIMEBase
import time
import socket
message=MIMEMultipart()
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


#write a email
def write(str_data,fromaddr,toaddr):
    mimes=[]
    message = MIMEMultipart()
    message['from'] = Header(fromaddr, 'utf-8')
    message['to'] = Header(toaddr, 'utf-8')
    message['subject'] = Header('自动填报健康状态回单表', 'utf-8')
    return MIMEText(str_data, 'plain', 'utf-8')

# 发送邮件
def post(message,msgfrom,msgto,smtpPasswd):
    print(msgfrom,msgto)
    smtpServer = 'smtp.qq.com'
    smtpPort = '465'
    while True:
        try:
            smtp = smtplib.SMTP_SSL(smtpServer, smtpPort)
            smtp.login(msgfrom, smtpPasswd)
            smtp.sendmail(msgfrom, msgto, str(message))
            smtp.quit()
            break
        except Exception as ce:
            print(ce)
            #time.sleep(20)
            #post(message)
