# 객체(Object)와 배열(Array)

## 객체(Object)
객체란 현실의 사물을 프로그래밍에 반영한 것입니다.
```js
const seungwon = {
    firstname: "Jeon",
    'last name': "Seung won",
    age: 17,
    height: 170.5,
    weight: 55,
}
```
>위에 코드를 보면 **seungwon** 이라는 변수에 {} 감싼 덩어리 입니다. 바로 저 덩어리가 **객체** 입니다.

### 속성(Property)
> seungwon 객체를 보면 _firstname_ 과 "Jeon" 이 콤마로 구분되는 것들을 객체의 **속성** 이라고 한다 <br>
> 그렇다면 위에 코드를 보면 속성이 5개라는것을 알수있다.

### 키(Key)와 값(Value)
> 위 코드에 [firstname , lastname , age, height , weight] 같은것들을 **객체의 키** 라고 하고 ["Jeon", "Seung won", 17, "170.5, 55] 를 **값** 이라고 부릅니다.
> 즉 속성은 **속성 키 : 값**의 관계로 이루어져 있다. <br>
> **키 값**에 띄어쓰기를 하고싶으면 **'last name'** 같이 키 값에 ''따음표로 감싸서 적어주면 된다. **속성값**은 어떤 값 이든지 상관없다 **문자열** 도 되고, **숫자**여도 되고, **객체**여도 된다. <br> 하지만 속성값이 **함수**이면 우리는 이것을 **메소드**라고 부른다
```js
console.log(seungwon.firstname); // Jeon
console.log(seungwon['firstname']); // Jeon
console.log(seungwon['last name']); // Seung won
```
> seungwon 이라는 객체 안의 **속성 값**을 사용하고 싶을때는 위에 코드처럼 사용하면 된다. 

```js
seungwon.age = 10;
seungwon; // 10 
```
>위와 같이 객체 안의 속성을 바꿀 수도 있습니다.

```js
const seungwon2 = {
    body = {
        firstname: "Jeon",
        lastname: "Seung won",
        age: 17,
        height: "170.5",
        weight: "55",
    }
}
```
>또한 객체안에 객체로 값을 넣을수도있다.



