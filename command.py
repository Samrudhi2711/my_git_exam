Q.1 Git Repository – Step by Step Commands

[10 Marks]

Step 1: Create a new directory and move into it
mkdir my_git_exam
cd my_git_exam

Step 2: Initialize Git repository
git init


👉 This creates a local Git repository.

Step 3: Create index.html file
nano index.html


Add sample content:

<html>
<body>
<h1>Welcome to Git Exam</h1>
</body>
</html>


Save and exit.

Step 4: Add file to staging area
git add index.html

Step 5: Commit index.html
git commit -m "Added index.html file"

Step 6: Create a new branch named exam
git branch exam

Step 7: Switch to exam branch
git checkout exam


(OR single command)

git checkout -b exam

Step 8: Create exam.html file in exam branch
nano exam.html


Add content:

<html>
<body>
<h1>Exam Branch File</h1>
</body>
</html>


Save and exit.

Step 9: Add and commit exam.html
git add exam.html
git commit -m "Added exam.html in exam branch"

Step 10: Switch back to main (or master) branch

Check branch name:

git branch


Switch accordingly:

git checkout main


OR

git checkout master

Step 11: Merge exam branch with main/master
git merge exam

Step 12: Verify merge
git log --oneline


You will see commits from both branches.






2️⃣ Check branches (main & exam exist)
git branch

Example output:
* main
  exam


✅ This confirms:

main (or master) branch exists

exam branch exists

* shows current branch





4️⃣ Check that exam.html exists in main branch

Make sure you are on main branch:

git checkout main


Now list files:

ls

Output:
exam.html  index.html





🔹 Step 1: Create a repository on GitHub (website)

Go to 👉 https://github.com

Login to your account

Click “+” (top right) → New repository

Repository name:

my_git_exam


❗ Do NOT check:

Add README

Add .gitignore

Click Create repository

👉 GitHub will show commands like “…or push an existing repository”

🔹 Step 2: Connect local repo to GitHub (REMOTE)

In your terminal (inside your project folder):

git remote add origin https://github.com/YOUR_USERNAME/my_git_exam.git


(Check remote)

git remote -v

🔹 Step 3: Push main branch to GitHub
git push -u origin main


OR (if branch name is master):

git push -u origin master


✅ Now your index.html is on GitHub

🔹 Step 4: Push exam branch to GitHub
git push origin exam


✅ Now exam branch is also visible on GitHub
