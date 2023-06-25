title: Git
date: 2020-06-12 12:00
author: Alex
### Intro
To begin with you'll need to have a computer to store a folder with content (local repo). After you are happy with you content you can 'send' it to remote repo. Sometimes it is vice versa from remote you get some code into your computer. Anyway computer and github account can be conected that is why I write all this article noise. I am born 1988 and use internet since 2007 daily and getting github account (around year 2017) is the best thing happened to me on the Internet. 

### Git Basics
Great ressource to start with is the codecademy.com where most of the examples here are pulled from: <https://www.codecademy.com/learn/learn-git>

### Cheatsheet 
    git branch: Lists all a Git project’s branches.
    git branch branch_name: Creates a new branch.
    git checkout branch_name: Used to switch from one branch to another.
    git merge branch_name: Used to join file changes from one branch to another. (branch_name is a giver branch)
    git branch -d branch_name: Deletes the branch specified.
    giver branch receiver branch

### Setup and First commit
```
  ______________
||             ||
||             ||
|| C:\here\.git||  --> <https://github.com/thisAKcode/here>
||             ||
||_____________||           
|_______________|
 \\#############\\
  \\#############\\
   \      _____    \   
    \_____\____\____\    
 ```   
 LOCAL repository > REMOTE repository

C:\here    --> https://github.com/thisAKcode/here

### Initial Setup
`git config --global user.name "thisAKcode"`

`git config --global user.email "alekseikupiakov@hotmail.com`

To set up Git username and email you can check github documentation:

<https://docs.github.com/en/github/getting-started-with-github/set-up-git>

<https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/setting-your-commit-email-address>

