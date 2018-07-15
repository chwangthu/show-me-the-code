#-*- coding:utf-8 -*-
#!usr/bin/env python3

from urllib import request, parse
from http import cookiejar

def login_renren():
    login_page = "http://www.renren.com/PLogin.do" #login page, use wireshark to get
    cj = cookiejar.CookieJar()
    opener = request.build_opener(request.HTTPCookieProcessor(cookiejar=cj), request.HTTPHandler(debuglevel=0))
    opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
    data = parse.urlencode({"email":"email", "password":"password"})
    data = data.encode(encoding='utf-8')
    op = opener.open(login_page, data)
    
    print("type=")
    print(type(op))
    print(op.geturl())
    result = op.read()
    #print(result)
    html = result.decode()
 
    with open('renren.html','w') as f:
        f.write(html)

if __name__ == '__main__':
    login_renren()
