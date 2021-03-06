## 동기(Sync) 비동기(Async) 란?



```js
const fs = require('fs')

console.log('파일을 생성합니다')
// fs 모듈로 동기방식의 파일 생성 메소드 
fs.writeFileSync('./Testfile.txt', 'Test용 파일 입니다.')
console.log('파일이 생성됩니다.')
console.log('파일 생성중')
```
> 위의 코드의 결과는 정말 쉽게 알수있다.
> 1. 파일을 생성합니다
> 2. 파일이 생성 되고
> 3. 파일이 생성됩니다.
> 4. 파일 생성중 이런식으로 구성이 될것이다. 

```js
const fs = require('fs')

console.log('파일을 생성합니다')
fs.writeFile('./Testfile.txt', 'Test용 파일 입니다.', (err) => {
        // 만일 에러가 발생했다면 에러를 호출해줍니다.
    if(err) throw err
    console.log('파일이 생성됩니다.')
})
console.log('파일 생성중')
```
> 위 코드는 비동기 방식으로 제작한 코드이다.
> 1. 파일을 생성합니다.
>  2. 파일 생성시키고  
> 3. 파일이 생성중. 
> 4. 파일이 생성이 다되면 
> 5. 파일이 생성됩니다. 이 순서로 결과가 출력 될것이다.

> **결론** : *비동기 방식은 파일을 생성하면서 동시에 작업이 가능하게 만들어주는것이죠*

