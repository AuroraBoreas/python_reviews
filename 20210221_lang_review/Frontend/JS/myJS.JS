console.log("hello world");

var header = document.querySelector("header");
console.log(header.innerHTML);

header.addEventListener((e)=>{
    console.log("event listner", e.target);
}, this);