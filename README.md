# Django

## 환경 설정

- gitignore 생성

- 가상환경 생성 및 활성화

- Django 설치

- 패키지목록 저장

- 프로젝트 및 앱 생성

```bash
$ python -m venv venv
$ source venv/Scripts/activate
$ pip install django==3.2.18
$ pip freeze > requirements.txt
$ django-admin startproject firstpjt .
$ python manage.py startapp articles
```

- settings.py의 INSTALLED_APPS 리스트에 앱 추가

- `templates/base.html` 생성 후 스켈레톤 템플릿 작성 및 경로 추가

- superuser 생성

## articles app

- url mapping

- Model 클래스 작성 후 마이그레이션 작업

- article 모델을 admin 페이지에서 관리할 수 있도록 설정

- ModelForm 생성

- CRUD 구현

## StaticFile

- settings.py의 STATIC_ROOT, STATICFILES_DIRS 지정

- /static/ 경로에 이미지 파일 배치 후 출력

## MediaFile

- settings.py에 MEDIA_ROOT, MEDIA_URL 지정

- urls.py에 미디어 파일 경로 추가

- Pillow 라이브러리 설치

- 모델 클래스 수정(: 이미지 관련 필드 작성) 후 마이그레이션

  - ImageField(): 이미지 업로드에 사용하는 모델 필드

  - FileField(): 파일 업로드에 사용하는 모델 필드

- create, update form태그에 enctype 속성 변경: `enctype="multipart/form-data"`

- views.py create, update에 request.FILES로 파일 및 이미지 담아서 넘김

- image가 있을 때만 출력

## accounts app

- accounts 앱 생성 및 등록

- Custom User model로 대체하기

  - models.py에 User클래스 작성

  - settings.py에 커스텀 User모델 지정

- admin.py에 커스텀 User모델 등록

- 로그인, 로그아웃 구현

- 회원가입, 회원탈퇴, 회원정보수정, 비밀번호 변경 구현

  - CustomUserCreationForm, CustomUserChangeForm 생성

## decorator

- views 함수에 데코레이터 임포트 후 필요한 곳에 사용

`from django.views.decorators.http import require_GET, require_safe, require_POST, require_http_methods`

## articles app - Comment

- Comment 모델 작성

  - content 필드, created_at, updated_at

  - article - comment: 1:N 관계, related_name='comments'

- CommentForm 작성

  - fields 수정

- CRUD

  - detail 페이지에서 CommentForm 출력

  - create_comment 함수 생성

  - detail 페이지 comment 조회

  - 댓글 삭제 구현