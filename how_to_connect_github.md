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