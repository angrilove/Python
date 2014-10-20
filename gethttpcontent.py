#!/share/bin/
#encoding:utf8

import urllib2
print('开始获取内容')
httpContent = urllib2.urlopen('http://gate.guokr.com/').read()
print(httpContent)
