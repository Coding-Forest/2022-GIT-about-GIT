# <span id='top'>06 Understanding GIT </span>

<br>

[[Command types]](#command)  
[[Git object Contents]](#object)  
[[Recap]](#recap)  

<br>

`GIT` is a store of key:value pairs. 
- a file is added to a commit, the contents of the file are hashed using the SHA-1 algorithm.
- `hash`: key name for the folder and stores the file using the key name.

<br>

## Command types

- Porcelain commands
  
  - `git add`
  - `git status`
  - `git commit`

<br>

- Plumbing commands: get access to the internals of `git`.
  
  - `git hash-object`
  - `git ls-files`
  - `git rev-parse`
  - `git ls-remote`
  - `git cat-file -p <hash>`
    - `-p`: prettyprint

<br>

- 1) `git hash-object`

            cd ./.git/objects ; ls
            7a  97  info  pack
            
            cd 7a ; ls
            102e66aa3a3e5cd548aad7eb9cf357eb55d357
            
            cd ../97 ; ls
            4a05363dc5ef3563e4075ab3844a15440b0eba

<br>
<br>

## <span id='object'>Git Object Contents</span>

[[Top]](#top)

<br>

- `commit`
- `tree`: a folder on your file system that is associated with the repository
- `blob`: a piece of data

<br>
<br>

## <span id='recap'>Recap</span>

    sudo apt install git-all
    sudo apt install git-man


    cd my_repo
    git init
    git remote add origin https://github.com/deep-woods/2022-GIT-about-GIT.git


    git push origin master
    git clone  https://github.com/deep-woods/2022-GIT-about-GIT.git


    git checkout -b branch_repo


    git merge branch_repo


    git rebase master          <------- creates a different commit history. 


    git rebase -i HEAD~4


    git revert 7fw336w3
    git reset --soft HEAD~1    <------- Keep the reset changes in the working area
    git reset --hard HEAD~1    <------- Wipe out the reset changes