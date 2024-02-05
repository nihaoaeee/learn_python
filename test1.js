'use strict';
class Demo {
    demo(arr = []) {
        console.log(arr);
        arr.push(1);
    }
}

let de = new Demo();
for (let index = 0; index < 10; index++) {
    de.demo();
}
