import os
import subprocess
import time


def git_do(cmd):
    cmd.insert(0,'git')
    subprocess.run(cmd,check=True)

# git_do(['--version'])
# print("Git Init is Running")
# git_do(['init'])
# time.sleep(1)
dict="/Users/kunjthakor/Documents/Python_Program/New_Folder"
# print("Git Init is Running")

# git_do([ 'remote', 'add', 'origin' ,'https://github.com/kunjthakore/repo2.git'])
# git_do(['add','-A'])
# git_do(['commit' ,'-m', '"commit"'])
# git_do(['push', '-u', 'origin', 'main'])


for name in  dict:
    if os.path.isdir(os.path.join(dict,name)):
        git_do([f'remote', 'set-url', 'origin' ,'https://github.com/kunjthakore/test3.git'])
        git_do(['add','-A'])
        git_do(['commit' ,'-m', '"commit"'])
        git_do(['push', '-u', 'origin', 'main'])
