
import os
import shutil
import zipfile

from lanzou.api import LanZouCloud


lzy = LanZouCloud()

def done(file_name):
    print(file_name+' '*3+'done')

# start.exe
lzy.down_file_by_url('https://wwz.lanzoul.com/iIfFL05oxhwh', '1o27', r'src/module/data/cloudfiles/mc_server_mod', downloaded_handler=done)
# .minecraft.zip
lzy.down_file_by_url('https://wwz.lanzoul.com/iWmWW05oyiyb', '9jo9', r'src/module/data/cloudfiles/zip', downloaded_handler=done)
# PCL.zip
lzy.down_file_by_url('https://wwz.lanzoul.com/ibR4h05oyg2h', 'g605', r'src/module/data/cloudfiles/zip', downloaded_handler=done)

f = zipfile.ZipFile("src/module/data/cloudfiles/zip/.minecraft.zip",'r')
for file in f.namelist():
    f.extract(file,"src/module/data/cloudfiles/mc_server_mod/")
f.close()

f = zipfile.ZipFile("src/module/data/cloudfiles/zip/PCL.zip",'r')
for file in f.namelist():
    f.extract(file,"src/module/data/cloudfiles/mc_server_mod/")
f.close()

# MoYuStudio Minecraft Server 1182 Mod.jar
lzy.down_file_by_url('https://wwz.lanzoul.com/ivt0S05oz21i', '4z5n', r'src/module/data/cloudfiles/mc_server_mod/.minecraft/versions/MoYuStudio Minecraft Server 1182 Mod', downloaded_handler=done)

# pkg1.zip
lzy.down_file_by_url('https://wwz.lanzoul.com/iQoTB05p80ze', 'cbjx', r'src/module/data/cloudfiles/zip', downloaded_handler=done)

# mod_pkg1.zip
lzy.down_file_by_url('https://wwz.lanzoul.com/iUMrm05ozadi', '7zo0', r'src/module/data/cloudfiles/zip', downloaded_handler=done)
# mod_pkg2.zip
lzy.down_file_by_url('https://wwz.lanzoul.com/iq1t905ozlja', '21nj', r'src/module/data/cloudfiles/zip', downloaded_handler=done)
# mod_pkg3.zip
lzy.down_file_by_url('https://wwz.lanzoul.com/irqa605ozlof', '4mww', r'src/module/data/cloudfiles/zip', downloaded_handler=done)
# mod_pkg4.zip
lzy.down_file_by_url('https://wwz.lanzoul.com/iZpGU05ozlpg', 'a59k', r'src/module/data/cloudfiles/zip', downloaded_handler=done)

f = zipfile.ZipFile("src/module/data/cloudfiles/zip/pkg1.zip",'r')
for file in f.namelist():
    f.extract(file,"src/module/data/cloudfiles/zip")
f.close()

f = zipfile.ZipFile("src/module/data/cloudfiles/zip/mod_pkg1.zip",'r')
for file in f.namelist():
    f.extract(file,"src/module/data/cloudfiles/zip")
f.close()

f = zipfile.ZipFile("src/module/data/cloudfiles/zip/mod_pkg2.zip",'r')
for file in f.namelist():
    f.extract(file,"src/module/data/cloudfiles/zip")
f.close()

f = zipfile.ZipFile("src/module/data/cloudfiles/zip/mod_pkg3.zip",'r')
for file in f.namelist():
    f.extract(file,"src/module/data/cloudfiles/zip")
f.close()

f = zipfile.ZipFile("src/module/data/cloudfiles/zip/mod_pkg4.zip",'r')
for file in f.namelist():
    f.extract(file,"src/module/data/cloudfiles/zip")
f.close()


src="src/module/data/cloudfiles/zip/pkg1"
des="src/module/data/cloudfiles/mc_server_mod/.minecraft/versions/MoYuStudio Minecraft Server 1182 Mod"
for file in os.listdir(src):
    full_file_name = os.path.join(src, file)
    print("要被复制的全文件路径全名:",full_file_name)

    shutil.move(full_file_name, des)

src="src/module/data/cloudfiles/zip/mod_pkg1"
des="src/module/data/cloudfiles/mc_server_mod/.minecraft/versions/MoYuStudio Minecraft Server 1182 Mod/mods"
for file in os.listdir(src):
    full_file_name = os.path.join(src, file)
    print("要被复制的全文件路径全名:",full_file_name)

    shutil.move(full_file_name, des)

src="src/module/data/cloudfiles/zip/mod_pkg2"
des="src/module/data/cloudfiles/mc_server_mod/.minecraft/versions/MoYuStudio Minecraft Server 1182 Mod/mods"
for file in os.listdir(src):
    full_file_name = os.path.join(src, file)
    print("要被复制的全文件路径全名:",full_file_name)

    shutil.move(full_file_name, des)

src="src/module/data/cloudfiles/zip/mod_pkg3"
des="src/module/data/cloudfiles/mc_server_mod/.minecraft/versions/MoYuStudio Minecraft Server 1182 Mod/mods"
for file in os.listdir(src):
    full_file_name = os.path.join(src, file)
    print("要被复制的全文件路径全名:",full_file_name)

    shutil.move(full_file_name, des)

src="src/module/data/cloudfiles/zip/mod_pkg4"
des="src/module/data/cloudfiles/mc_server_mod/.minecraft/versions/MoYuStudio Minecraft Server 1182 Mod/mods"
for file in os.listdir(src):
    full_file_name = os.path.join(src, file)
    print("要被复制的全文件路径全名:",full_file_name)

    shutil.move(full_file_name, des)

src = 'src/module/data/cloudfiles/zip'
for file in os.listdir(src):
    full_file_name = src+'/'+file
    try:
        os.remove(full_file_name)
    except:
        pass
    try:
        os.rmdir(full_file_name)
    except:
        pass

