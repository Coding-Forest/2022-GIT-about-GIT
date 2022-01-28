# GIT branches

<br>

- A pointer to a specific commit in git
- Allows you to branch out your current copy of your code to share with friends and colleagues. 

- `master`: the default branch of a git repository

<br>

## Create a new branch

- Create a new branch

        git branch forest

- Switch to an existing branch

        git checkout forest

- Create a new branch and switch to it

        git checkout -b forest
        Switched to a new branch 'forest'

- Delete a branch

        git branch -d forest

- List all branches

        git branch

<br>

- `HEAD`: your current location in the repository


<br>

## Hands-on Exercise 

- `git log --decorate`: you can check from which branch to which branch commits are made.

        commit 187840...0b02be49 (HEAD -> master)
        Author: sarah <sarah@example.com>
        Date:   Fri Jan 28 09:05:48 2022 +0000

            Added the lion and mouse story

- Create and switch to a new `branch`

        git checkout -b story/willow-and-lake
        Switched to a new branch 'story/willow-and-lake'

- check `git log`: see how the HEAD always points to the last commit on the currently checked-out branch.


        git log

        commit 471ad6...78868f8 (HEAD -> master, story/willow-and-lake, animals)    <--- check this line.
        Author: forest <coding@forest.com>
        Date:   Fri Jan 28 16:19:11 2022 +0900

            added timon and pumba lyrics

        commit 88d9a67...e1bad9
        Author: forest <coding@forest.com>
        Date:   Fri Jan 28 10:51:17 2022 +0900

            added two stories

- Create a file and commit it in the new `branch`.

        git checkout story/willow-and-lake

        Switched to branch 'story/willow-and-lake'


        forest (story/willow-and-lake)$  vi willow-and-lake.txt

        forest (story/willow-and-lake)$  git add willow-and-lake.txt
        forest (story/willow-and-lake)$  git commit -am 'added story willow-and-lake'

        [story/willow-and-lake 97345c8] added story willow-and-lake
            2 files changed, 5 insertions(+)
            create mode 100644 .gitignore
            create mode 100644 willow-and-lake.txt

- Check `status`

        git status

        On branch master
            Changes not staged for commit:
            (use "git add/rm <file>..." to update what will be committed)
            (use "git restore <file>..." to discard changes in working directory)
                deleted:    forest_story.txt

        Untracked files:
            (use "git add <file>..." to include in what will be committed)
                forest_story
                personal_notes.txt
                willow_story.txt

        no changes added to commit (use "git add" and/or "git commit -a")

- Commit updates


        git add .gitignore willow_story.txt

        git commit willow_story.txt -m "updated willow_story"

        [master 1fbf5df] updated willow_story
            1 file changed, 3 insertions(+)
            create mode 100644 willow_story.txt


        git log

        commit 1fbf5d.....48bb (HEAD -> master)
        Author: forest <coding@forest.com>
        Date:   Fri Jan 28 19:08:04 2022 +0900

            updated willow_story

<br>

- Check all branches and where you are.

        git branch
          animals
          master
        * story/willow-and-lake


        git checkout master


        git branch
          animals
        * master
          story/willow-and-lake

<br>

- `git log --graph --decorate`

    * commit 1fbf5d...248bb (HEAD -> master)
    | Author: forest <coding@forest.com>
    | Date:   Fri Jan 28 19:08:04 2022 +0900
    | 
    |     updated willow_story
    | 
    * commit 471ad6...868f8 (animals)
    | Author: forest <coding@forest.com>
    | Date:   Fri Jan 28 16:19:11 2022 +0900
    | 
    |     added timon and pumba lyrics
    | 
    * commit 88d9a6...1bad9
    Author: forest <coding@forest.com>
    Date:   Fri Jan 28 10:51:17 2022 +0900
    
        added two stories