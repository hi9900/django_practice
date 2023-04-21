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

- Article Detail 페이지에 댓글 출력

  override- 중첩

- shortcutfunction

  get_object_or_404(): objects.get, 없으면 404

  get_list_or_404(): objects.all, 없으면 404

- 특정 게시물의 댓글 목록 조회

  댓글 목록 조회(GET-List) + 댓글 생성(POST-Create)

  comment_list 함수 수정

---

- 상세조회 페이지에서 `comment_set`을 `comments`로 표현, 댓글 조회 시 `article id` 필드는 안보이게

  1. `to_representation`: 직렬화

  직렬화가 필요한 개체 인스턴스를 가져오고 기본 표현을 반환, 표현 스타일을 수정하기 위해 재지정

  2. 