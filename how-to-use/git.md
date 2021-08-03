> A very interesting [website](https://learngitbranching.js.org/) to practice git commands, strongly recommended!

# Frequently-used commands

```bash
git clone <git_or_https_link_of_a_repository> # Clone a project from remote to local.

git pull # Get updates from remote to local, and merge the changes.

git add <file> # Register the changes of the file.

git commit -m <'your comments' ># Make comments about the changes.

git push # Push the changes from local to remote.

git push --set-upstream origin branch # If this is the first time that this branch being pushed.


git branch # Print all the local branches, your current branch starts with *.

git branch -vva # # Print all the local and remote branches.

git branch -f <one_branch> <another_branch> # Replace one_branch by another_branch by force.

git branch -D <branch_to_be_deleted> # Delete a branch from local.

git push origin :<branch_to_be_deleted> # Delete a branch from remote.

git push origin --delete <branch_to_be_deleted> # Delete a branch from remote.

git push -f origin master # Push local master to remote master by force.


git checkout <another_branch> # Switch to another branch.

git checkout -b <new_branch> # Create a new branch and switch to it, coping everything from current branch to the new branch.

git checkout <another_branch> <file> # Replace a file by the file from another branch (local).

git checkout origin/<another_branch> <file> # Replace a file by the file from another branch (remote).

git checkout origin/master <file> # Replace a file by the file from remote master branch.

git checkout commit-id <file> # Replace a file by the file from another commit.

git checkout HEAD <file> # Discard added but un-committed local changes of a file.

git checkout <file> # Discard un-added local changes of a file.

git restore <file> # Discard un-added local changes of a file.


git reset --hard origin/master # Made the current branch the same status as remote master branch.

git reset --hard commit-id # Made the current branch the same status as the specified commit-id.


git diff origin/master # Display the changes of the current branch compared with the remote/master (Ctrl + Z to exit).

git diff origin/master --name-only # Display the changes of the current branch compared with the remote/master (only show the filenames).

git status # Display the status of the current branch.


git merge <another_branch> # Merge another branch into the current branch.

git merge master # Merge local master branch into the current branch.

git rebase master # Get updated from local master branch.


git stash # Temporarily save the local changes, which you have not added and committed.

git stash list # List all the local changes that you saved

git stash drop <stash index> # Discard the saved local changes by stash index. For example, stash@{0}, where 0 is the stash index.

git stash pop # Restore the latest local changes that you saved.

git stash apply <stash index> # Restore the local changes that you saved, according to the stash index.


git move <file_old> <file_new> # Rename a file both locally and remotely.

git rm <file> # Delete a file both locally and remotely.

git rm --cached <file> # Delete a file remotely (keep the local one).

git rm --cached -r <folder> # Delete a folder remotely (keep the local one).


git remote -v # Check how many remote branches

git remote add upstream <git_url_of_another_project> # Get remote upstream master from git_url_of_another_project

git pull upstream master # Pull from the remote upstream master

git remote remove upstream # Remove upstream

```

# Set up a Git repository
## Git global setup
```bash
git config --global user.name "your user name"
git config --global user.email "your.user.name@example.com"
```

## Create a new repository
```bash
git clone git@github.com:ykaitao/setting-up-a-professional-data-science-environment.git
cd setting-up-a-professional-data-science-environment
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master
```

## Existing folder
```bash
cd setting-up-a-professional-data-science-environment
git init
git remote add origin git@github.com:ykaitao/setting-up-a-professional-data-science-environment.git
git add .
git commit -m "Initial commit"
git push -u origin master
```

## Existing Git repository
```bash
cd setting-up-a-professional-data-science-environment
git remote set-url origin git@github.com:ykaitao/setting-up-a-professional-data-science-environment.git
git push -u origin --all
git push -u origin --tags
```
