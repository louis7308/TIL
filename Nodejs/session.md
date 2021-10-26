## 세션이란?

쿠키와 달리 서버의 메모리에다가 사용자의 세션 데이터를 저장하고 웹 브라우저는 Session ID만을 가지고 있기 때문에 비교적 안전합니다.

```jsx
세션의 동작을 살펴보자.

1. 서버는 웹 브라우저에게 세션 값을 보내줍니다. (SID라고 하며, 단순 식별자)
2. 클라이언트는 접속할 때 자신이 가지고 있는 SID를 서버에게 전달합니다.
3. 서버는 클라이언트가 보내준 SID를 가지고, 해당 유저를 식별한다.
```

> npm install —save express-session
> 

> npm install —save express-mysql-session
> 

세션은 저장소를 사용하지 않기 때문에 직접 저장소를 만들어 사용하여야 한다 ( mysql 패키지 사용)

### express-session 설정

```jsx
const session = require('express-session');                      (1)
const MySQLStore = require('express-mysql-session')(session);    (2)
const options ={                                                 (3)
    host: 'localhost',
    port: 3306,
    user: '',
    password: '',
    database: ''
};
const sessionStore = new MySQLStore(options);                    (4)

app.use(session({                                                (5)
  secret:"asdfasffdas",
  resave:false,
  saveUninitialized:true,
  store: sessionStore                                            (6)
}))
```

(1) express-session 모듈을 로드합니다.

(2) express-mysql-session 모듈을 로드하되, 인자로 session을 넘겨줍니다.

(3) 데이터베이스에 접속하는 것이므로, host, port, user, password, database 정보를 객체로 저장해둡니다.

(4) 앞서 저장한 객체를 MySQLStore() 함수의 인자로 넘겨줍니다. 이 때 생성되는 객체를 sessionStore라는 변수에 저장합니다.

(5) session() 미들웨어를 설치합니다. secret은 keyboard cat으로 랜덤한 값을 입력해줍니다. secret 값은 공개되어서는 안됩니다. resave와 saveUninitialized는 세션을 다시 저장하냐, 초기화하냐 정도의 옵션인 것 같은데 저도 잘 모르겠습니다.. 보통 false와 true로 설정한다고 합니다.

(6) 저장소를 앞서 DB 연결로 생성된 sessionStore 객체로 지정합니다. (제가 지정한 DB에 session 테이블이 생성됨을 확인할 수 있습니다.)

### session 사용하기

```jsx
app.get('/login', function(req,res){    
    const post = req.body;
    db.query('select member.id as id, password, author_id, name from member left join author on member.author_id = author.id where member.id=? and password=?',
    [post.id,post.password], (err,result) => {
        if(err) throw err;
        if(result[0]!==undefined){
            req.session.uid = result[0].id;                            (1)
            req.session.author_id = result[0].author_id;
            req.session.isLogined = true;
            //세션 스토어가 이루어진 후 redirect를 해야함.
            req.session.save(() => {                               (2)
                res.redirect('/'); // 다른 페이지 이동할때 사용됨
            });
        }
    });
}
```