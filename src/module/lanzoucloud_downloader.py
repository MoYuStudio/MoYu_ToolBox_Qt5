
# -*- coding: UTF-8 -*-
 
import os
import shutil
import zipfile
import threading

from lanzou.api import LanZouCloud

class LanZouCloudDownloader:
    def __init__(self):
        self.runingfile_path = 'src/module/data/cloud_files/runing_files'

        self.lzy = LanZouCloud()

    def download_list(self,list_name):
        list_file = open(os.getcwd()+'/src/module/data/lanzoucloud_downloader/'+list_name,'r')
        list = list_file.read()
        list_file.close()
        list = eval(list)

        return list

    def download(self,list_name):
        def download_done(file_name):
                print(file_name+' '*3+'done')
        list = self.download_list(list_name)

        for code in range(len(list)):
            file_data = list[code]
            self.lzy.down_file_by_url(file_data['url'],file_data['password'],file_data['save_path'], downloaded_handler=download_done)
            if file_data['unpackable'] == True:
                f = zipfile.ZipFile(file_data['save_path']+file_data['name'],'r')
                for file in f.namelist():
                    f.extract(file,file_data['unpack_path'])
                f.close()
            if file_data['move'] == True:
                for file in os.listdir(file_data['unpack_path']+file_data['name'][:-3]):
                    full_path = os.path.join(file_data['unpack_path']+file_data['name'][:-3], file)
                    shutil.move(full_path, file_data['move_path'])

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

    dr = LanZouCloudDownloader()
    dr.download('mc_server_mod')