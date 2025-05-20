---
title: "Git and GitHub from the command line"
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

A git repository \-- or \"git repo\" is a directory that is being
tracked with version control. It is the place you\'re working in and all
file edits or creations are tracked by git. The changes are stored in a
special, hidden folder called `.git`.

The *local repository* is the git repository on your computer, i.e. your
\"local\" machine. This is enough to use git on your own. The local
repository might have an address like:

: `/Users/spicedacademy/Documents/my_awesome_project/`

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



## Basic Git / GitHub Workflow

### 1. Create a Remote Repository on GitHub

When using git and GitHub, you can either:

-   create a git repository remotely on
    [github.com](https://github.com/) and then \"clone\" it to your
    local machine,

*OR*

-   create a git repository locally (with the `git init` command) and
    then upload it to a remote repository later.

We usually stick with the first approach. Here are the steps:

1.  Create an account on [GitHub](https://github.com/).
2.  Create a new **repository** there.
3.  Give the repository a name and description.
4.  Use the checkbox to create a `README.md` file (*optional*).
5.  Select the MIT-License (*optional*).
6.  Choose the *Python .gitignore* file

7.  Create a Local Working Copy of the Repository

### 2. Create a Local Working Copy of the Repository

We also want a local version of the git repository, so we have to
`clone` it *once*.

1.  Go to the starting page of your GitHub project.
2.  Click the green button **Code**.
3.  Copy the URL of your project (i.e. the remote location of the *.git*
    directory).
4.  Open a console / terminal
5.  Use `cd` to switch to the directory where you would like your
    project to be (e.g. Desktop).
6.  Enter `git clone <the-url-you-just-copied>` and hit enter.
7.  You should see a new directory with the README file.

{{% notice info "Authentication with GitHub" %}}

You cannot use your GitHub password when working with the command line.
Please setup a [personal access
token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
Once you have a token, you can enter it instead of your password when
performing Git operations over HTTPS.

{{% /notice %}}

###  3. Stage Changes Locally

Git won\'t automatically log the changes into the version control
history for you. You have to decide when you want this to happen.

1.  Make a change to your local repository. This can mean one of the
    following:
    -   Adding a new file that wasn\'t there before.
    -   Modifying an existing file.
    -   Deleting a file that was previously tracked by git.
2.  After making some kind of change, enter `git status`. If git is
    working properly, you should see the file(s) appear in red font.
3.  Add the file(s) to the staging area with
    `git add <name-of-file-you-want-to-add>`.
4.  Enter `git status`. You should now see the file(s) appear in green
    font, meaning they are now staged and ready to \"commit\".

{{% notice info "git add ." %}}

To save time, you can instead type `git add .` to add everything to the
staging area at once, rather than manually entering the name of the
file(s). Similarly, with the `git add *.py` you can add multiple python
files at once. Refer to the `linux_command_line`{.interpreted-text
role="ref"} for a refresher on this \"wildcard\" syntax.

{{% /notice %}}

### 4. Commit Changes Locally

After your changes to the local state of the git repository have been
added to the staging area, they are now ready to be officially
\"committed\" into the version control history. This creates an official
snapshot of your work.

-   Commit the changes with `git commit -m "your log message"`.
-   Enter `git status`. If everything was committed / logged into the
    version control history correctly, you should see a message:
    *nothing to commit, working tree clean*.
-   You can see the history of all commits with the `git log` command.

{{% notice info "First-Time Git Configuration Commands" %}}

Git associate your identity with every commit you make. To setup your
identity use the following commands once:

``` {.sourceCode .bash}
git config --global user.name "Your Name" 
#enter your actual name inside the quotes 

git config --global user.email "youremail@yourdomain.com"
#best if it's the email address you use for GitHub
```

{{% /notice %}}

### 5. Push Committed Changes Remotely

After having committed the changes locally, the local version of the git
repository is now \"ahead\" of its remote version. This is because you
only logged these changes locally, but the remote repository on GitHub
is not yet aware of these changes. You need to \"push\" these changes
remotely so that the remote repo is \"synchronized\" with the latest
changes.

1.  Enter `git push origin <name-of-branch>` in the console.
    -   The branch name will usually be `main` or `master`. You can
        check by running the `git branch` command to see which branch
        you are on.
    -   Branches are explained in more detail in a later section.
2.  Refresh the project website on GitHub in your browser. You should
    see your new changes / commits there.

### Summary

In summary, the main takeaway is that you internalize the following
sequence of git commands:

``` {.sourceCode .bash}
# 1. Check whether the repository is clean
git status

# 2. Add your change 
git add <name-of-file>
git status 

# 3. Commit your change
git commit -m "message about what you did"
git status

# 4. Push your changes to GitHub (remote repo)
git push origin <name-of-branch>
git status
```

**Note:** the frequent use of `git status`! This is a nice command to always
run to get a check on the status of everything going on. Also note that
that `git status` won\'t show you anything if you\'ve successfully
addressed and committed all recent changes. Instead, use `git log` to
see your changes logged into history!

{{% notice info "What and where to push and pull from" %}}
Don\'t actually type in `<name-of-file>` or `<name-of-branch>`
literally, but rather replace it with the name of the branch you would
like to push to or pull from. The default branch name is usually
`master` or `main`.
{{% /notice %}}

## Git Workflow at Spiced

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
 the \"**tensor-thyme**\" cohort, then your 2 repos are
 **tensor-thyme-student-code** and **tensor-thyme-encounter-notes**.

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

 | 

 ![](/images/spiced-git-workflow.png)

 **Some important concepts to keep in mind:**

 -   These are 2 completely separate repositories whose paths will
     never cross.
 -   In the `student-code` repository, each student will have his/her
     own branch. In this way, we will be able to see each others\' work
     on separate branches, but all still inside the same repository
     (i.e. \"folder\"). **However, the purpose is not to merge branches
     (we will learn that much later in the course)**! Rather, the idea
     is simply to have everyone\'s stuff in one place so that we don\'t
     need to manage a separate repository for each student.
 -   Don\'t get confused between branches and folders / repositories
     \-- these are entirely different concepts!
 -   The code in your local branch is only visible to you (and not
     others) until you decide to \"upload\" it (i.e. `git push`) to
     GitHub.
 -   Really make sure you understand this workflow! It is not trivial,
     but it is fundamental to everything we do at Spiced (as well as in
     your future programming career!)


## Finish Setting Up Your Working Environment

Assuming you\'ve starting setting up a working directory this week (from
the section `set up a project folder <project_folder>`{.interpreted-text
role="ref"}), the next logical step would be to clone the GitHub
repositories into your local working directory so that everything you
need for the course is in the same place on your computer.


{{% notice challenge "Push to a shared repository with multiple branches" %}}

 **In this final demo, you will learn how to submit / push your own
 code to your own git branch. This is so that each student commits his
 / her work to a separate space within the same repository, thus
 providing transparency and facilitating easier collaboration
 throughout the course.**

 -   Get an invitation to a private git repository for the entire
     course.
 -   Use `git branch <branch-name>` to create your own branch.
 -   Use `git branch` to see which branch you are on.
 -   Use `git checkout <branch-name>` to switch to your branch.
 -   Add and commit a file to your branch.
 -   Use `git push origin <branch-name>` to upload your branch to the
     remote repository.

{{% /notice %}}

### Step 1: Clone your GitHub Repositories

If you\'re already inside a directory you created on your computer (e.g.
`spiced_projects/`), this might be a good place for you to include the 2
main repositories that you\'ll use throughout the course.

``` {.sourceCode .}
git clone https://github.com/spicedacademy/dummy-dill-student-code.git
git clone https://github.com/spicedacademy/dummy-dill-encounter-notes.git
```

As explained in the `git_spiced_workflow`{.interpreted-text role="ref"}
section, the first repo (student code) is for pushing your code to your
own branch, and the second repo (encounter notes) is for pulling code
(and other materials) from the master branch.

### Step 2: Begin Organizing your Student Code Repository

Inside of your student code repository, create a week 1 subfolder for
this week\'s project:

``` {.sourceCode .bash}
cd dummy-dill-student-code/
mkdir week_01
```

**Best Practices:**

:   -   use a folder name that consists of
        **lowercase\_and\_underscores-or-hypens**.
    -   on Windows avoid uppercase especially
    -   whitespace in file and folder names is a bad idea everywhere
    -   with \'`rmdir your_folder_name`\' you can remove a folder

### Step 3: Create a Data Folder

To have a neat structure from the beginning, it would be wise to have a
sub-folder called `data/`. Again, organization is key!

``` {.sourceCode .bash}
mkdir data
```

Move all downloaded files into the data folder:

``` {.sourceCode .bash}
mv ../../*.{xlsx,csv} data/
```

**Hint:** The above command might need to modified depending on the relative path
of your project data files.


Check that it has worked with

``` {.sourceCode .bash}
ls data
```

In the end, your directory structure should look something like this:

``` {.sourceCode .text}
dummy-dill-encounter-notes/
dummy-dill-student-code/
├── .git/
├── .gitignore
└── week_01/
   ├── data/
   │   ├── continents.csv
   │   ├── gapminder_lifeexpectancy.xlsx
   │   ├── gapminder_population.xlsx
   │   └── gapminder_total_fertility.csv
   └── my_work.ipynb
```

### Step 4: Add, Commit, Push

Practice the `basic_git_workflow`{.interpreted-text role="ref"} to add,
commit, and push the changes to your branch of the shared GitHub
repository.

## Additional Resources

Git is a complicated program with tons of advanced features (you could
take a whole course just on mastering git), but the good news is that we
only need to use a few essential for the vast majority of the time.

Command  |  Description
---|---|
  `git clone <url>`         |     creates a local working copy from GitHub
  `git status`            |       shows the state of the local working copy
  `git add <file>`         |      stages changes for committing
  `git commit -m "my message"` |   stores changes in the local repository
  `git push origin master`   |    sends commits to GitHub (to master branch)
  `git pull origin master`    |   gets updates from GitHub (from masterbranch)
  `git log`              |        shows the version history on current branch
  `git branch new-branch` |       creates a new branch called `new-branch`
  `git checkout -b new-branch` |  creates a new branch and switches to it
  `git checkout master`     |     switch to the master branch
  `git branch`             |      see what branch you\'re currently on


{{% notice reading "FAQ: Git Terminology" %}}

 **A note on branches**:

 We will need to use branches in this lesson (and throughout the course
 as part of our normal workflow), but we will not be using them to
 their full extent (i.e. working on different features of a software
 project and eventually merging those changes to the \"master\"
 branch). So for now, we just need to know what they are and how to use
 them, but we will revisit them in more detail in a later part of the
 course, `git_collaboration`{.interpreted-text role="ref"}.

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


{{% notice info "Common Problems" %}}

 **I cannot push to my repository!**

 Check `git status` first and see what is going on.

 **I am stuck in a strange editor!**

 If you omit the `-m` in the command `git commit`, you will end up in
 the editor **vi**. You can leave it by pressing `ESCAPE` and `:q` and
 then hitting `ENTER`!

 **I think I messed up my repository. What should I do?**

 Use a safe fallback strategy:

 1.  Manually copy the entire folder with your repository as a backup
 2.  Use `git clone` to get a clean working copy
 3.  Try again

 **For more complicated issues**:

 1.  Great (and funny) resource: <https://ohshitgit.com/>
 2.  Ask a teacher

{{% /notice %}}

{{% notice reading "Links" %}}

 -   [Git
     Introduction](https://realpython.com/python-git-github-intro/)
 -   [Try GitHub - Online-Tutorial](https://try.github.io/)
 -   [Adding SSH keys to your GitHub
     account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)
 -   [Splitting a Subfolder into a new
     Repo](https://docs.github.com/en/github/using-git/splitting-a-subfolder-out-into-a-new-repository)
{{% /notice %}}


{{% notice info "Reflection Questions" %}}

 -   Why is it better to use git instead of GoogleDrive or Dropbox?
 -   What benefits does git provide in a one-person project?
 -   `git push` does not work. What are possible reasons?
 -   What files should not be added to a git repo?
 -   How can you find out whether you are in a git folder?
 -   In the beginning of the course, why do we push our work to a
     single repository that contains multiple branches?

{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Kristian Rother" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}