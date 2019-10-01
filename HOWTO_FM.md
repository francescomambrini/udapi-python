# How To
This is a forked project. Here some Git commands to update the repo and push the changes.

## Keep the forked repo in sync

Forked repos are not automatically in sync: if changes are made into the original `udapi-python` 
repo, they have to be pulled manually. [Here](https://www.youtube.com/watch?v=-zvHQXnBO6c)'s how 
to do it:

* first, check if you have already set the `upstream` remote: `git remote -v`
* if not, then configure it: `git remote add upstream https://github.com/udapi/udapi-python.git`
* fetch changes from the upstream: `git fetch upstream`
* new commits are saved in a branch called `upstream/master`; if we want to include them in our 
master branch we must `merge` them: `git merge upstream/master`
* now we can also push them to our GitHub repo: `git push origin master` 
