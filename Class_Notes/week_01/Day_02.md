[comment]: render
# Day 2 Notes


### Git and GitHub Process

Before we start we need some basic terminology for git and GitHub. The first word is a *repository*. A repository is a folder
that contains files and subfolders that have files that you wish to track the changes in. Repositories can be stored on 
your local machine (a **local or remote repository (repo)**) or on a computer in the cloud at a site like GitHub (an **origin** repository). 


Once you have a repository you will tell the git program which files you want to track. This is called adding the file
to the repository. Once added, git will track the changes you make in the file. 

Many people can have the same repository locally on their computer, but their versions may be different. Git has ways of checking
to see if there is a **conflict** between different versions of the repository once people look to **merge** their versions. 


#### When making a change

Once a change is complete, you should **commit** your changes to repository. On PyCharm you do this by clicking on the 
green check mark then adding a message about what you did and hitting the button labeled commit. 

##### Make a new branch

Sometimes you want to make changes free of other's changes. You want to work on your own area, or you want to keep a version
of what you have done intact without. This is most easily done by making a new branch. Branches can be made using the PyCharm 
Git menu. Branches allow you have several versions of the same code on your machine. When you check out a new branch Git 
will update the tracked files to be in alignment with the most recent version of that branch.

##### Make commits in that branch

You make commits in a branch the way you always make commits. You click on the checkmark or goto Git/Commit then type a 
short message about the commit 

##### Merging a branch

When you are done with the changes in a branch you can merge the changes back into another branch. This is done by
checking out the main branch and then clicking on the green checkmark and selecting the branch you want to merge.

##### Make a pull-request

Once you have made changes in a branch that you want to tell other people that are working on the project that you have 
completed an important task. To do this you can create a pull request. 

##### Cloning

Cloning is a way of copying the project repository on to your own device.


#### Git Glossary

* **repository** - The highest level of a GitHub project.
* **branch** - A branch is a version of the project that can be updated, or it may be the main branch which contains
all the completed changes.
* **commit** - A step in the completion of the project. This is a moment in the development of your project where you
have completed a significant step (sort of like saving).
* **pull-request** - An announcement that an updated version of the code has been completed and needs to be incorporated
into the main branch.
* **clone** - making a copy of a remote repository on your own computer.

#### Practice

1. Make a new project and clone the repo at: https://github.com/CS570/Text_Integrator_Test
2. Create a new branch using your name
3. In the folder ```Text_Snippets``` create a file using your name and use the markdown ending, ".md" for the name. 
   Simply put make a file called "Jane_Doe.md"
4. In that file write what you like about robotics, and sign your name, and add a few line spaces at the end of the file.
5. Commit that change
6. Make a pull-request to the main branch.

#### Homework

Your homework is to sign up for GitHub Classroom and to do the assignment called 
```CS570-Assignment-Branching```. This is a simple assignment that will help you get used to the process 
of making branches and commits.



