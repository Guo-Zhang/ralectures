#-*-coding:utf-8-*-

import os


fname = raw_input('please input the file name: ')
f = open(fname,'rb')
args = list(set(f.readlines()))
f.close()

for arg in args:
    name,url = arg.split(',')
    url = url.replace('\n','')
    fp = open('urls','ab')
    fp.write(url)
    fp.write('\n')
    fp.close()

