
# -*- coding: UTF-8 -*-
 
import os
import shutil

class AutoStart:
    def __init__(self, switch):
        self.switch = switch

    def windows_write_cmd(self):
        path = os.getcwd()
        bat = open('moyu_toolbox_autostart.bat','w')
        cmd_data = path[0]+path[1]+'\n'
        cmd_data += 'cd '+path+'\n'
        cmd_data += 'start MoYuToolBox.exe\n'
        bat.write(cmd_data)
        bat.close()

    def windows_set_cmd(self):

        if self.switch == True:
            self.windows_write_cmd()
            try:
                os.remove('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Startup/moyu_toolbox_autostart.bat')
            except:
                pass
            try:
                shutil.move(os.getcwd()+'/moyu_toolbox_autostart.bat','C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Startup')
            except:
                pass

        if self.switch == False:
            try:
                os.remove('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Startup/moyu_toolbox_autostart.bat')
            except:
                pass
            