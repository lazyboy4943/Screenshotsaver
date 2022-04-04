import os
import shutil
from time import sleep

tempscreenshotfolder = "C:\\Users\\lazyb\\AppData\\Local\\Packages\\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\\TempState\\ScreenClip\\"
newscreenshotfolder = "C:\\Screenshots\\"

while True:
    for file in os.listdir(tempscreenshotfolder):
        if file.endswith('.png'):
            sleep(0.5)
            filename = str(file)
            shutil.move(tempscreenshotfolder+filename, newscreenshotfolder+filename)
