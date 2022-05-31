
# -*- coding: UTF-8 -*-
 
import urllib.request

class AnonfilesDownloader:
    def __init__(self,filename,filepath,link):
        self.link = link
        self.filename = filename
        self.filepath = filepath

    def post_link(self,url):
        #IE 9.0 User-Agent
        ua_header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"} 
        request = urllib.request.Request(url, headers = ua_header)
        response = urllib.request.urlopen(url)

        return response

    def get_download_link(self):
        response = self.post_link(self.link)
        lines = response.readlines() 
        line = str(lines[64])

        return line[31:91]+'/'+self.filename

    def download(self):
        response = self.post_link(self.get_download_link())
        file = open(self.filepath+'/'+self.filename, 'wb')
        content = response.read()
        file.write(content)
        file.close()

if __name__ == '__main__':
    ad = AnonfilesDownloader('test.txt','src/module/data','https://anonfiles.com/j184D7ldyb/test_txt')
    ad.download()
