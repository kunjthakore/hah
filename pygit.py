import subprocess
import time


def git_do(cmd):
    cmd.insert(0,'git')
    subprocess.run(cmd,check=True)

# git_do(['--version'])
# print("Git Init is Running")
# git_do(['init'])
# time.sleep(1)

# print("Git Init is Running")
# git_do(['commit' ,'-m', '"first commit"'])
# git_do([ 'remote', 'add', 'origin' ,'https://github.com/kunjthakore/repo2.git'])
# git_do(['push', '-u', 'origin', 'main'])
git_do(['add','-A'])

