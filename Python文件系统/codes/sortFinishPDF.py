#--coding=utf-8--


"""
功能：把已经处理的PDF移动到PDF_FINISH文件夹
"""


import os


print u'开始整理'

txtpath = raw_input('txt path:')
pdfpath = raw_input('pdf path:')
newpath = raw_input('finished path:')

if not os.path.exists(newpath):
    os.mkdir(newpath)

num = 0

for txtname in os.listdir(txtpath):
    pdfname = txtname.replace('.txt','.pdf')
    if pdfname in os.listdir(pdfpath):
        oldfname= os.path.join(pdfpath,pdfname)
        newfname = os.path.join(newpath,pdfname)
        os.rename(oldfname,newfname)
        num += 1
        
print u'本次处理总数：%d'%num
print u'结束整理'

raw_input('FINISH')
