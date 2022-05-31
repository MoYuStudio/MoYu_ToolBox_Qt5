
# -*- coding: UTF-8 -*-
 
import urllib.request


 
url = 'https://anonfiles.com/v7P6Cal9ye/ViaBackwards-4.2.1_jar'
#IE 9.0 User-Agent
ua_header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"} 

request = urllib.request.Request(url, headers = ua_header)

response = urllib.request.urlopen(url)

# html = response.read()
lines = response.readlines() 
line = str(lines[64])
print(line)
print(line[31:91]+"/"+'ViaBackwards-4.2.1.jar')
lur = line[31:91]+"/"+'ViaBackwards-4.2.1.jar'

request1 = urllib.request.Request(lur, headers = ua_header)
myURL = urllib.request.urlopen(lur)
f = open("ViaBackwards-4.2.1.jar", "wb")
content = myURL.read()  # 读取网页内容
f.write(content)
f.close()