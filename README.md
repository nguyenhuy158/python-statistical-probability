`git config --global user.name ""`
`git config --global user.email ""`

---
# --> check <--
`git config --list`

---

# 1/ create a local repo
--> `git init`
link two repo
--> git remote add origin https:\\...
# 2/
--> `git clone https:\\...  "directory"`
# 3/
--> `git add "file"`
# 4/
--> `git commit -m "msg"`
change commit
--> `git commit --amend -m "new msg"`
# 5/
--> `git push origin master`
# 6/
--> `git status`
# 7/
--> `git diff (so sanh two commit)`
# 8/
--> `git log --oneline`
# 9/
--> `git reset "file"`
# 10/
--> `git fetch <-- run first`
--> `git pull <== run after git fetch`