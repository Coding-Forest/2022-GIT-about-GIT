## Issue

Git fails to `pull`.

<br>

## Context

I mistyped authentication details so I exited the `pull` process in the middle. I run the `pull` command again and the following happens:

    git pull origin main

    error: You have not concluded your merge (MERGE_HEAD exists).
    hint: Please, commit your changes before merging.
    fatal: Exiting because of unfinished merge.


<br>

## Solution

    git merge --abort

<br>

Now check your `status` just in case.

    git status

    On branch main
    Your branch and 'origin/main' have diverged,
    and have 1 and 2 different commits each, respectively.
       (use "git pull" to merge the remote branch into yours)

    nothing to commit, working tree clean

<br>

## Success

Then `pull` again. It works!

    git pull origin main

    Username for 'https://github.com': 
    Password for 'https://: 
    From https://github.com/Coding-Forest/2022-Linux
        * branch            main       -> FETCH_HEAD
    Merge made by the 'recursive' strategy.
        README.md | 13 +++++++++++++
        1 file changed, 13 insertions(+)
        create mode 100644 README.md


<br>

### References 

  - https://www.lesstif.com/gitbook/git-pull-you-have-not-concluded-your-merge-merge_head-exists-23757078.html