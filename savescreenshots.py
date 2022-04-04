import os
import shutil
from time import sleep
import time




tempscreenshotfolder = "C:\\Users\\lazyb\\AppData\\Local\\Packages\\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\\TempState\\ScreenClip\\"
newscreenshotfolder = "C:\\Screenshots\\"

while True:
    for file in os.listdir(tempscreenshotfolder):
        if file.endswith('.png'):
            sleep(0.5)
            curtime = str(time.ctime())
            curtimelist = curtime.split(":")
            curtime = ''.join(curtimelist)
            filename = str(file)
            shutil.move(tempscreenshotfolder+filename, newscreenshotfolder+curtime+'.png')
