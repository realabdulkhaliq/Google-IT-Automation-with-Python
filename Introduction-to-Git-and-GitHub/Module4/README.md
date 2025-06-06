# Collaboration

In this module, you’ll continue to explore the collaboration tools available in Git. You’ll learn about the tools that are available to help improve the quality of your code and to better track your code. This includes an overview of pull requests and how the typical workflow of a pull request looks like on GitHub. Next, you’ll dive into how you can squash changes in your code. We’ll finish up by providing you with a study guide on fork and pull requests. Next up, we’ll cover what code reviews are and what the code review workflow looks like. Then, you’ll learn about how to use code reviews on GitHub. The final lesson of this module will focus on managing projects. We’ll take a rundown of best practices on managing projects and how to manage collaboration within those projects. We’ll explore different ways of tracking issues and finish up by discussing the concept of continuous integration with your projects.

**Learning Objectives**
Utilize the code review workflow
Create, update, and execute pull requests on GitHub
Explain what a code review is
Use code reviews in GitHub
Explain the importance of managing projects and accepting or rejecting changes
Utilize issue trackers
Describe the methodology behind continuous integration

Merge commits. All commits from the feature branch are added to the base branch in a merge commit using the -- no–ff option.

Squash and merge commits. Multiple commits of a pull request are squashed, or combined into a single commit, using the fast-forward option. It is recommended that when merging two branches, pull requests are squashed and merged to prevent the likelihood of conflicts due to redundancy.

Merge message for a squash merge. GitHub generates a default commit message, which you can edit. This message may include the pull request title, pull request description, or information about the commits.

Rebase and merge commits. All commits from the topic branch are added onto the base branch individually without a merge commit.

Indirect merges. GitHub can merge a pull request automatically if the head branch is directly or indirectly merged into the base branch externally.

## SSH authentication

In the previous module, you learned how to generate an SSH key pair and use it for logging in to remote hosts. You can use the same SSH key to authenticate with GitHub.

To add your SSH key for use with GitHub:

Find the public key you generated in the previous module. It will have a filename like id_rsa.pub.

Open
GitHub.com
in your browser.

Click on your profile icon in the top right corner and select Settings.

Go to SSH and GPG keys.

Click New SSH key.

Paste the contents of your public key into the text box and click Add SSH key.

### Resources for more information

[A Quick Guide to Using GitHub for Project Management](https://www.jobsity.com/blog/a-quick-guide-to-using-github-for-project-management)

This article provides a brief overview of project management tools on GitHub.

[GitHub for project management](https://openscapes.github.io/series/core-lessons/github/github-issues.html)

This lesson offers detailed descriptions of GitHub’s project management tools.

[Using GitHub as your Project Management Tool](https://www.youtube.com/watch?v=qgQAFP6oSKw)

This video provides examples on GitHub project management tools.

[GitHub Issues: Project Planning for Developers](https://github.com/features/issues)

This GitHub page shows the many project management tools available for developers.

### Terms and definitions from Course 3, Module 4

CI/CD: The name for the entire continuous integration and continuous deployment system

Code reviews: The deliberate and methodical gathering of other programmers to examine each other's code for errors to increase the code quality and reduces the amount of bugs

Continuous deployment (CD): New code is deployed often after it has been automatically built and tested

Continuous integration (CI): A system that will automatically build and test our code every time there's a change

Fix up: The decision to discard commit messages for that commit

Forking: A way of creating a copy of the given repository so that it belongs to our user

Indirect merges: GitHub can merge a pull request automatically if the head branch is directly or indirectly merged into the base branch externally

Issue tracker (bug tracker): A tracker that shows tasks that need to be done, the state they're in and who's working on them

Merge commits: All commits from the feature branch are added to the base branch

Pipelines: The specific steps that need to run to obtain the desired result

Pull request: A procedure where new code is examined before it is merged to create a branch or master branch

Squash commits: The decision add commit messages together and an editor opens to make any necessary changes

### Project

Advanced git interaction: You use git diff to view and compare code changes and look back at the history of changes. When needed you can use git diff to compare whole branches as the feature becomes more robust. As you get closer to completing the feature you create tags to mark development milestones. When feature release is approaching, you can use a milestone to share progress with stakeholders.

```
# View code changes

git diff

# View commit history

git log

# Create a new tag

git tag v1.0.0


# Compare branches

git diff feature/user-authentication main

Undoing things: As you encounter issues, you have stable milestones you know you can restore back. You can stash away pending changes or, safely undo changes using Git's commands.

# Stash changes

git stash

# Restore changes from stash

git stash pop

# Undo changes in working directory

git checkout -- <file>

Branching and merging: Your team makes sure to keep up with branching and merging changes. The team tests their changes in the feature branch to avoid introducing any issues or bugs into the main branch.

# Merge changes from feature branch to main

git checkout main

git merge feature/user-authentication

# Delete feature branch

git branch -d feature/user-authentication

Solving Conflicts: As code conflicts arise during merging, you attempt to automerge. When deeper conflicts arise, you gather your team and address them collaboratively.

# Attempt to automerge

git merge feature/user-authentication

# Resolve conflicts manually

# Edit files to resolve conflicts

git add <resolved-files>

git commit -m "Resolved conflicts"

Pull requests and code reviews: One of your team members opens up a pull request for your feature branch. It is finally time to merge our feature into the main branch. Automated tests run against the code in question and your team schedules a code review. You prepare to gather and track feedback.

# Push changes and open pull request

git push origin feature/user-authentication

# Automated tests run in CI/CD pipeline

# Pull request is reviewed

# Feedback is addressed

```
