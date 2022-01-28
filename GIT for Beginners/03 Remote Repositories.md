# <span id='top'>03 Remote Repositories</span>

<br>

[[Push]](#push)  
[[Clone]](#clone)  
[[Pull Request]](#pullrequest)  
[[Fetching and Pulling]](#fetchpull)  
[[Merge Conflicts]](#mergeconflicts)  
[[Fork]](#fork)  

<br>

## Set a remote repository

[[Top]](#top)

- `git remote add origin [HTTPS/SSH].git`

        git remote add origin https://github.com/Coding-Forest/2022-GIT-about-GIT.git

<br>

- `git remote -v`: list all remote repos.

        origin	https://github.com/Coding-Forest/2022-GIT-about-GIT.git (fetch)
        origin	https://github.com/Coding-Forest/2022-GIT-about-GIT.git (push)


<br>

## <span id='push'>`Push`</span>

[[Top]](#top)

- syntax: `git push <remote repo alias> <current branch>`   <--- takes 2 arguments
  - `git push origin master`

<br>
<br>

## Hands-on Exercise

- `git status`

        On branch master
        nothing to commit, working tree clean


- `git push origin master`

        Username for 'https://forest@github.com': 
        Password for 'https://forest@github.com': here please put AUTH TOKEN!

        Enumerating objects: 12, done.
        Counting objects: 100% (12/12), done.
        Delta compression using up to 2 threads
        Compressing objects: 100% (12/12), done.
        Writing objects: 100% (12/12), 10.12 KiB | 5.06 MiB/s, done.
        Total 12 (delta 1), reused 0 (delta 0)
        remote: Resolving deltas: 100% (1/1), done.
        To https://github.com/Coding-Forest/2022-GIT-about-GIT.git
        * [new branch]      master -> master


<br>

## <span id='clone'>`Clone`</span>

[[Top]](#top)

<br>

- `git clone [ SSH LINK ]`

<br>

        git clone https://github.com/Coding-Forest/UNI-2022-1281-13-Statistical-Inference.git

        Cloning into 'UNI-2022-1281-13-Statistical-Inference'...
        remote: Enumerating objects: 3, done.
        remote: Counting objects: 100% (3/3), done.
        remote: Compressing objects: 100% (2/2), done.
        remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
        Unpacking objects: 100% (3/3), 653 bytes | 653.00 KiB/s, done.
        


        git clone https://github.com/Coding-Forest/UNI-2022-4407-12-Machine-Learning.git
        
        Cloning into 'UNI-2022-4407-12-Machine-Learning'...
        remote: Enumerating objects: 3UNI-2022-4407-12-Machine-Learning3), 654 bytes | 654.00 KiB/s, done.

<br>

        cd UNI-2022-1281-13-Statistical-Inference
        git remote -v

        origin	https://github.com/Coding-Forest/UNI-2022-1281-13-Statistical-Inference.git (fetch)
        origin	https://github.com/Coding-Forest/UNI-2022-1281-13-Statistical-Inference.git (push)


        cd ../UNI-2022-4407-12-Machine-Learning
        git remote -v

        origin	https://github.com/Coding-Forest/UNI-2022-4407-12-Machine-Learning.git (fetch)
        origin	https://github.com/Coding-Forest/UNI-2022-4407-12-Machine-Learning.git (push)


<br>
<br>

## <span id='pullrequest'>`Pull Request`</span>

[[Top]](#top)

- `git checkout -b <new branch>`: Branch out of the `master` repository to not directly modify `master` without the master's approval.

<br>
<br>

## <span id='fetchpull'>Fetching and Pulling</span>

[[Top]](#top)

Bring down (download) the changes in the `origin` in the cloud server down to the local machine. 

1) `fetch` + `merge`
- `git fetch <from branch> <to branch>`

        git branch
          * master
          story/willow-and-lake
          animals

        git fetch origin master

        remote: Enumerating objects: 4, done.
        remote: Counting objects: 100% (4/4), done.
        remote: Compressing objects: 100% (3/3), done.
        remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
        Unpacking objects: 100% (3/3), 723 bytes | 723.00 KiB/s, done.
        From https://github.com/Coding-Forest/2022-GIT-about-GIT/
          * branch            master     -> FETCH_HEAD
          2d90c4d..c104b5b  master     -> origin/master


        git branch -a
  
          * master
            story/willow-and-lake
            animals
          remotes/origin/master                <----- the result of fetching.

<br>

- `git merge <other-branch>`
  
        git merge origin/master

        Updating 2d90c4d..c104b5b
        Fast-forward
        perching_birds.txt | 21 +++++++++++++++++++++
        1 file changed, 21 insertions(+)
        create mode 100644 perching_birds.txt

<br>
<br>

2) `pull`
- `git pull origin master` = `fetch` + `merge`

        git pull origin master

        remote: Enumerating objects: 4, done.
        remote: Counting objects: 100% (4/4), done.
        remote: Compressing objects: 100% (3/3), done.
        remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
        Unpacking objects: 100% (3/3), 779 bytes | 779.00 KiB/s, done.
        From https://github.com/Coding-Forest/2022-GIT-about-GIT/
           * branch            master     -> FETCH_HEAD
           c104b5b..0fb6d30  master     -> origin/master
        Updating c104b5b..0fb6d30
        Fast-forward
           die-Reiher.txt | 19 +++++++++++++++++++
           1 file changed, 19 insertions(+)
           create mode 100644 die-Reiher.txt

<br>
<br>

## <span id='mergeconflicts'>Merge Conflicts</span>

[[Top]](#top)

This occurs when multiple local repositories merge to the `origin` at the same time. The identity of the `origin` gets fragmented. 

        git push origin master

        To https://github.com/Coding-Forest/2022-GIT-about-GIT.git
          ! [rejected]        master -> master (fetch first)
        error: failed to push some refs to 'https://github.com/Coding-Forest/2022-GIT-about-GIT.git'
        hint: Updates were rejected because the remote contains work that you do
        hint: not have locally. This is usually caused by another repository pushing
        hint: to the same ref. You may want to first integrate the remote changes
        hint: (e.g., 'git pull ...') before pushing again.
        hint: See the 'Note about fast-forwards' in 'git push --help' for details.


<br>

To resolve this, you have to `pull` form `origin` first. 

        git pull origin master

        remote: Enumerating objects: 4, done.
        remote: Counting objects: 100% (4/4), done.
        remote: Compressing objects: 100% (3/3), done.
        remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
        Unpacking objects: 100% (3/3), 305 bytes | 305.00 KiB/s, done.
        From https://github.com/Coding-Forest/2022-GIT-about-GIT.git
           * branch            master     -> FETCH_HEAD
           4c7163b..fc09dba  master     -> origin/master

        hint: Pulling without specifying how to reconcile divergent branches is
        hint: discouraged. You can squelch this message by running one of the following
        hint: commands sometime before your next pull:
        hint: 
        hint:   git config pull.rebase false  # merge (the default strategy)
        hint:   git config pull.rebase true   # rebase
        hint:   git config pull.ff only       # fast-forward only
        hint: 
        hint: You can replace "git config" with "git config --global" to set a default
        hint: preference for all repositories. You can also pass --rebase, --no-rebase,
        hint: or --ff-only on the command line to override the configured default per
        hint: invocation.
        CONFLICT (add/add): Merge conflict in story-index.txt
        Auto-merging story-index.txt

        Automatic merge failed; fix conflicts and then commit the result.   <--------------- read this.

<br>

Identify the last committer.
- `git log origin/master`

        commit fc09dbae2682b5b92330df39b019f9876f5a1547 (origin/master, origin/HEAD)
        Author: forest <coding@forest.com>
        Date:   Fri Jan 28 18:53:50 2022 +0000

                Added the index file

<br>

Fix the error, then commit the merged file again.
- `git commit -am 'Resolved merge conflicts and merged story index'`

        [master 5e9f6b3] Resolved merge conflicts and merged story index

<br>

Then finally `push` the changes to the `origin`.

        git push origin master

        Enumerating objects: 9, done.
        Counting objects: 100% (9/9), done.
        Delta compression using up to 36 threads
        Compressing objects: 100% (6/6), done.
        Writing objects: 100% (6/6), 628 bytes | 628.00 KiB/s, done.
        Total 6 (delta 3), reused 0 (delta 0), pack-reused 0
        remote: . Processing 1 references
        remote: Processed 1 references in total
        To https://github.com/Coding-Forest/2022-GIT-about-GIT.git
        fc09dba..5e9f6b3  master -> master

<br>
<br>

## <span id='fork'>Fork</span>

[[Top]](#top)


<br>
<br>
