#-*-coding:utf-8-*-

import os


OLDPATH = raw_input('please input the old path:')
NEWPATH = raw_input('please input the new path for rar files:')

if not os.path.exists(NEWPATH):
    os.mkdir(NEWPATH)
    
for root,dirs,files in os.walk(OLDPATH):
    print(root)
    for fname in files:
        if '.rar' in fname:
            os.rename(os.path.join(root,fname),os.path.join(NEWPATH,fname))
        elif '.pdf' in fname:
            os.rename(os.path.join(root,fname),os.path.join(OLDPATH,fname))
