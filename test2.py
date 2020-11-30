import os
import os.path
import shutil

rootdir = r"C:\Users\user\Desktop\data\train"
# rootdir = r"C:\Users\user\Desktop\data\valid"

def f(rootdir):
    for dir2 in os.listdir(rootdir):
        for b in os.listdir(rootdir+'/'+dir2):
            #print(dir2,b)
            shortname,_=os.path.splitext(b)
            #print(shortname)
            with open(rootdir+'/'+dir2+'/'+shortname+'.txt','w') as f:
                f.write(dir2)
# f(rootdir)

def copy(src,dest):
   for root, dirs, files in os.walk(src):
        for file in files:
            src_file = os.path.join(root, file)
            shutil.copy(src_file, dest)
            print(src_file)
copy(r"C:\Users\user\Desktop\data\train",r"C:\Users\user\Desktop\data\all")
copy(r"C:\Users\user\Desktop\data\valid",r"C:\Users\user\Desktop\data\all")