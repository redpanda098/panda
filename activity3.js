
//               resolve and reject
new Promise((res, rej) => {
    a = false
    if(a){
        res("data fetched")
    }else{
        rej("error")
    }    
})
.then((data) => console.log(data))
.catch((err) => console.log(err));