#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import smtplib
import os
from email.mime.text import MIMEText
from email.utils import formataddr

ipFile = './ip.txt'

def email(message):
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['From'] = formataddr(["title", 'email1@email.com'])         #发送邮件的邮箱和名称
    msg['To'] = formataddr(["title", 'email2@email.com'])           #接受邮件的邮箱和名称
    msg['Subject'] = "subject"

    server = smtplib.SMTP("smtp@smtp.com", 25)                      #发送方的邮箱 SMTP 地址和端口
    server.login("email1@email.com", "password")                    #发送方的邮箱账户和密码
    server.sendmail('', ['email2@email.com', ], msg.as_string())    #接收方的邮箱
    server.quit()

def getIP():
    ip = os.popen('curl ifconfig.me').read()                        #使用 curl 命令
    return ip

def writeFile(text):
    with open(ipFile, 'w+') as file:
        file.truncate()
        file.write(text)

def readFile():
    with open(ipFile, 'r') as file:
        return file.read()

if __name__ == '__main__':
    nowIP = getIP()
    if os.path.exists(ipFile) == False:
        writeFile(nowIP)
        email(nowIP)
        exit()
    savedIP = readFile()
    if savedIP == nowIP:
        print('IP is not changed!')
        exit()
    else:
        writeFile(nowIP)
        email(nowIP)
