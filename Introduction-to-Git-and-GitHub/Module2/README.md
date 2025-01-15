# Using Git Locally

In this module, you’ll dive into advanced Git interactions by skipping the staging area for small code changes, and understand how Git uses the HEAD alias to represent checked-out snapshots. Next, you’ll explore how to move and remove files before finally getting a study guide to help you in your Git explorations! The next step of your learning will include how to undo changes before committing and how to amend commits once they’re submitted. Finally, you’ll be able to identify errors in commits that were submitted a while back. In the final section of this module, you’ll explore the concept of branching and merging. You’ll learn what a branch is, how to create one, and how they work in harmony with you and your code. Once you’re comfortable with branching, you’ll dive into merging, how it works with branched data, and how to deal with merge conflicts.

**Learning Objectives**

- Skip the staging area to delete and move files within Git
- Delete and rename files in a repository
- Amend and roll back commits
- Explain the concept of branching and merging
- Create new branches
- Use merging to combine branched data
- Manage and handle merge conflicts

## Advanced Git

Command

Explanation & Link

git commit -a

$ [git commit -a](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---all)
automatically stages the files that have been locally modified. New files which have not been published yet are not affected.

git log -p

$ [git log -p](https://git-scm.com/docs/git-log#generate_patch_text_with_p)
produces patch text that displays the lines of code that were changed in each commit in the current repo.

git show

$ [git show](https://git-scm.com/docs/git-show)
shows you one or more object(s) such as blobs, trees, tags, and commits.

git diff

$ [git diff](https://git-scm.com/docs/git-diff)
is similar to the Linux `diff` command, and can show the changes between commits, changes between the working tree and index, changes between two trees, changes from a merge, and so on.

git diff --staged

$ [git diff --staged](https://git-scm.com/docs/git-diff)
is an alias of $ git diff --cached, which shows all staged files compared to the named commit.

git add -p

$ [git add -p](https://git-scm.com/docs/git-add)
allows a user to interactively review patches before adding to the current commit.

git mv

$ [git mv](https://git-scm.com/docs/git-mv)
is similar to the Linux `mv` command. This command can move or rename a file, directory, or symlink.

git rm

$ [git rm](https://git-scm.com/docs/git-rm)
is similar to the Linux `rm` command. This command deletes or removes a file from the working tree.

There are many useful git command summaries online as well. Please take some time to research and study a few, such as
this one.

.gitignore files
.gitignore files are used to tell the git tool to intentionally ignore some files in a given Git repository. For example, this can be useful for configuration files or metadata files that a user may not want to check into the master branch.

When writing a .gitignore file, there are some specific formats which help tell Git how to read the text in the file. For example, a line starting with # is a comment; a slash / is a directory separator. Visit
https://git-scm.com/docs/gitignore
to see more examples.

This GitHub repository
offers some examples of configurations which are often included in a .gitignore file. These examples include: compiled sources, packages, logs, databases, and OS generated files.

## Git Revert

When writing and committing code, making mistakes is a common occurrence. Thankfully, there are multiple ways for you to revert or undo your mistakes. Take a look at the helpful commands below.

[git checkout](https://git-scm.com/docs/git-checkout)
is used to switch branches. For example, you might want to pull from your main branch. In this case, you would use the command git checkout main. This will switch to your main branch, allowing you to pull. Then you could switch to another branch by using the command git checkout <branch>.
