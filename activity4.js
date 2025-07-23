// callback = function

// definition of sum function
function sum(a ,b,c){ // container (a, b, c) for parameters
    console.log( a + b )
    c() //calling the callback function
    
}

function example(){ // definition part of call back function
    console.log("This is a callback function");

}
//calling main sum function
// a   b   c(callback given)
sum(10 , 30, example) // real value will change the answer

