```
# Git - Github 연결 (User)

##### 한번만 해도 되는 작업

`git config --global user.name <username> ` :  username 등록

`git config --global user.name  ` :  username 확인

`git config --global user.email <email> ` : email 등록

`git config --global user.email ` : email 확인



# Git - Github 연결 (Repository)

##### ⭐️Repository 연결할때는 한번만 해도 되는 작업⭐️

`git init` : git 시작

`git remote add origin <git repository url>` : repository 연결



##### 파일 수정, 생성 할때마다 해야하는 작업!!!

`git add .` : 모든 파일 staging area에 올리기

`git add <file_name>` :  파일 staging area에 올리기

`git commit -m '<commit message>'` : 커밋 message 작성

`git push origin master` : github로 밀어내기
```

# git bash 작성

- `mkdir` 폴더만들기
  ex: `mkdir TIL` : TIL폴더생성
- `li` : 작업공간의 리스트 보여주기
- `cd ..` : 상위 공간으로 이동
- `cd 위치` : 해당 위치로 이동 
- `vi` : 파일 생성
  ex: `vi READ.md` : READ.md 파일 생성
  vi창 빠져나오는 법: `esc` 클릭 후, `:wq` 작성 후 Enter
- `git status` : 상태 확인
- `git add .` 모든 파일 트래킹하여 staging area 에 올리기
- `git commit -m ' 메시지'` : 커밋 메시지 작성
-  `git push origin master` : github으로 밀어내기

