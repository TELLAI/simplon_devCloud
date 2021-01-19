let listName = [];
let divList = document.querySelector(".list");
let divGrp = document.querySelector(".grp");


function create_list() {
  let myName = document.querySelector("#name").value;
  listName.push(myName);
  let mylist = document.createElement("div");
  mylist.innerText += myName + "\n";
  divList.appendChild(mylist);
}
function swapArray(array) {
  for (var i = array.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }
}
let new_grp = [];
let nb_par_grp = document.querySelector("#nb_grp").value;
function nb_input() {
  
  let exp=new RegExp("[0-9]");
  nb_par_grp = parseInt(nb_par_grp);

  if (exp.test(nb_par_grp) == true) {
    create_grp();
  } else {
    //alert("Attention, votre saisie est incorrect !");
  }
  swapArray(listName);
  return nb_par_grp;
}
console.log(listName);
console.log(nb_par_grp);
//let nb_par_grp = nb_input();
function create_grp() {
    let count_Grp = 1;
  while (listName.length > 0) {
    let myGrp = document.createElement("div");
    myGrp.innerText += "Groupe" + count_Grp + " : " + "\n";
    new_grp = listName.splice(0, nb_par_grp);

    for (var i = 0; i < new_grp.length; i++) {
      myGrp.innerText += new_grp[i] + "\n";

      divGrp.appendChild(myGrp);
    }
    count_Grp++;
  }
}
console.log(nb_par_grp);

function app_delete() {
  let deleteList = listName.splice(0, listName.length);
  deletelist = new_grp.splice(0, new_grp.length);
  divGrp.innerText = new_grp;
  divList.innerText = new_grp;
}
