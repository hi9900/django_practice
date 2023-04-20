- 새로운 drf 프로젝트 생성, articles 앱 생성, urls 등록

- Article 모델 작성 및 Migration

- fixtures 데이터 로드

- drf 설치, 등록

---

- GET - List

  - 게시글 데이터 목록 조회

- GET - Detail

  - 단일 게시글 데이터 조회

  - 각 데이터의 상세 정보를 제공하는 ArticleSerializer 정의

- POST - List

  - 게시글 생성

  - 생성이 성공했을 때는 201 상태코드, 실패했을 때 400 상태코드 응답

- DELETE - Detail

  - 게시글 삭제

  - 삭제에 성공했을 때는 204

- PUT - Detail
 
  - 게시글 수정

  - 성공했을 경우 200 상태코드

---

- Comment 모델 작성 후 데이터베이스 초기화

- Migration, fixture load

- CommentSerializer 작성

- GET - List

  댓글 목록 조회

- GET - Detail

  단일 댓글 조회

- POST - create

  단일 댓글 생성

  외래키 필드를 읽기전용 필드로 설정

- DELETE, PUT

  댓글 삭제, 수정

  article 정보가 이미 저장되어 있기 때문에 save속성 안넘겨도 됨