# Introduction to GitHub

In this module, you’ll be introduced to GitHub and learn how it works with Git. You’ll create new repositories and clone those repositories onto your computer. Next, we’ll explain what a remote repository is, how we can work with them, and how we can host them. You’ll get familiar with commands like modify, stage, and commit, which will be used for local changes, as well as the fetch command, which can pull any changes from remote repositories. We'll cover secure shell protocol and when to use API keys. Our final lesson will focus on learning about conflicts. This will allow you to explore the concepts of pull-merge-push workflows, pushing remote branches and rebasing your changes.

**Learning Objectives**
Describe the advantages of using separate branches
Utilize the git rebase command
Describe what GitHub is and how to interact with it
Explain what a remote repository is
Utilize remote repositories, fetch new changes, and update local repositories
Utilize the pull-merge-push workflow to address conflicts
Push remote branches so code can be viewed and tested by collaborators
Explain what rebasing is

## Basic Interaction with GitHub

There are various remote repository hosting sites:

[GitHub](http://github.com/)

[BitBucket](https://bitbucket.org/product)

[Gitlab](https://gitlab.com/)

Follow the workflow at
https://github.com/join
to set up a free account, username, and password. After that,
these steps
will help you create a brand new repository on GitHub.

**Some useful commands for getting started:**

git clone URL

[Git clone is used to clone a remote repository into a local workspace](https://git-scm.com/docs/git-clone)

git push

[Git push is used to push commits from your local repo to a remote repo](https://git-scm.com/docs/git-push)

git pull

[Git pull is used to fetch the newest updates from a remote repository](https://git-scm.com/docs/git-pull)

This can be useful for keeping your local workspace up to date.

https://help.github.com/en/articles/caching-your-github-password-in-git

https://help.github.com/en/articles/generating-an-ssh-key

## Git Remotes

git remote

$ [git remote](https://git-scm.com/docs/git-remote)
allows you to manage the set of repositories or “remotes” whose branches you track.

git remote -v

$ [git remote -v](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt--v)
is similar to $ git remote, but adding the -v shows more information such as the remote URL.

git remote show <name>

$ [git remote show <name>](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emshowem)
shows some information about a single remote repo.

git remote update

$ [git remote update](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emupdateem)
fetches updates for remotes or remote groups.

git fetch

$ [git fetch](https://git-scm.com/docs/git-fetch)
can download objects and refs from a single repo, a single URL, or from several repositories at once.

git branch -r

$ [git branch -r](https://git-scm.com/docs/git-branch#Documentation/git-branch.txt--r)
lists remote branches and can be combined with other branch arguments to manage remote branches.

**Tips for resolving merge conflicts**
Here are some tips to keep in mind when you’re resolving merge conflicts:

After running Git merge, a message will appear informing that a conflict occurred on the file.

Read the error messages that imply you cannot push your local changes to GitHub, especially the remote changes with Git pull.

Use the command line or GitHub Desktop to push the change to your branch on GitHub after you make a local clone of the repository for all other types of merge conflicts.
