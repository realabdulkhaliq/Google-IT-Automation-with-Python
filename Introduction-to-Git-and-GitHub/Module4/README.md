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