### HTTPS | SSH
GitHub offers two authentication options, HTTPS and SSH.
I use HTTPS. There is an article on caching your password to configure your computer to be able to [use HTTPS](https://docs.github.com/en/github/using-git/caching-your-github-credentials-in-git).

### Making First Commit! 
Commit is a command that executed at the end of writing.
```bash
mkdir git_practice
cd git_practice
git init 
echo "Hello Git and GitHub" >> README.txt
git add README.txt
git commit -m "First commit"
```
Type `git status` to check new or edited files and folders. 

### Link GitHub repo to local Git repo 
1. Create remote repo on GitHub named `/here.git`.
2. Push an existing repository from the command line

```bash
git remote add origin https://github.com/thisAKcode/Git.git
git push -u origin master
```
If it is first time you are prompted for username and password
The push is complete after the above command executed succesfully.

### Backtracking
Different ways to backtrack in git:

    git checkout HEAD filename: Discards changes in the working directory.
    git reset HEAD filename: Unstages file changes in the staging area.
    git reset commit_SHA: Resets to a previous commit in your commit history.

### Eraser features
How do I get rid of some changes that were made?
Imagine scenario:
I create a file in a working directory.
I add some initital content ("... enikibeniki") to it : `vim myfile.txt`
```bash
here is my original content
Here I have to add bogus on the next line.
"enikibeniki"
```
I add changed file to staging area then commit
```
git add myfile.txt
git commit -m "added some bogus"
```
Now myfile looks like that `cat myfile.txt`
```
here is my original content
Here I have o add bogus on the next line.
"enikibeniki"
```
### Head Commit
You are currently on commit that is called HEAD. 
`HEAD` is at the most recent commit
To check HEAD: `git show HEAD`
```bash
commit f33412218ee787f149e41f6d8d9d2d25a50ec190 (HEAD -> master)
Author: AKcode <43783718+thisAKcode@users.noreply.github.com>
Date:   Fri Mar 12 14:57:41 2021 +0100

    added some bogus

diff --git a/myfile.txt b/myfile.txt
new file mode 100644
index 0000000..9784014
--- /dev/null
+++ b/myfile.txt
@@ -0,0 +1,3 @@
+here is my original content
+Here I have to add bogus on the next line:
+"enikibeniki"
```
###  Edit and Call `git diff` to Inspect Changes 
`
I change the last line in the working directory adding some extra chars.
```
here is my original content
Here I have to add bogus on the next line.
"enikibeniki" and "elivareniki"
```
`git diff` results in: 
```
warning: LF will be replaced by CRLF in myfile.txt.
The file will have its original line endings in your working directory
diff --git a/myfile.txt b/myfile.txt
index 9784014..7e3c898 100644
--- a/myfile.txt
+++ b/myfile.txt
@@ -1,3 +1,3 @@
 here is my original content
 Here I have to add bogus on the next line:
-"enikibeniki"
+"enikibeniki" and "elivareniki"
```
#### Scenario: Suddenly I Change My Mind 
Then I decided to discard added chars `and "elivareniki"`. 
In a working directory I want to get my file look as it was before `and "elivareniki"` insert .
`git checkout HEAD myfile.txt`
Changes made to myfile.txt will be gone. Most recently-committed version of the file overwrite your current copy. 
So you get back your thing, and to prove than do `git show HEAD`
```
+here is my original content
+Here I have to add bogus on the next line:
+"enikibeniki"
```
sweet! 

### More on git add
It is possible to add to the staging area, and commit them to a repository in a single commit. 
```
git add file_1 file_2
git commit -m "try to commit 2 things"
```
### git reset I
Think if you in file_2 did delete an important line. 
Unstage that file from the staging area using 
`git reset HEAD file_2`
It doesn't affect on working directory, but removes changes from the staging area.
`M file_2`
`M` is short for “modification” 
`git commit rectified` 

### git reset II 
When you get lost in your commits you can rewind the part to before you got confused.
Print out git commit log `git log`, press “q” to escape.

Choose the previous commit from list of past commits.

`git reset commit_SHA` using 7 characters of SHA.

`git reset 1a232456` The characters are hexadecimal digits (0-9, a-f) 

HEAD goes to commit of your choice. 
Commits after reset are not part of your project anymore.

### Practice Backtracking
To discard changes and restore a fiel in the working directory, do checkout HEAD version of file1 as per last commit: 
`git checkout HEAD file1` or use common shortcut: `git checkout -- filename`. Close and re-open the `file1` to see the result.
Restored and completed file1 has to be added to the staging area along with two files `file2` and `file3`.

### Practice Unstage `file1` After `git add .`.
Unstage & then continue commit files that you consider okay to commit 
```bash
git reset HEAD file1
git commit -m "files good to go
```

#### Practice Regret My Last Commit
Here is commit I edit
After `git add. && git commit -m "my message"` I decided to rollback.
`git reset d1fc1f2`
Here’s a problem: reset HEAD to a previous commit, but the changes persist in the working directory.
Git backtracking command that you already know can discard changes to the working directory

`git checkout HEAD file1.txt`

Yeah!

### Practice Reset
You have some content in the last commit that was deleted in the working directory. To get that back, discard changes in the working directory for file_x.txt
```bash
git reset file_x.txt
git checkout -- file_x.txt
```
...then edit file and add the file to the stagin area 

`git add file_x.txt && git commit -m "changes to file_x"`
... then you come up with idea that you forgot add signature

---

**NOTE**

`add .` is used broadly but make sure you always know what you’re adding. 

---

### Remove the File From Staging Commit
Add 3 files to the staging area
`git add file_x.txt file_y.txt file_z.txt`
Unstage file_z.txt from a staging area
`git reset HEAD file_z.txt`
continue commit 
`git commit -m "all files commited except file_z.txt"`


### Backtrack
The purpose of Git backtracking commands:
    discard changes in working directory
    go back to a previous commit
    unstage file from a staging area
To achieve it you type:
`git log` to view the SHAs of all previous commits.
`git reset HEAD filename` removes file changes from the staging area and reports undtaged changes after reset.

### Undo Accidentally Deleted Lines
`git checkout HEAD filename` rewind accinentally edited changes

### reset HEAD to a commit with this SHA
`git reset 844d1f7`
---

**NOTE**
What is HEAD commit? Commit you are currently on.
---

### A New Project Feature - a New Branch

At the point of creating a new branch, new branch and "master" share the exact same commit history, then you develop multiple versions of a project. 
`git branch` check branch, result shows what branch you're on.
```
      nb-nb
     /
mb-mb-mb-mb
```
New branch is a new version of the Git project: new branch contains commits from master but also own unique commits.
`git branch new_branch` creates new branch while staying on master.
`git checkout new_branch` switch to the branch, work, while master stays intact.

### git merge
Git merge executed to update master: include all the changes from the `fencing` branch to the `master` branch.
`git merge branch_name ` merge `branch_name` to `master`

`branch_name` is the giver branch(provides the changes).
`master` is a receiver branch since it accepts those changes.

---
**NOTE**

`branch_name` is the giver branch(provides the changes).

`master` is a receiver branch since it accepts those changes.

---
### Scenario Merge Two Branches
What if I decided to switch back to master then ask Git to merge the two branches
### merging the branch into master

From the terminal, merge the fencing branch into the master branch. 
`git merge branch_name`
Output says it is fast-forward. Git recognizes that `branch_name` contains the most recent commit. 
Git fast forwards `master` to be up to date with `branch_name`. 

### Merge Conflict I
Merge works fine where master has no changes since commit on `branch_name`.
`merge conflict` I 
commit on `branch_name` plus commit on `master` before you merge the two branches.
Git cannot decide for you which changes you want to keep.
### Merge Conflict II
You’ve made commits on separate branches that alter the same line in conflicting ways. The trouble begins!
In case of merge Git need help to know which version of the file to keep. 
### Fix The Merge Conflict
in the file concerned you see the changes that made it impossible to merge.
```
<<<<<<< HEAD
-Lorem ipsum dolor sit amet 
=======
-Lorem ipsum dolor sit amet such as pain.
>>>>>>> branch_name
```
### interpret marks in concerned text
Git need to have properly distinguished which version of the file to keep: on `master` or on `branch-name`. 
If I decide to keep changes according to `branch-name` I delete line as per master, all of Git's special markings including `HEAD` and `branch_name`.
Then add and commit file `git add filename.txt && git commit -m "test"`.

#### Delete Branch

In Git the branch has to be merged to the master branch at the end, after not master branch served its purpose it can be deleted:
`git branch -d branch_name`

### Merge conflict 

```
<<<<<<< 

HEAD -
 Intuitive and easy to use, providing crucial functionality 
======= 
- Intuitive and fun for use, offering the best in software 
>>>>>>> feature
 
```

While on master merge the `edits` branch into the `master` branch.
`git merge edits` as a result you got two merge conflicts: README.md and examples.md.

### Git Teamwork
A suite of collaboration tools.
I am a collaborator. Work with Bob.

### Remote is Needed
To work together the following required:
1. Complete replica of the project on your own computers.
2. Way to keep track of and review each others work.
3. access to a definitive project version.

### Git clone 
`git clone remote_location clone_name` where `remote_location` could be web adress or a filepath 
and where `clone_name` is the name you give to directory-destination for your clone.

### Remote Adress is `origin`
`git remote -v` lists Git project's remotes (`origin` by default) and its location 

### Git fetch 
What if your collaborator changed the content. If so, your clone will no longer be up-to-date.

### Me Doing Slow Fast-forwards
I cannot remember scenario, but I used to do some troubleshooting of git push origin master.
```
(venv) λ git push origin master
To https://github.com/thisAKcode/thisAKcode.github.io.git
 ! [rejected]        master -> master (non-fast-forward)

error: failed to push some refs to 'https://github.com/thisAKcode/thisAKcode.github.io.git'
hint: Updates were rejected because a pushed branch tip is behind its remote
hint: counterpart. Check out this branch and integrate the remote changes
hint: (e.g. 'git pull ...') before pushing again.

hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

### Reverting Commit
After doing `push` my pelican site died and I needed the way to get thing back as they were just before. For whathever reason I am evey now and then reverting to a specific commit based on commit id with Git.

Undo a whole commit with all changes instead of going through all the changes manually git has stuff to revert a commit, which does not even have to be the last one. "Reverting a commit means to create a new commit that undoes all changes that were made in the bad commit. Just like above, the bad commit remains there, but it no longer affects the the current master and any future commits on top of it." <https://opensource.com/article/18/6/git-reset-revert-rebase-commands>
https://git-scm.com/docs/git-revert
https://github.com/git/git/blob/master/Documentation/howto/revert-a-faulty-merge.txt

### Screw it: Practice makes perfect
I'll say it again!

### Ressources
<https://happygitwithr.com/push-rejected.html>
<https://happygitwithr.com/pull-tricky.html>
<https://ohshitgit.com/>