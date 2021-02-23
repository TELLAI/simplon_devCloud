 
 $.ajax ({
   url: "http://127.0.0.1:5200/Equipe?equipe=atl",
   success: display_news
 });

 function display_news(result){
   let contain = document.getElementById("mydata")
   for (let i = 0; i < result.length; i++){
    data = result[i]
    console.log(data)
    let mydiv = document.createElement("div");
    let num = i + 1
    let className = "line" + num.toString()
    mydiv.setAttribute("id", className)
    contain.appendChild(mydiv);
    let contain_1 = document.getElementById(className)
    for(let j = 0; j < data.length; j++){
        let mydiv_1 = document.createElement("div")
        num = j + 1
        mydiv_1.setAttribute("class", "data")
        mydiv_1.innerHTML = data[j]
        contain_1.appendChild(mydiv_1);
    }
   }
 }


 
