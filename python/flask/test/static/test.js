
// fetch("http://127.0.0.1:5200/real")
//   .then(function(data) {
//     console.log(data.length)
//     document.getElementById("mydata").innerHTML = "salut"
//   })
// let buttEquipe = document.getElementById("Equipe") let url = "http://127.0.0.1:5200/"
// buttEquipe.addEventListener("click", function(){
//   url = url + "Equipe"
// })
// $.ajax({
//   url: "http://127.0.0.1:5200/Equipe",
//   success: display_news
// });
// $.ajax ({
//   url: "http://127.0.0.1:5200/search?equipe1=real&equipe2=inter",
//   success: display_news
// });

// function display_news(result){
//   console.log("coucou")
//   data1 = result[0]
//   data2 = result[1]
//   console.log(data1)
//   console.log(data2)
//   contain = document.getElementById("mydata")
//   for (let i = 0; i < result.length; i++){
//     mydiv = document.createElement("div")
//     mydiv.innerHTML = result[i]
//     contain.appendChild(mydiv)
//   }
// }
let buttEquipe = document.querySelector("#push");
let displayEquipe = document.getElementById("team_search");

 $.ajax({
   url: "http://127.0.0.1:5200/Equipe",
   success: display_search
  });
function display_search(){
buttEquipe.addEventListener("click", function(){
  // url_now = url_now + "Equipe";
  console.log("url_now");
})}