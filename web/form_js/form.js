let listName = [];
let myP = document.querySelector("#myP");

document.querySelector("#push").addEventListener("click", function() {
    let myName = document.getElementById("#fname");
    myP.innerText = myName;
})