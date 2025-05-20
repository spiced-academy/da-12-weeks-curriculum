---
title: "Git and GitHub"
weight: 15
---

![](/images/journal.jpg)

*Photo by Colton Sturgeon on Unsplash*


{{% notice warmup "Warmer: Why do we need git?" %}}


 **Read the story:**

 -   Ada writes a program `hello.py`
 -   Some time later, she modifies it and stores the changes in a file `hello2.py`
 -   She sends the file to Bob by email who also edits the code and
     sends back `hello_new_version.py`
 -   In the meantime, Ada has improved her version to `hello3.py`
 -   She goes through the code line by line to include Bobs changes, resulting 
     in `hello3_with_bob.py`
 -   Later, Bob finds out that the original `hello.py` was not working properly.
 -   Ada and Bob sit together and try to find out what they need to
     fix.

 **What problems do you see with the approach Ada and Bob took?**

{{% /notice %}}

What is Version Control?
========================

**Version Control stores changes in program code or other files over
time.**

Using a Version Control System helps you to:

-   keep backups of your code
-   jump back to earlier versions
-   edit the same program on multiple computers
-   collaborate with other people on a project
-   publish your project online

Version control is the first step towards professional development.

Local Repositories
------------------

A git repository - or \"git repo\" - is a directory that is being
tracked with version control. It is the place you\'re working in and all
file edits or creations are tracked by git. The changes are stored in a
special, hidden folder called `.git`.

The *local repository* is the git repository on your computer, i.e. your
\"local\" machine. This is enough to use git on your own. The local
repository might have an address like:

: `/Users/spicedacademy/Documents/GitHub/my_awesome_project/`

The purpose of the local repository is to manage the version control of
your project on your local, physical computer, where you are usually
doing work. With git you can locally track and log all changes to files:

-   adding new files
-   editing existing files
-   deleting files

Remote Repositories
-------------------

