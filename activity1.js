// js obj
const student = {
    name: "Tanishka",
    age: 17,
    subjects: ["math", "science", "english"],
};


//convert object to JSON ( sending end )
const studentJSON = JSON.stringify(student);
console.log("JSON format:", studentJSON);

//convert JSON back to an object ( receiving end )
const studentObj = JSON.parse(studentJSON);
console.log("javascript object:", studentObj.name);

