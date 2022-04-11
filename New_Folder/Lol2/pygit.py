from fnmatch import fnmatch
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
dicto="/Users/kunjthakor/Documents/Python_Program/New_Folder"
# print("Git Init is Running")

# git_do([ 'remote', 'add', 'origin' ,'https://github.com/kunjthakore/repo2.git'])
# git_do(['add','-A'])
# git_do(['commit' ,'-m', '"commit"'])
# git_do(['push', '-u', 'origin', 'main'])


dictlist=os.listdir(dicto)


for name in  dictlist:
    if os.path.isdir(os.path.join(dicto,name)):
        git_do(['init',f'{dicto}/{name}'])
        git_do(['status',f'{dicto}/{name}'])
        git_do(['add',f'{dicto}/{name}'])
        git_do(['commit' ,'-m',f'{dicto}/{name}'])
        git_do(['remote', 'remove', 'origin'])
        git_do(['remote', 'add', 'origin' ,'https://github.com/kunjthakore/test4.git'])
        git_do(['push', 'origin', 'main'])
