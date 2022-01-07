# branch

- `git branch` branch 리스트 확인
- `git branch <name>` name이라는 리스트 생성
- `git switch <name>` name이라는 branch로 이동
- `git checkout` 브랜치 이동
- `git log --all --oneline --graph` 그래프 형태로 branch들을 나타냄
- `git merge <branch명>` 해당branch를 합친다. 
   (기준이 될 브랜치에서! 합칠 브랜치 명을 작성)
- `git branch -d <name>`  name이라는 branch를 삭제한다.
-  `git switch -c <name>` name이라는 branch를 생성하면서 해당 branch로 변경



# 수정하는 방법

- `git restore <파일명>` 
  * 파일 수정 후 아직 add하지 않았을때, 이전 상태로 변경
- `git restore --staged`
  - 스테이징 에이아에서 내려준다.
- `git rm -cached`
  - untracked 상태로 바꿔준다.
- `commit --amend`
  - 파일 수정이 없으면 코밋 메시지만 재작성 해주고
  - 파일 수정이 있으면 그것을 반영하여 코밋을 덮어씌운다.
- `git diff`
  - 워킹디렉토리와 가장 최근 기록(스테이징 에리아  혹은 코밋의)의 차이를 보여준다.
- `git diff --staged`
  - 스테이징 에리아와 코밋의 차이를 보여준다.



# reset

- `git reset --soft <commit log>` commit만 하면 원상태로 돌아올 수 있다.
- `git reset --mixed <commit log>`  add, commit까지하면 원상태로 돌아올 수 있다.
- `git reset --hard <commit log>` 진짜 리셋 (작업+add+commit 까지 해야 돌아올 수 있다.)
- `git reflog` 코밋 리셋 기록 확인
- `git revert <commit id> ` 해당 코밋을 취소하고 코밋를 남긴다.



