import git
import os
import subprocess

gitUrl = "https://github.com/kunjthakore/repo2.git"
cwd = "//Users//kunjthakor//Documents//Python_Program//New_Folder"

with open("migrateList.txt", "r") as file:
    for line in file:
        #configure gitUri for each repository
        gitUri = gitUrl + line.strip() + ".git"
        try:
            global repo
            repo = git.Repo.clone_from(gitUri, cwd + line.strip())
        except:
            print(" directory already available")
        os.chdir(cwd + line.strip())

        #checkout new branch for migration
        repo.git.checkout('-b', "jenkinsMigrate")

        subprocess.call(["git", "mv", "Jenkinsfile", "Jenkinsfile.migrate"])
        repo.git.add(update=True)
        repo.index.commit("jenkins migration")
        origin = repo.remote(name='origin')

        #push new branch to github
        subprocess.call(["git","push", "--set-upstream", "origin", "jenkinsMigrate"])
        subprocess.call(["cd", ".."])