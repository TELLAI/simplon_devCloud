fetch('http://localhost:5200/real', {mode: 'no-cors'})
  .then(function(data) {
    console.log("salut")
    console.log(data.length)
    console.log(data[3])
    let contain = document.getElementById("mydata");
    for(let i = 0; i < data.length; i++){
        let div = document.createElement("div");
        div.innerHTML = data[i];
        contain.appendChild(div);
    }
});