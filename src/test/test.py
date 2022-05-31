
from lanzou.api import LanZouCloud
lzy = LanZouCloud()
# https://wwz.lanzoul.com/iIfFL05oxhwh
# 密码:1o27

code = lzy.download_dir_by_url('https://wwz.lanzoul.com/iIfFL05oxhwh', '1o27',r'C:\Users\WilsonVinson\Documents\GitHub\MoYu_ToolBox\src\module\data\cloud_files')
# code == LanZouCloud.SUCCESS