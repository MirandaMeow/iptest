#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import smtplib
import os
from email.mime.text import MIMEText
from email.utils import formataddr

ipFile = './ip.txt'

def email(message):
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['From'] = formataddr(["title", 'email1@email.com'])
    msg['To'] = formataddr(["title", 'email2@email.com'])
    msg['Subject'] = "subject"

    server = smtplib.SMTP("smtp@smtp.com", 25)
    server.login("email1@email.com", "password")
    server.sendmail('', ['email2@email.com', ], msg.as_string())
    server.quit()

def getIP():
    ip = os.popen('curl ifconfig.me').read()
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
