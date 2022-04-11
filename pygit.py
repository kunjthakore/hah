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
        git_do(['init',f'{dicto}'])
        git_do(['remote', 'set-url', 'origin' ,'https://github.com/kunjthakore/test4.git'])
        git_do(['status'])
        git_do(['add','--all'])
        git_do(['commit','-m','"newpush"'])
        git_do(['push', 'origin', 'main'])
