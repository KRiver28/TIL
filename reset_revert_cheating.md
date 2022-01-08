------

## [1] 파일 내용을 수정 전으로 되돌리기

> Working Directory에서 파일을 수정했다고 가정해봅시다. 만약 이 파일의 수정 사항을 취소하고, 원래 모습대로 돌리려면 어떻게 해야 할까요?

### (1) git restore

- `git restore <파일 이름>`의 형식을 사용합니다.
- Git의 추적이 되고 있는, 즉 버전 관리가 되고 있는 파일만 되돌리기가 가능합니다.

1. 이미 버전 관리가 되고 있는 [test.md](http://test.md) 파일을 변경 후 저장(save)합니다.

   ```
   # test.md
   Hello
   World <- "World"라는 새로운 내용 추가
   -------------------------------------
   이후 저장
   ```

2. test.md는 modified 상태가 되었습니다.

   ```bash
   $ git status
   On branch master
   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git restore <file>..." to discard changes in working directory)
           modified:   test.md
   
   no changes added to commit (use "git add" and/or "git commit -a")
   ```

3. git restore를 통해 수정 전으로 되돌립니다.

   ```bash
   $ git restore test.md
   ```

   ```
   # test.md
   Hello
   -------------------------------------
   World가 삭제 되면서, 수정 전으로 되돌아감
   ```

4. 참고사항

   ```bash
   구버전 Git(2.23.0 이전)에서는 아래와 같은 명령어 사용
   
   $ git checkout -- <파일 이름>
   ```

<aside> ❗ 한 번 git restore를 통해 수정을 취소하면, 해당 내용을 복원할 수 없으니 주의 바랍니다!

</aside>

## [2] 파일 상태를 Unstage로 되돌리기

> `git add`를 통해서 파일을 `Staging Area`에 올렸다고 가정해봅시다. 만약 이 파일을 다시 `Unstage` 상태로 내리려면 어떻게 해야 할까요? 두 가지 상황으로 나누어 살펴보겠습니다.

### (1) git rm --cached

> 새로운 파일을 만들고 Staging Area에 올렸는데, 이를 취소하고 싶을 때
>
> `git rm --cached <파일 이름>` 의 형식을 사용합니다.

1. `test.md` 파일을 생성하고 git add를 진행

   ```bash
   $ touch test.md
   ```

   ```bash
   $ git add test.md
   ```

   ```bash
   $ git status
   On branch master
   
   No commits yet
   
   Changes to be committed:
     (use "git rm --cached <file>..." to unstage)
           new file:   test.md
   ```

2. Staging Area에 올라간 test.md를 다시 내리기

   ```bash
   $ git rm --cached test.md
   rm 'test.md'
   ```

   ```bash
   $ git status
   On branch master
   
   No commits yet
   
   Untracked files:
     (use "git add <file>..." to include in what will be committed)
           test.md
   
   nothing added to commit but untracked files present (use "git add" to track)
   ```

### (2) git restore --staged

> Git이 이미 관리하고 있는 파일을 수정하고 Staging Area에 올렸는데, 이를 취소하고 싶을 때

`git restore --staged <파일 이름>` 의 형식을 사용합니다.

1. `test.md`의 내용을 변경하고 git add를 진행

   ```bash
   test.md 파일 변경 후
   $ git add test.md
   ```

   ```bash
   $ git status
   On branch master
   Changes to be committed:
     (use "git restore --staged <file>..." to unstage)
           modified:   test.md
   ```

2. Staging Area에 올라간 test.md를 다시 내리기

   ```bash
   $ git restore --staged test.md
   ```

   ```bash
   $ git status
   On branch master
   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git restore <file>..." to discard changes in working directory)
           modified:   test.md
   
   no changes added to commit (use "git add" and/or "git commit -a")
   ```

3. 참고사항

   ```bash
   구버전 Git(2.23.0 이전)에서는 아래와 같은 명령어 사용
   
   $ git reset HEAD <파일 이름>
   ```

## [3] 바로 직전 커밋을 되돌리기

> 만약 `A`라는 기능을 완성하고 `"A 기능 완성"`이라는 커밋을 남겼다고 가정해봅시다. 그런데 아차! A 기능에 필요한 파일 중 1개를 빼놓고 커밋 했다는 걸 깨달아 버렸습니다. 직전 커밋을 취소하고, 모든 파일을 포함해서 다시 커밋 하려면 어떻게 해야 할까요?

### (1) git commit --amend

- Staging Area에 새로 올라온 내용이 없다면, 단순히 `직전 커밋의 메시지만 수정`합니다.
- Staging Area에 새로 올라온 내용이 있다면, 직전 커밋 내역에 같이 묶어서 재 커밋 됩니다.

1. A 기능을 완성하고 커밋합니다.

   ```bash
   $ git commit -m 'A 기능 완성'
   ```

2. 빼놓은 파일 1개를 Staging Area에 올립니다.

   ```bash
   $ git add forgotten_file
   ```

3. 직전 커밋에 forgotten_file을 포함하기 위해 `git commit --amend`를 입력합니다.

   ```bash
   $ git commit --amend
   ```

4. Vim 편집기가 열리면서 직전 커밋 메시지를 수정할 수 있습니다.

   ```bash
   A 기능 완성
   
   # Please enter the commit message for your changes. Lines starting
   # with '#' will be ignored, and an empty message aborts the commit.
   #
   # Date:      Mon Dec 13 12:04:39 2021 +0900
   #
   # On branch master
   # Changes to be committed:
   #       modified:   A.md
   #
   # Changes not staged for commit:
   ```

5. Vim 편집기를 저장 후 종료하면 직전 커밋이 덮어 씌워집니다.

   ```bash
   $ git commit --amend
   [master a95b4dd] A 기능 완성
    Date: Mon Dec 13 12:04:39 2021 +0900
    1 file changed, 2 insertions(+)
   ```

6. `git log -p` 를 사용하여 직전 커밋의 변경 내용을 살펴봅니다.

<aside> 💡 **Vim 간단 사용법**

1. 입력 모드(

   ```
   i
   ```

   )

   - 문서 편집 가능

2. 명령 모드(

   ```
   esc
   ```

   )

   - `dd` : 해당 줄 삭제

   - ```
     :wq
     ```

      : 저장 및 종료

     - `w` : write (저장)
     - `q` : quit (종료)

   - ```
     :q!
     ```

      : 강제 종료

     - `q` : quit
     - `!` : 강제 </aside>