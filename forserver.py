# =============================
#
# Luogu-Practice-Detector
#
# Copyright @ zymooll 2023
#
# This source code is licensed under the GPL2.0 license
#
# =============================

import requests
import urllib
from requests_html import HTMLSession
import time

session = HTMLSession()

username = []
useruid = []


file = open(r'ret.csv', 'a')

for i in range(0, len(username)):
    user_number = useruid[i]
    user_name = username[i]
    rp = session.get('https://www.luogu.com.cn/user/' +str(user_number)+'#practice')
    if rp.html.text.find('出错了') == -1:
        ls = urllib.parse.unquote(rp.html.text).encode(
            'utf-8').decode('unicode_escape')
        spn = ls.find("submittedProblems")
        if spn == -1:
            file.write(str(user_number)+','+user_name+','+'Permission denied'+',/,/,/,/,/,/,/,')
        else:
            # print(spn)
            js = [0, 0, 0, 0, 0, 0, 0, 0]
            i = 0
            while i < spn:
                i = ls.find("\"difficulty\":", i+1)
                if i == -1:
                    break
                js[int(ls[i+13])] += 1
            file.write(str(user_number)+','+user_name+','+str(js[0])+','+str(js[1])+','+str(js[2])+','+str(
                js[3])+','+str(js[4])+','+str(js[5])+','+str(js[6])+','+str(js[7])+',')
    else:
        file.write(str(user_number)+','+user_name+','+'User not found'+',/,/,/,/,/,/,/,')
    file.write(time.strftime('%Y-%m-%d,%H:%M:%S,%A,GMT%z\n'))
file.close()
print('Update Completed! '+time.strftime('%Y-%m-%d %H:%M:%S')+'\n')
