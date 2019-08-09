function log(message){
    console.log(message);
}
var message = "hello-world";
log(message);
function doSomething(){
    for(let i=0;i<5;i++){ //
        console.log(i);
    }
    console.log('finally:'+i);
}
doSomething();

let a: number;
let b: number[] = [1,2,3,4];
let c: boolean = true;
enum Color { Red = 0, Green = 1, Blue= 2};
let backgroundcolor = Color.Red;