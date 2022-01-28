# GIT branches - Merging branches

<br>

- fast-forward merge
  - the current branch has no extra commits. 
  - doesn't create a new commit. This `merge` merges the commits on the current branch into the target branch.

- no-fast-forward merge
  - Performed when there are new commits in the target branch. 
  - GIT creates a new `merging commit` on the target branch. So the history will log (commits in target + current branch), (commits in the target branch), and the (new merge commit including all changes in both branches.)

<br>

Syntax 

- `git merge <branch>`: stay on the current branch and the target <branch> will be merged into your current branch.

<br>

## Hands-on Exercise 

It is important that you clear or to-commits in each branch prior to merging. 

- `git rm --cached <file name>`: delete file. 

        git rm --cached forest_story.txt

        rm 'forest_story.txt'


- `git status`

        On branch story/willow-and-lake
        Changes to be committed:
        (use "git restore --staged <file>..." to unstage)
                deleted:    forest_story.txt


- `git commit -m 'deleted forest_story'`: commit deletion of files... ? 

        [story/willow-and-lake 75782a6] deleted forest_story
            1 file changed, 3 deletions(-)
                delete mode 100644 forest_story.txt 


- `git status`
        
        On branch story/willow-and-lake
            nothing to commit, working tree clean

<br>
<br>

### Now let's merge all branches to our `master`. 

<br>

- `git branch`

        animals
        * master
        story/willow-and-lake

<br>

- `git merge animals`
    
        Merge made by the 'recursive' strategy.

<br>

- `git merge story/willow-and-lake`

        Removing forest_story.txt
        Merge made by the 'recursive' strategy.
            forest_story.txt    | 3 ---
            willow-and-lake.txt | 4 ++++
            2 files changed, 4 insertions(+), 3 deletions(-)
            delete mode 100644 forest_story.txt
            create mode 100644 willow-and-lake.txt

<br>

- `git log --graph --decorate`

        *   commit 8d389cdd70e105f87ff8dc8a7053419d1560ee5e (HEAD -> master)
        |\  Merge: b3fdc13 75782a6                                       <----- Merge
        | | Author: forest <coding@forest.com>
        | | Date:   Fri Jan 28 20:01:14 2022 +0900
        | | 
        | |     Merge branch 'story/willow-and-lake'
        | | 
        | * commit 75782a62eb3bc00c803956df135dea5a55840ff6 (story/willow-and-lake)
        | | Author: forest <coding@forest.com>
        | | Date:   Fri Jan 28 19:46:22 2022 +0900
        | | 
        | |     deleted forest_story
        | | 
        | * commit 97345c8a158c801b33655e996682a1e5369f7226
        | | Author: forest <coding@forest.com>
        | | Date:   Fri Jan 28 18:57:35 2022 +0900
        | | 
        | |     added story willow-and-lake
        | |   
        * |   commit b3fdc13c9f691231a0538fd89e8a643b42744a9b
        |\ \  Merge: 542e6a4 3b3fc45                                    <----- Merge
        | | | Author: forest <coding@forest.com>
        | | | Date:   Fri Jan 28 20:01:00 2022 +0900
        | | | 
        | | |     Merge branch 'animals'
        | | | 
        | * | commit 3b3fc45e471c21923a46237525fdd88b89820419 (animals)
        | |/  Author: forest <coding@forest.com>
        | |   Date:   Fri Jan 28 20:00:30 2022 +0900
        | |   
        | |       updated gitignore