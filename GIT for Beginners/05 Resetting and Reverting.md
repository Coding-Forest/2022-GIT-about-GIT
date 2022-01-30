# 05 Resetting and Reverting

<br>

used to undo the changes.

<br>

### Syntax

- `git revert <hash>`
- `git revert HEAD~0`
- `git reset --soft HEAD~1`
  - resetting the commit with a soft flag allows for the access to the changes that were made by that commit.

<br>

## Hands-on Exercise - Resetting and Reverting

- `git log --name-only`

        commit 6d5f456273cec6a7334d947468923cf114f23fb5 (HEAD -> master)
        Author: sarah <sarah@example.com>
        Date:   Sat Jan 29 09:27:05 2022 +0000

            Add author info to stories

        kiwi-and-takahe.txt
        willow-and-lake.txt
        Kakapo-and-Kea.txt
        pine-and-sawtooth.txt
        the-bamboos.txt

        commit 2a21ee4778c4e1e52eafbf09c8d69a95e782183b
        Author: sarah <sarah@example.com>
        Date:   Sat Jan 29 09:26:51 2022 +0000

            Add stories

        kiwi-and-takahe.txt
        willow-and-lake.txt
        Kakapo-and-Kea.txt
        pine-and-sawtooth.txt
        the-bamboos.txt


<br>
<br>

- `git revert HEAD~0`

        evert "Add author info to stories"

        This reverts commit 6d5f...3fb5.

        # Please enter the commit message for your changes. Lines starting
        # with '#' will be ignored, and an empty message aborts the commit.
        #
        # On branch master
        # Changes to be committed:
        #       modified:   kiwi-and-takahe.txt
        #       modified:   willow-and-lake.txt
        #       modified:   Kakapo-and-Kea.txt
        #       modified:   pine-and-sawtooth.txt
        #       modified:   the-bamboos.txt
        #

<br>
<br>

- `git revert <commit id>`

        git revert 2a21ee4778c4e1e52eafbf09c8d69a95e782183b
        error: your local changes would be overwritten by revert.
        hint: commit your changes or stash them to proceed.
        fatal: revert failed

<br>

- `git reset --soft HEAD~1`: revert the last commit but retain the unfinished changes. The last commit must not be part of the GIT history.
  - `--hard`: completely removes the commits from history. 

        git reset --hard HEAD~3
        HEAD is now at 9a7f71a Finish willow-and-lake story

<br>
<br>

## Edit commit history

- `git commit --amend`: Edit the last commit history

Before

    git log --name-only
    commit f3c88e~ (HEAD -> main)
    Author: Coding Forest
    Date:   Sun Jan 30 13:04:04 2022 +0900

        Completed Ansible for beginners

        Added badge image

        Updated README

        Updated README

    Ansible for the Absolute Beginners/00 Setup.md
    README.md
    images/Badge - Ansible for Beginners.png


<br>

After 

    git log --name-only
    
    commit 1b9569~ (HEAD -> main)
    Author: Coding Forest
    Date:   Sun Jan 30 13:04:04 2022 +0900

        Completed Ansible for beginners

    Ansible for the Absolute Beginners/00 Setup.md
    README.md
    images/Badge - Ansible for Beginners.png
 

<br>
<br>
<br>

## `stash`

<br>

- `git stash`: stash a working file from the working area
- `git stash pop`: bring back to the working area
- `git stash list`: show list of stashed files
- `git stash show stash@{1}`

<br>
<br>

## Hands-on Exercise - `stash`

<br>

**Scenario 1.**

There is an urgent task that has to be addressed immediately. Stash your work in hands and move over to the master branch to deal with it.

    git stash
    Saved working directory and index state WIP on willow-and-lake: 267573a Added the lion and mouse story


    git stash list
    stash@{0}: WIP on willow-and-lake: 267573a Added the willow-and-lake story

<br>

**Scenario 2.**

There is another branch that you stashed away multiple files. Now let's go handle them.

    git checkout bamboo-forest

    git stash list

    stash@{0}: WIP on bamboo-seedlings-task: 8b3343c all pending changes      <--- pushed latest to the stash
    stash@{1}: WIP on bamboo-seedlings-task: 8b3343c all pending changes
    stash@{2}: WIP on bamboo-seedlings-task: 8b3343c all pending changes

Check out which files are stashed at which `stash`.

    git stash show stash@{0}
       story3.txt | 1 +
       1 file changed, 1 insertion(+)
    

    git stash show stash@{1}
       story2.txt | 1 +
       1 file changed, 1 insertion(+)
    

    stash show stash@{2}
       story1.txt | 1 +
       1 file changed, 1 insertion(+)


<br>
<br>

## Reflog 

- `git reflog`: logs every single command used on `git`. shows state of your repository. 
- `git log`: shows the log of commits only.
