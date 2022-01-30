# 04 Rebasing

<br>

- Coping commits from one branch to another. These new copied commits are a commit themselves, hence the hashes update. 
- it is important to commit everything before rebasing the desired branch on top of another branch.


<br>

### Rebasing preps

- `git pull origin master`: pull from the origin for latest updates by team mates + collaborators

        git checkout story/hare-and-tortoise
        A       willow_story.txt
        M       story-index.txt
        A       birch_story.txt


- `git rebase master`: update master branch

        error: cannot rebase: Your index contains uncommitted changes.
        error: Please commit or stash them.


- `git status`

        On branch story/willow-and-late
        Changes to be committed:
            (use "git restore --staged <file>..." to unstage)
                new file:   willow_story.txt
                modified:   story-index.txt
                new file:   birch_story.txt


- `git commit -m 'commit for rebase'`  

        [story/willow-and-lake 9c7ade0] commit for rebase
           3 files changed, 42 insertions(+)
           create mode 100644 willow_story.txt
           create mode 100644 birch_story.txt

<br>

Finally, `rebase`.

- `git rebase master`

    Current branch story/hare-and-tortoise is up to date.

<br>

## Interactive rebasing

- `git rebase -i HEAD~<NUMBER>`: rebase last <number> of commits
  - `-i`: interactive
  - `git` will show you the rebase file in text editor. 
    - `squash`: melt multiple commits into one. 


`git rebase -3 HEAD~4`: rebase last 3 commits

        pick 9c7ade0 commit for rebase
        squash 1247ab3 Update hare-and-tortoise          <--- modified from pick to squash
        squash 34f68e0 Finish hare-and-tortoise          <--- modified from pick to squash


        # Rebase a6e7265..34f68e0 onto a6e7265 (3 commands)
        #
        # Commands:
        # p, pick <commit> = use commit
        # r, reword <commit> = use commit, but edit the commit message
        # e, edit <commit> = use commit, but stop for amending
        # s, squash <commit> = use commit, but meld into previous commit
        # f, fixup [-C | -c] <commit> = like "squash" but keep only the previous
        #                    commit's log message, unless -C is used, in which case
        #                    keep only this commit's message; -c is same as -C but
        #                    opens the editor
        # x, exec <command> = run command (the rest of the line) using shell
        # b, break = stop here (continue rebase later with 'git rebase --continue')
        # d, drop <commit> = remove commit
        # l, label <label> = label current HEAD with a name
        # t, reset <label> = reset HEAD to a label
        # m, merge [-C <commit> | -c <commit>] <label> [# <oneline>]
        # .       create a merge commit using the original merge commit's
        # .       message (or the oneline, if no original merge commit was
        # .       specified); use -c <commit> to reword the commit message
        #
        # These lines can be re-ordered; they are executed from top to bottom.
        #
        # If you remove a line here THAT COMMIT WILL BE LOST.
        #
        # However, if you remove everything, the rebase will be aborted.

<br>
<br>
<br>

## 🍒 Cherry Picking 🍒

`git cherry-pick <hash>`: pick specific commits to add to a desired branch.

        git cherry-pick f9816eb...241ed54

        CONFLICT (add/add): Merge conflict in story-index.txt
        Auto-merging story-index.txt
        [story/willow-and-lake c139299] Updated the story index file
            Author: forest <coding@forest.com>
            Date: Sat Jan 29 09:10:26 2022 +0000
            1 file changed, 4 insertions(+)
