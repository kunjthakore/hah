from re import sub
import subprocess


def git_do(cmd):
    cmd.insert(0,'git')
    subprocess.run(cmd,check=True)

# git_do(['--version'])
# git_do(['init'])
git_do(['status'] )
git_do(['add','--all'])
# git_do(['--version'])
# git_do(['--version'])
# git_do(['--version'])
