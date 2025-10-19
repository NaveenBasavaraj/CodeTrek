/**
2667. Create Hello World Function

Write a function createHelloWorld. 
It should return a new function that always returns "Hello World".
 

Example 1:

Input: args = []
Output: "Hello World"
Explanation:
const f = createHelloWorld();
f(); // "Hello World"

The function returned by createHelloWorld should always return "Hello World".
Example 2:

Input: args = [{},null,42]
Output: "Hello World"
Explanation:
const f = createHelloWorld();
f({}, null, 42); // "Hello World"

Any arguments could be passed to the function but it should still always return "Hello World". 

 **/

function sayHelloWorld(){
    return function(...args){
        return "This is a named Function";
    }
};

var sayhello = sayHelloWorld();
console.log(sayhello());

var createHelloWorldAnonymous = function() {
    return function (...args){
        return "Hello World";
    }
};

var createHelloWorldAgain = () => {
    return (...args) => {
        return "Hello World Again";
    }
};

var createHelloWorldArrow = () => (...args) => "Hello World Arrow";

const f = createHelloWorldAnonymous();
console.log(f());              // Hello World
console.log(f(1, 2, 3));       // Hello World
console.log(f({}, null, 42));  // Hello World


const f2 = createHelloWorldAgain();
console.log(f2());              // Hello World
console.log(f2(1, 2, 3));       // Hello World
console.log(f2({}, null, 42));  // Hello World


const f3 = createHelloWorldArrow();
console.log(f3());              // Hello World
console.log(f3(1, 2, 3));       // Hello World
console.log(f3({}, null, 42));  // Hello World