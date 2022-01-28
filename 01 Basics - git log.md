# 01 Basics - git log

<br>

## GIT log

- `git log`

        git log

        commit 883435432..........dsfe323sdd3d3 (HEAD -> master)        <--- commit hash
        Author: forest <coding@forest.com>
        Date:   Fri Jan 28 10:51:17 2022 +0900

            added two stories

- `git log --oneline`


        88d9a67 (HEAD -> master) added two stories

<br>
<br>

## Hands-on practice 2 - `git log`

- `Commit info`: commit hash, branch
- `author info`: name, email
- `Date`
- `Update message`


Scenario: there is nothing to commit. Let's update some files and commit them. 

- `git log`

        fatal: your current branch 'master' does not have any commits yet

- Added `timon_and_pumba.txt` then `git status`

        git status

        On branch master
        Untracked files:
        (use "git add <file>..." to include in what will be committed)
            .gitignore
            timon_and_pumba.txt

        nothing added to commit but untracked files present (use "git add" to track)

- `git add` + `git commit`

        git add timon_and_pumba.txt

        git commit -m "added timon and pumba lyrics"

        [master 471ad6f] added timon and pumba lyrics
            1 file changed, 45 insertions(+)
            create mode 100644 timon_and_pumba.txt


- `git status`

        On branch master
        nothing to commit, working tree clean

- `git log`

        commit 7258ed....3293 (HEAD -> master)
        Author: sarah <sarah@example.com>
        Date:   Fri Jan 28 07:13:35 2022 +0000

            Added the lion and mouse story

  - `--name-only` flag

            git log --name-only

            commit 471ad6f.....8868f8 (HEAD -> master)
            Author: forest <coding@forest.com>
            Date:   Fri Jan 28 16:19:11 2022 +0900

                added timon and pumba lyrics

            timon_and_pumba.txt

            commit 88d9a67....04e1bad9
            Author: forest <coding@forest.com>
            Date:   Fri Jan 28 10:51:17 2022 +0900

                added two stories

            forest_story.txt
            lion.txt

  - `--oneline` flag

            git log --oneline

            471ad6f (HEAD -> master) added timon and pumba lyrics
            88d9a67 added two stories


  - `(HEAD -> [branch name])`

<br>

### Team project - e-commerce application 

- move to `/team/e-commerce-app`

    git status

    On branch master
    Your branch is ahead of 'origin/master' by 3 commits.
    (use "git push" to publish your local commits)

    nothing to commit, working tree clean

- check `git log`

    commit c860adddf........ (HEAD -> master)
    Author: birch <birch@forest.com>
    Date:   Fri Jan 28 07:10:43 2022 +0000

        Update color from red to green

    commit ec180c13b........
    Author: willow <willow@forest.com>
    Date:   Fri Jan 28 07:10:43 2022 +0000

        Add instructions to verify application

    commit c097661d9........
    Author: oak <oak@forest.com>
    Date:   Fri Jan 28 07:10:43 2022 +0000

        Increase interval time to 500

    commit 74143590d........ (origin/master, origin/HEAD)
    Author: Mumshad Mannambeth <mmumshad@forest.com>
    Date:   Mon Jul 6 14:41:22 2020 +0800

        Update README.md

    commit 744e000c........
    Author: Mumshad Mannambeth <mmumshad@forest.com>
    Date:   Mon Jul 6 14:11:46 2020 +0800

<br>

- Limit the number of commits on log
  - `git log -<number>`: shows the specified <number> of commits on log. 

        commit c860adddf........ (HEAD -> master)
        Author: birch <birch@forest.com>
        Date:   Fri Jan 28 07:10:43 2022 +0000

            Update color from red to green

        commit ec180c13b........
        Author: willow <willow@forest.com>
        Date:   Fri Jan 28 07:10:43 2022 +0000

            Add instructions to verify application

        commit c097661d9........
        Author: oak <oak@forest.com>
        Date:   Fri Jan 28 07:10:43 2022 +0000

            Increase interval time to 500