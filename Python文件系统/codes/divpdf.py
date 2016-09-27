# --coding=utf-8--

import os

OLDPATH = raw_input('please input the old path:')
NEWPATH = raw_input('please input the new path:')

i = 0
for fname in os.listdir(OLDPATH):
    newpath = os.path.join(NEWPATH,str(int(i/500)+1))
    if not os.path.exists(newpath):
        os.mkdir(newpath)
        print(newpath)
        
    old = os.path.join(OLDPATH,fname)
    new = os.path.join(newpath,fname)
    os.rename(old,new)
    
    i = i + 1

