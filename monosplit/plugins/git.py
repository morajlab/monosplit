import os
import shutil
from git import Repo

def push_repository(repo_url, repo_path, message):
    tmpdir = os.path.join(os.path.curdir, "temp")
    os.mkdir(tmpdir)
    print('Temporary directory is', tmpdir)
    clone_directory = os.path.join(tmpdir, "test-repo")
    repo = Repo.clone_from(repo_url, clone_directory)
    shutil.copytree(repo_path, clone_directory, dirs_exist_ok=True)

    if repo.is_dirty():
        print("Repository is dirty !")
        repo.git.add(A=True)
        repo.index.commit(message)
        origin = repo.remote(name="origin")
        origin.push()
