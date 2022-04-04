#-*-coding:utf-8 -*-
import os
import sys

dir ='/Users/grey/Documents/may/' # the folder that you want to transform

save_dir = os.path.join(dir,'transormed')

# Don't worry if the save dir doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

def findn(ini_str,occurrence,sub_str='/'):
    """Finding nth occurrence of substring"""
    val = -1
    for i in range(0, occurrence):
        val = ini_str.find(sub_str, val + 1)
    return val

def relpath(root,dir):
    """return the ralative path of root to dir"""
    times = dir.count('/')
    index =findn(dir,times) + 1
    root = root[index:]
    return root
    
for root, folders, files in os.walk(dir):
    for file in files:
        file_path = os.path.join(root, file)
        #gre the relative path
        rel_path = relpath(root,dir)
        new_file_path =os.path.join(save_dir,rel_path)

        if not os.path.exists(new_file_path):
            os.makedirs(new_file_path)
        new_file_path =os.path.join(new_file_path, file)

        newfile = open(new_file_path, mode='w+')
        try:
            newfile.write(open(file_path,'r',encoding='gb2312').read())
        except Exception as e:
            print(file_path)
        newfile.close()

print('success')