Usually the local repository has a *remote repository* counterpart,
which is physically located on a different machine, i.e. \"in the
cloud.\" This remote repository is usually hosted on a website like
[github.com](https://github.com/).

The remote repository might have an address like this:

:   `https://github.com/spicedacademy/my_awesome_project/`

The name of the project folder usually is named the same both locally
and remotely.

The idea is then to upload (\"`push`\") all the changes to the remote
repository so that it\'s easily accessible and editable to multiple
people. This is useful because multiple people might be working on a
project, or the remote repository is simply useful as a backup in case
you lose your work locally.

Here is what the process looks like:

![](/images/repository.png)

Concept  |  Description
---|---|
  git      |      most popular version control system today
  repository |    place where the history of your project is stored
  working copy |  the files you actually work with
  staging area |  changes scheduled, but not yet stored in the repository
  `.git`    |     directory in which changes to a local repository are stored
  GitHub     |    website that stores repositories (i.e. \"in the cloud\")



## Git and Github in VS Code

There are different ways to sync with your local repositories with ones in the cloud like **github**. One way is via plugin that is available in VS Code. In the following **Milestone** boxes the installation instructions for Windows, Mac and Linux can be found. Please skip to the correct OS and follow the instructions.


{{< notice challenge "Git Installation" >}}
<br>
Choose your Operating System:

{{% expand "Windows" %}}

1. First open VS Code. 

2. In order to add source control to VS Code click on the icon with 3 circles connected by lines:

![git](/images/git_win_1.png)

3. The Windows operating system does not come with Git. To continue to the download site click on the `Open` button, which will forward to [https://git-scm.com/download/win](https://git-scm.com/download/win).

![git](/images/git_win_2.png)

4. Download the appropriate installer and start the installation process. Once you are at the **Choosing the default editor used by Git** stop!

![git](/images/git_win_3.png)

5. Vim is a editor used by computer scientists and is not user friendly. Please change it to use `vs code` as seen below:

![git](/images/git_win_4.png)

6. Finish the installation process and then proceed to the configuration instructions. 

{{% /expand %}}


{{% expand "Mac" %}}

1. First open VS Code. 

2. In order to add source control to VS Code click on the icon with 3 circles connected by lines:

![git](/images/git_mac_1.png)

3. Even though the Mac operating system associates with Git - it still needs to be installed. To continue to the download site click on the `Open` button, which will forward to [https://git-scm.com/download/mac](https://git-scm.com/download/mac).

![git](/images/git_mac_2.png)

4. There are multiple ways to install git on Mac OS. One way is to use homebrew. Homebrew helps to install "stuff" on your Mac or Linux systems. To install [homebrew](https://brew.sh) copy and execute this line in a terminal. 
(Mac OS Terminal from Launchpad >> Other can also be used.)

```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
``` 

![git](/images/git_mac_3.png)

5. The installation will pause and ask to press ENTER/RETURN to proceed. Press ENTER.

![git](/images/git_mac_4.png)

6. At the of the homebrew installation a terminal message will mention a WARNING in red that /opt/homebrew/bin is not in your PATH. Follow the instructions under the "Next steps" in order to add homebrew to PATH. 
   
![git](/images/git_mac_5.png)

7. To install Git with homebrew execute this line in a terminal:

```bash
    brew install git
``` 

{{% /expand %}}

{{% expand "Linux" %}}

1. First open VS Code. 

2. In order to add source control to VS Code click on the icon with 3 circles connected by lines:

![git](/images/git_win_1.png)

3. To continue to the download site click on the `Open` button, which will forward to [https://git-scm.com/download/linux](https://git-scm.com/download/linux).
   
4. To install Git execute this line in a terminal:

```bash
    sudo apt-get install git
``` 

{{% /expand %}}

{{< /notice >}}


### Configure Github locally


In order for your local git repository to connect to github your user name and email must be configured via the command line. Open a terminal in VS Code and enter the following commands to configure github:

```bash
    git config --global user.email "you@example.com"

    git config --global user.name "Your Name"
``` 

See below for an example in the terminal:

![git](/images/git_configure.png)


## Github Workflow: **encounter-notes**

There will be two github repos used in the course. **encounter-notes** is for the instructors to share notebooks, data, files and more with the cohort. In this repo students will **only** pull (download) the files. The other github repos will be discussed below.

In order for this file sharing to be initiated first the online repo needs to be *cloned* locally. Then anytime the instructor pushes (uploads) files the student can then pull them in order to sync the local and online repos. Students are alerted via slack anytime a new file is pushed by instructors. 

**Note:** Keep in mind after the repo has been set up locally **only** Step 3. will be necessary. 

### Clone **encounter-notes** repo

1. Cloning is normally **only** done once for each repo that already exists in the cloud. Now that git has been installed and configured we can clone the necessary repos. First click on `Clone Git Repository...`

2. Enter the **encounter-notes** URL the cohort your instructor has given to you into the text bar at the top of VS Code. 

![clone](/images/git_clone.PNG)

3. After pressing enter select your computers **desktop** as the repository destination.

4. At this point a pop up window may appear, if so enter your GitHub login and password. Once the authentication has been checked the following window should appear:

![clone](/images/git_win_8.png)

5. Once the repo has been cloned open it using `Open Folder...` under the `File` option to have an overview of the folders and files in the repo:

![clone](/images/git_clone_3.png)


### Sync local files with new online files

When an instructor pushes new files to **encounter-notes** you should receive an alert in the **Github** slack channel:

![](/images/slack_alert.png)

When the channel is clicked on the file and any accompanying message can be viewed: 

![](/images/slack_message.png)

In order to pull these new files navigate to the source control menu in VS Code, click on the 3 dots `...` next to the repository name that you want to update. At this point scroll down to **Pull** and click on that option. 

![git pull](/images/git_pull_1.png)

Now the local and online repos have been synced and have the same files in them. Do not work on these files while they are in the **encounter-notes** folder! Only work on copies of them in a **working-folder**. Please see the next workflow for the working folder (or repo). 

## Workflow: **working-folder**

The **encounter-notes** repo should be a one-way road. Files should only be **pulled**. If you want to use any files for coding then please copy them to a new folder called **cohort-name-working-folder**

Create this folder on your desktop as you did for **encounter-notes**:

![](/images/working.png)

Now any files are to be used and executed should be copied to this folder and worked on there.

## Workflow: **student-code** repo

Thus far there are two folders **encounter-notes** for instructors to share files and **working-folder** for working on these and other files locally. The last repo is **student-code**. Here finished exercises, milestones and projects will be uploaded to a personal branch in order for instructors to be able to see what work you have accomplished. 

You should push to this repo everytime you finished an exercise or project milestone. The following steps will first help set up the repo then take you through the daily workflow used to push your work. 

###  Clone **student-code** repo

First follow steps 1-5 in the *Clone **encounter-notes*** repo section above. Once the `student-code` folder is open in VS Code create your own branch by following these steps:

1. Open source control on the left. Next to the words `SOURCE CONTROL` there are 3 icons and then `...` Click on  `...` and scroll down to `Branch` and then on to `Create Branch`

![](/images/git_win_9.png)

Unlike the **encounter-notes** repo in **student-code** you will push code to GitHub. In order to allow every student to be able to push their code to a personal repo, each student will create a branch. 

2. Give the branch your first name or nick name so your instructor can recognize who is who. 

![](/images/git_clone_4.png)


3. Once the branch has been created, publish the branch to github by clicking on the **Publish branch**. This will ensure that there is access to the repo online as well as locally. 

![](/images/git_win_10.png)

As you can see in the bottom left corner of VS Code the **Current branch** name should no longer be master or main but the name you gave it (in the example `samuel`). In **student-code** you should **ONLY** work on the branch you created. 

![](/images/git_branch_1.png)

You can also visit the `student-code` github in your browser to see the branch online.

![](/images/git_branch_online.png)



### Adding files to **student-code**

Adding work to your branch should be part of your daily routine during the bootcamp. 

Once you have finished working on some code in your **working-folder**, copy the file(s) to the **student-code** repo. 

Git will recognize the changes in the repository and list it in the source control window. In the example one `README.md` file was added to the repo. 

![](/images/git_win_11.png)


1. Click on the file you would like to stage and additionally click on the `+` symbol to stage the change. 

![](/images/git_win_12.png)

2. Once the file(s) has been staged then commit the change(s). Before committing add a message to give some insight into the changes that are being committed. 

![](/images/git_win_13.png)


3. Once the change(s) have been committed then push (sync) the data online by clicking on `sync changes`. 

![](/images/git_win_14.png)

4. You then be asked to confirm that you want to complete the sync. Feel free to push `OK, Don't Show Again` or only `OK` until you are comfortable with the workflow

![](/images/git_win_16.png)

After these steps the local and online repos should be synced and your instructors now have access to your code and look over it to review. **Please push your work on a daily basis throughout the bootcamp. You code will be checked to ensure you are meeting graduation requirements.**

If everything has been set up correctly you should have the folder structure below on your computer. Keep in mind `thymestamps` should be replaced by the name of your cohort:

![](/images/19_folders.png)


## Git Workflow Overview at Spiced

 **WARNING:** Git is not something that can be learned in a single lesson; rather,
 it will become more intuitive to use over time through lots of (daily)
 practice!

 In order for git commands to start becoming second nature to you, we
 (both teachers and students) will be using git on a daily basis to
 share code and collaborate with one another. This means **basic git
 knowledge is a pre-requisite**, as you will not be able to get the
 latest lesson notes or submit your own work without it!

 So, every day, after the teachers finish an \"encounter\" (i.e.
 lesson), they will share the code on GitHub for students to have as
 reference. Likewise, students will frequently commit and push their
 own code to GitHub so that:

 -   teachers can see students\' progress,
 -   students can share code snippets and ideas with each other,
 -   teachers can help debug students\' code a lot easier / faster,
 -   students get in the habit of committing frequently, thereby
     building up a nice GitHub portfolio.

 **So how exactly will our day-to-day git (and Github) workflow look
 like to facilitate this?**

 For the first several weeks of the bootcamp, there will be **2 GitHub
 repositories** that are relevant to you:

 1.  `<cohort-name>-student-code`, and
 2.  `<cohort-name>-encounter-notes`.

 To be clear, the above syntax inside `<` *angled brackets* `>` means
 \"insert your actual cohort name here\". So, for example, if you are
 the \"**thymestamp**\" cohort, then your 2 repos are
 **thymestamp-student-code** and **thymestamp-encounter-notes**.

 **What each repository is for:**   

1\. The first repository, `<cohort-name>-student-code`, is for **students
to push their own code to GitHub each week**. In this repository, you
will **push to your own branch**.

2\. The second repository, `<cohort-name>-encounter-notes`, is used
exclusively as a repository **for the teacher to share code / notes
after each \"encounter\" (i.e. lesson)**. In this repository, you will
**pull from the master branch**.

 

 **Here is a diagram to help illustrate the GitHub workflow we use at
 Spiced:**

 ![](/images/pull-create-push.png)

 **Some important concepts to keep in mind:**

 -   These are 2 completely separate repositories whose paths will
     never cross.
 -   In the `student-code` repository, each student will have his/her
     own branch. In this way, we will be able to see each others\' work
     on separate branches, but all still inside the same repository
     (i.e. \"folder\"). **However, the purpose is not to merge branches**! 
     Rather, the idea
     is simply to have everyone\'s stuff in one place so that we don\'t
     need to manage a separate repository for each student.
 -   Don\'t get confused between branches and folders / repositories
     \-- these are entirely different concepts!
 -   The code in your local branch is only visible to you (and not
     others) until you decide to \"upload\" it (i.e. `git push`) to
     GitHub.
 -   The code in your `working-folder` is not connected to github and therefore will not be visible to anyone unless you copy it to `student-code`and push it
 -   Really make sure you understand this workflow! It is not trivial,
     but it is fundamental to everything we do at Spiced (as well as in
     your future programming career!)

{{% notice reading "FAQ: Git Terminology" %}}

 **A note on branches**:

 We will need to use branches in this lesson (and throughout the course
 as part of our normal workflow), but we will not be using them to
 their full extent (i.e. working on different features of a software
 project and eventually merging those changes to the \"master\"
 branch). So for now, we just need to know what they are and how to use
 them.

 Nonetheless, here are some definitions to help orient yourself better:

 **What is a branch?**:

 In non-technical terms, you can think of a branch as a version of the
 current state / reality of everything inside the repository. If you
 create a new branch (e.g. `my-branch`) based off an existing branch
 (e.g. `master`), then what you are essentially doing is creating a
 parallel, alternate \"universe\" / version of your repository\'s
 contents.

 Now of course, upon the creation of the branch, `my-branch` is
 identical in content to `master`, but the key here is that `my-branch`
 is now isolated from what goes on in `master`. In other words, what
 this means is that if you continue working and committing changes to
 `my-branch`, this will only affect the version history of that branch
 and not the master branch. This is nice, because if you\'re working in
 software development, and you\'re working on some new feature of the
 project, you can run and test out your new code in an isolated,
 separate environment and not affect the \"master\" version (which is
 most likely deployed in production).

 Eventually, the goal is to \"merge\" the git history of `my-branch`
 into the master branch. But we don\'t need to concern ourselves with
 this concept just yet.

 **What is \"master\"?**:

 The \"master\" branch is the default branch that comes with a cloned
 repo from GitHub. If you are the only person working on a project
 using git, odds are that you will only be working on with the master
 branch.

 **What is \"main\"?**:

 As of 2020, GitHub replaced their default branch name to **main**.
 This means that if you create a new remote repository on
 [github.com](https://github.com/), your primary default branch will be
 named differently. Apart from the name, however, it is otherwise the
 same thing as the **master** branch that you might see elsewhere.

 **What is \"origin\"?**:

 `origin` (as you probably observed from a few commands) is an alias /
 nickname that refers to the location (i.e. URL) of the remote
 repository (e.g. on GitHub) that your local repository is connected
 to. The use of the word \"origin\" is just convention; just like
 \"master\", it\'s the default terminology. You can of course change
 this, but it\'s probably better not to.

 Rather than constantly refer to the remote repository by it\'s full,
 long URL (e.g. <https://github.com/spicedacademy/bash_tutorial.git>),
 we just refer to this URL as `origin` for short.

{{% /notice %}}


{{% notice reading "Links" %}}

 -   [Getting Started with GitHub Desktop](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/overview/getting-started-with-github-desktop) 
 -   [Git
     Introduction](https://realpython.com/python-git-github-intro/)
 -   [Try GitHub - Online-Tutorial](https://try.github.io/)
{{% /notice %}}


{{% notice info "Reflection Questions" %}}

 -   Why is it better to use git instead of GoogleDrive or Dropbox?
 -   What benefits does git provide in a one-person project
 -   What files should not be added to a git repo?
 -   In the beginning of the course, why do we push our work to a
     single repository that contains multiple branches?

{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Kristian Rother" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}