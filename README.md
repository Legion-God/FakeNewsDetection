# FakeNewsDetection

![Test workflow](https://github.com/Legion-God/FakeNewsDetection/actions/workflows/tests.yml/badge.svg)
[![Deployment workflow](https://github.com/Legion-God/FakeNewsDetection/actions/workflows/deploy.yml/badge.svg)](https://fake-news0.herokuapp.com/)
![GitHub](https://img.shields.io/github/license/Legion-God/FakeNewsDetection?color=informational)

Fake News detection using Passive Aggressive classifier.

## Contents
1. [Environment Set Up](#setting-up-development-environment)
2. [Coding Workflow](#coding-workflow)
3. [How to run website locally](#running-website)
4. [Fake News References](#fake-news-references)

## Setting up development environment.

### Use pycharm to speed up the environment setup
1. Create a new project from **VCS** and paste this url `https://github.com/Legion-God/FakeNewsDetection.git`
2. If prompted for setting up virtualenv, agree and wait for the setup to complete. After completion open the terminal
in the pycharm often found in bottom panel named as **Terminal** and if **(venv)** appears then everything is set up
   correctly.
   
3. You are done setting up the environment.


## Coding Workflow
NOTE: Always push to a feature branch NEVER directly push to **main** branch.

1. Create or select issue you want to work on, new issue can be easily created by going to issues tab in Github.
2. Create a new feature branch on your local machine of format <short_issue_name><issue_number>,
ex: if someone wants to work on feature frontend which is issue number 9, then branch name would be `frontend9`
   
3. To create a new feature branch on your local machine, run `git checkout -b <branch_name>`
-b flag creates a new branch and checkout command switches to that branch. run `git status` to check your current branch.
   
4. Before working on any issue pull changes from `main` remote branch into the current feature branch,
if you are working on issue for long time, commit any changes before pulling from remote branch.
   `git pull origin main` this pulls code from `main` remote branch and merges into your new feature branch.
   
5. Write some code about feature.

6. `git status` to check which files are changed, `git add .` to stage the changed files for committing.
`git commit -m "a very helpful commit message describing solution for the issue/feature."`
   
7. `git push origin <branch_name>` WARNING: don't write `main` in branch_name, write the name of feature branch you
worked on your local machine.
   
8. Open Github and you will see an option to create a Pull Request(PR), create a PR and then leave for review. 
Someone else will do a code-review and merge it to `main`. If tests failed when creating a PR request close it and 
   make new PR with changes.
   

## Running Website

The CI/CD pipeline is set up which will run the tests and deploy the website if tests pass automatically.
The tests for flask app are basic tests, improve them as you go.

### Running a Flask app
```bash
$ flask run
```

## Fake News References
1. Using [scikit-learn](https://medium.com/swlh/detecting-fake-news-with-python-and-machine-learning-f78421d29a06)
2. Alter Using [scikit-learn](https://towardsdatascience.com/detecting-fake-political-news-online-a571745f73dd)
   
3. Scikit Learn Passive-Aggressive Classifier [Help Page](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html#sklearn.linear_model.PassiveAggressiveClassifier)
4. Passive-Aggressive Classifier Implementation in [Scikit Learn](https://github.com/scikit-learn/scikit-learn/blob/95119c13a/sklearn/linear_model/_passive_aggressive.py#L10)
5. Research Paper Implementing the [Classifier](https://jmlr.csail.mit.edu/papers/volume7/crammer06a/crammer06a.pdf)