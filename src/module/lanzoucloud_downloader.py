
# -*- coding: UTF-8 -*-
 
import os
import shutil
import zipfile

from lanzou.api import LanZouCloud

class LanZouCloudDownloader:
    def __init__(self):
        self.download_list = []
        self.dezip_list = []
        self.movefile_list = []
        self.runingfile_path = ''

        self.lzy = LanZouCloud()

    def download(self):
        def download_done(file_name):
            print(file_name+' '*3+'done')
        for file in self.download_list:
            self.lzy.down_file_by_url(file[0],file[1],file[2], downloaded_handler=download_done)

    def dezip(self):
        for filelist in self.dezip_list:
            f = zipfile.ZipFile(filelist[0],'r')
            for file in f.namelist():
                f.extract(file,filelist[1])
            f.close()

    def movefile(self):
        for filelist in self.movefile_list:
            for file in os.listdir(filelist[0]):
                full_path = os.path.join(filelist[0], file)
                shutil.move(full_path, filelist[1])

    def delete_runingfile(self):
        for file_name in os.listdir(self.runingfile_path):
            full_path = self.runingfile_path+'/'+file_name
            try:
                os.remove(full_path)
            except:
                pass
            try:
                os.rmdir(full_path)
            except:
                pass

if __name__ == '__main__':
    
    download_list = [['https://wwz.lanzoul.com/iIfFL05oxhwh', '1o27', 'src/module/data/cloudfiles/mc_server_mod'],
                    ['https://wwz.lanzoul.com/iWmWW05oyiyb', '9jo9', 'src/module/data/cloudfiles/zip'],
                    ['https://wwz.lanzoul.com/ibR4h05oyg2h', 'g605', 'src/module/data/cloudfiles/zip']]
    dr = LanZouCloudDownloader()
    dr.download_list = download_list
    dr.download()

    dezip_list = [['src/module/data/cloudfiles/zip/.minecraft.zip', 'src/module/data/cloudfiles/mc_server_mod/'],
                    ['src/module/data/cloudfiles/zip/PCL.zip', 'src/module/data/cloudfiles/mc_server_mod/']]

    dr.dezip_list = dezip_list
    dr.dezip()

    dr.runingfile_path = 'src/module/data/cloudfiles/zip'
    dr.delete_runingfile()