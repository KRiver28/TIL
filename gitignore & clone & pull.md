# gitignore & clone & pull

------

## [1] .gitignore

> 특정 파일 혹은 폴더에 대해 Git이 버전 관리를 하지 못하도록 지정하는 것

### (1) .gitignore에 작성하는 목록

- 민감한 개인 정보가 담긴 파일 (전화번호, 계좌번호, 각종 비밀번호, API KEY 등)
- OS(운영체제)에서 활용되는 파일
- IDE(통합 개발 환경 - pycharm) 혹은 Text editor(vscode) 등에서 활용되는 파일
  - 예) pycharm -> .idea/
- 개발 언어(python) 혹은 프레임워크(django)에서 사용되는 파일
  - 가상 환경 : `venv/`
  - `__pycache__/`

### (2) .gitignore 작성 시 주의 사항

- 반드시 이름을 `.gitignore`로 작성합니다. 앞의 점(.)은 숨김 파일이라는 뜻입니다.

- `.gitignore` 파일은 `.git` 폴더와 동일한 위치에 생성합니다.

- **제외 하고 싶은 파일은 반드시 `git add` 전에 `.gitignore`에 작성합니다.**

  <aside> ❗ **왜 git add 전에 .gitignore에 작성해야 할까요?**

  `git add a.txt` 라고 작성하면, 이제 Git은 `a.txt`를 버전 관리의 대상으로 여깁니다. 한 번 버전 관리의 대상이 된 `a.txt`는 이후에 .gitignore에 작성하더라도 무시되지 않고 계속 버전 관리의 대상으로 인식됩니다.

  따라서 제외 하고 싶은 파일은 반드시 git add 전에 .gitignore에 작성해야 합니다!

  </aside>

### (3) .gitignore 쉽게 작성하기

> .gitignore의 내용을 쉽게 작성할 수 있도록 도와주는 두 개의 사이트를 소개합니다. 자신의 개발 환경에 맞는 것을 찾아서 `전체 복사, 붙여넣기`를 하면 됩니다.

1. **웹사이트**

[gitignore.io](https://gitignore.io/)

1. **gitignore 저장소**

https://github.com/github/gitignore

1. **Python에 대한 .gitignore 예시**

   ![https://gitignore.io/ 에서 가져옴](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fd7bd601-9433-418a-b08e-7b027db9a301/Untitled.png)

   https://gitignore.io/ 에서 가져옴

## [2] 실습

> `Vscode, Markdown, Git 기초, Github, .gitignore` 까지 배운 것을 모두 활용하는 실습 진행

1. 홈 디렉토리에서 `git-training-1` 이라는 이름의 폴더를 만들고, 그 안에서 vscode를 엽니다.
2. Github에서 마찬가지로 `git-training-1` 이름으로 원격 저장소를 생성합니다.
3. 로컬 저장소에서 `README.md`와 `.gitignore` 파일을 만든 후 첫 번째 커밋을 기록합니다.
4. Typora를 이용해 `README.md`를 자유롭게 작성하고 두 번째 커밋을 기록합니다.
5. `no.txt` 파일을 만든 후 `.gitignore`에 등록하고 세 번째 커밋을 기록합니다.
6. 로컬 저장소와 원격 저장소를 연결합니다.
7. 로컬 저장소의 변경 사항을 원격 저장소에 업로드 합니다.

**실습 결과 확인**

![README.md의 내용과 각 커밋 메시지는 자유롭게 작성합니다.](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ab8a2e0b-2ea4-40e5-8016-248a596652f9/Untitled.png)

**README.md의 내용과 각 커밋 메시지는 자유롭게 작성합니다.**

## [3] 심화

> .gitignore에 대해 조금 더 알아봅니다.

### (1) .gitignore 패턴 규칙

1. 아무것도 없는 라인이나, `#`로 시작하는 라인은 무시합니다.
2. `슬래시(/)`로 시작하면 하위 디렉터리에 재귀적으로 적용되지 않습니다.
3. 디렉터리는 `슬래시(/)`를 끝에 사용하는 것으로 표현합니다.
4. `느낌표(!)`로 시작하는 패턴의 파일은 ignore(무시)하지 않습니다.
5. 표준 Glob 패턴을 사용합니다.
   - `*(asterisk, wildcard)`는 문자가 하나도 없거나 하나 이상을 의미합니다.
   - `[abc]`는 중괄호 안에 있는 문자 중 하나를 의미합니다.
   - `물음표(?)`는 문자 하나를 의미합니다.
   - `[0-9]`처럼 중괄호 안에 하이픈(-)이 있는 경우 0에서 9사이의 문자 중 하나를 의미합니다.
   - `**(2개의 asterisk)`는 디렉터리 내부의 디렉터리까지 지정할 수 있습니다. (`a/**/z`라고 작성하면 `a/z`, `a/b/z`, `a/b/c/z` 까지 모두 영향을 끼칩니다.)

### (2) 패턴 예시

```bash
# .gitignore

# 확장자가 txt인 파일 무시
*.txt

# 현재 확장자가 txt인 파일이 무시되지만, 느낌표를 사용하여 test.txt는 무시하지 않음
!test.txt

# 현재 디렉터리에 있는 TODO 파일은 무시하고, folder/TODO 처럼 하위 디렉터리에 있는 파일은 무시하지 않음
/TODO

# build/ 디렉터리에 있는 모든 파일은 무시
build/

# folder/notes.txt 파일은 무시하고 folder/child/arch.txt 파일은 무시하지 않음
folder/*.txt

# folder 디렉터리 아래의 모든 .pdf 파일을 무시
folder/**/*.pdf
```