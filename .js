async function product(a,b){
    let response = await a*b;
    display(response);
}
function display(some) {    
    console.log(some);
}
product(5, 10);