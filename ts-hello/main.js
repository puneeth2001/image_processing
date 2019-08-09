function log(message) {
    console.log(message);
}
var message = "hello-world";
log(message);
function doSomething() {
    for (var i = 0; i < 5; i++) { //
        console.log(i);
    }
    console.log('finally:' + i);
}
doSomething();
var a;
var b = [1, 2, 3, 4];
var c = true;
var Color;
(function (Color) {
    Color[Color["Red"] = 0] = "Red";
    Color[Color["Green"] = 1] = "Green";
    Color[Color["Blue"] = 2] = "Blue";
})(Color || (Color = {}));
;
var backgroundcolor = Color.Red;
