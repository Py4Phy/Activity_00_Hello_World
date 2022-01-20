# Activity 0 -- Hello World!
![GitHub Classroom Workflow](../../workflows/GitHub%20Classroom%20Workflow/badge.svg?branch=main) ![Points badge](../../blob/badges/.github/badges/points.svg)



In this class we will us many tools that are used in professional
software development. In particular, we will make use of the
[`git`](https://git-scm.com/) version control software (we will learn
in class how to use it) and we will use [GitHub](https://github.com/)
as a cloud storage service. Each of your homework assignments will be
stored in a _repository_ and autograded on GitHub.

## Workflow

The workflow for submitting homeworks in this class will be

1. **Follow the repository creation link** (on Canvas). The link looks
   like `https://classroom.github.com/a/FuNNyleTT3rs`. This will
   create your personal, private repository, named `hwNN-yourname`
   where _yourname_ is your GitHub username.
2. In the shell on your computer, **clone the repository to your own
   computer**, using the specific repository name:

        git clone  https://github.com/Py4Phy/activity-00-yourname.git
	  
   This creates a directory `hw00-yourname` on your computer. This is
   your *local repository*.

3. **Navigate to the local repository**

        cd activity-00-yourname

4. **Solve the problem**: read the instructions in the assignment file
   and do what you need to do, e.g., add code, create files and
   directories, etc.
   
5. **Add your changes** (can be done as often as you like):

        git add -A .
	  
6. **Commit your changes** (can be done as often as you like):

        git commit -m "updated assignment"
	  
   (You can write any message instead of "updated assignment".)
   
7. **Push your changes** to GitHub (can be done as often as you like):

        git push

   This will synchronize your repository in the cloud on GitHub with
   your local repository. When you push the changes, you **submit your
   homework**. You can push changes as often as you like until the
   submission deadline. 
   
   **Only changes in your GitHub repository until the deadline count
   for grading**.
   
8. **Check autograding**: Your homework repository on GitHub has "pull
   request" named **Feedback**. Navigate to it in your webbrowser and
   look at the **checks**. If you have a _green_ checkmark then all
   the tests passed. If you have _red_ X then some tests failed and
   you should look at the output of the tests to see what exactly
   failed. This will initially look dauting and complicated but you'll
   quickly learn what to look for.
   
   There is more help available in [Viewing autograding
   results](https://docs.github.com/en/education/manage-coursework-with-github-classroom/learn-with-github-classroom/view-autograding-results).
   
9. If you have errors then fix your submission and resubmit: `GOTO 4`

10. Else: your done

   
## Try it!

Let's do **activity-00** together: follow the instructions above and read
[assignment_00.md](assignment_00.md).

