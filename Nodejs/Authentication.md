> **인증과 인가는** API 에서 자주 구현되는 기능중 하나이다.

### 인증 (Authentication)

> 방문자가 자신이 회사 건물에 들어 갈 수있는지 확인 받는 과정이다. 

- 유저 아이디와 비밀번호를 확인하는 절차를 가르키며 로그인 하는 과정을 생각하면 된다.

```md
 **로그인*!*의 과정을 살펴보자.

1. 회원가입을 통한 아이디/비밀번호 생성
2. 비밀번호 암호화 -> DB저장
3. 유저 로그인 : 아이디와 비밀번호 입력
4. 비밀번호 확인 : 비밀번호를 암호화 한뒤 DB의 암호와 같은지 확인, 일치하면 로그인!
5. 로그인 성공 > access token을 클라이언트에게 전달
6. 발급받은 access token을 통해 로그인 유지 및 서비스 사용
```

### 인가 (Authorization)

> 유저가 요청하는 request를 실행할 수 있는 권한이 있는 유저인가를 확인하는 절차.

- 유저는 서버에게 요청을 보낼때 {encoding} 된 {Access Token}을 함께 첨부하며, 서버는 {Access Token} 을 {decoding}을 통해 데이터를 확인하여, 유저 정보를 얻는다. 서버에서 해당 유저 정보를 통해 권한(permission)을 확인하여 해당 요청을 처리함.

```md
**인가 절차*!*
1. Authentication 절차를 통해 access token을 생성한다. access token에는 유저 정보를 확인할 수 있는 정보가 들어가 있어야 한다 (예를 들어 user id).
2. 유저가 request를 보낼때 ac낸cess token을 첨부해서 보다.
3. 서버에서는 유저가 보낸 access token을 복호화 한다.
4. 복호화된 데이터를 통해 user id를 얻는다.
5. user id를 사용해서 database에서 해당 유저의 권한(permission)을 확인하다.
6. 유저가 충분한 권한을 가지고 있으면 해당 요청을 처리한다.
7. 유저가 권한을 가지고 있지 않으면 Unauthorized Response(401) 혹은 다른 에러 코드를 보낸다.
```