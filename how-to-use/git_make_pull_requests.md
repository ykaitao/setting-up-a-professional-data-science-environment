> This file shows the steps of how to make a pull request.

# Terms explaination:
> local, your local computer.

> origin, your own remote space (your own GitHub space in this case)

> upstream, other's remote space where you forked the repository (other's GitHub space in this case)

# Get `SSH link` of a repository
- Go to GitHub repository [
setting-up-a-professional-data-science-environment](https://github.com/ykaitao/setting-up-a-professional-data-science-environment)
- Click the `Fork` button on the top-right conner, forking the above repository from `ykaitao` into `your own GitHub space`.
- Go to `your own GitHub space`.
- Click `setting-up-a-professional-data-science-environment` in `your own GitHub space`.
- Click the drop-down menu of `Code`.
- Click `SSH`
- Copy the `SSH link` of the repository.

# Clone a project from `remote` to `local`
- Open vs-code
- Open a new terminal of vs-code
- Run the following command:
```bash
cd # Go to your home directory, you can `cd` to any other directory if you wish.
git clone ssh_link_of_a_repository # Clone a repository from `remote` to `local`.
cd setting-up-a-professional-data-science-environment # Go into the project folder.
```

# Some global settings
```bash
git config --global user.name "your user name"
git config --global user.email "your.user.name@example.com"

git remote add upstream git@github.com:ykaitao/setting-up-a-professional-data-science-environment.git # Get remote upstream master from git_url_of_another_project
git remote -v # Check how many remote branches
```

# Make changes on your `local` machine
```bash
git checkout -b <new_branch> # Create a new branch and switch to it, coping everything from current branch to the new branch.
git branch # Print all the local branches, your current branch starts with *.
```

# Push changes from `local` to `origin remote`
```bash
git add <file> # Register the changes of the file.
git commit -m <'your comments' ># Make comments about the changes.
git push # Push the changes from local to remote.
git push --set-upstream origin branch # If this is the first time that this branch being pushed.
```

# Make a `pull request` from `origin remote` to `upstream remote`
```bash
```

# Code review and merge
```bash

```

# Clean up branches
```bash
git checkout master
git branch -D <branch_to_be_deleted> # Delete a branch from local.
git push origin :<branch_to_be_deleted> # Delete a branch from remote.
git push origin --delete <branch_to_be_deleted> # Delete a branch from remote.
```

# Update your `local` from `upstream remote`
```bash
git fetch upstream
git rebase upstream/master master
```
