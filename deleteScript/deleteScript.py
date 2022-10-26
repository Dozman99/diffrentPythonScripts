import os
import datetime
import glob
import sys

path = sys.argv[1] #argv[0] is your current python file and argv[1] is first argument where you want to delete files from
logging_path='Enter your log directory path'
destination = sys.argv[2] #argv[2] is the destination where you want to move the files

if not os.path.isdir(logging_path):
    os.mkdir(logging_path)
else:
    print("Directory already exists")

today = datetime.datetime.today()
os.chdir(path)

file=open(logging_path+datetime.datetime.today().strftime('%d-%m-%Y')+'.txt','a')

for root,directories,files in os.walk(path,topdown=False):
    for name in files:
        t = os.stat(os.path.join(root, name))[8]
        print(t)
        # filetime = datetime.datetime.fromtimestamp(t) - today
        # if filetime.days <= -1:
        #     print(os.path.join(root, name), filetime.days)
        #     file.write(os.path.join(root, name)+' created '+str(-1*filetime.days)+' days ago\n')
        #     carry = path + name
        #     os.rename(path + name, destination + name)
        #     # os.remove(os.path.join(root, name))