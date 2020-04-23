import shutil,os
sou=r'C:\Users\Darshan H D\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
des=r'E:\Windows Spotlight Wallpapers\New folder'
jun=r'E:\Windows Spotlight Wallpapers\New folder\Junk'
for files in os.listdir(sou):
    s=os.path.join(sou,files)
    d=os.path.join(des,files+'.jpg')
    j=os.path.join(jun,files+'.jpg')
    if (os.path.getsize(s))<150000:     #because wallpapers are above 150KB in size
        shutil.copy(s,j)
    else:
        shutil.copy(s,d)