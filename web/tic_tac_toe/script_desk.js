let btn_desk = document.querySelector("#desktop");

let list_carre_2 = document.querySelectorAll(".carre_2");
let containeur_2 = document.querySelector("#main_2");
let player = ["", ""];
let list_copy = [0, 1, 2, 3, 4, 5, 6, 7, 8];
let list_index = [];

btn_desk.addEventListener("click", function () {
  player[0] = "O";
  player[1] = "X";
  containeur_1.style.display = "none";
  containeur_2.style.display = "grid";
  console.log(list_carre_2);
});

function recup_index_vide(list_copy) {     /* fonction qui mélange la liste d'index vide et qui retourne un index */
  list_copy.sort(function () {
    return Math.random() - 0.5;
  });
  return list_copy;
}
function case_vide(){
    for (item of list_carre_2){
        if (item.innerText == ""){
            return true;
        }
    }
    return false;
}
function reset_case(){
    for(item of list_carre_2){
        item.innerText = "";
    }
    list_copy = [0, 1, 2, 3, 4, 5, 6, 7, 8];
}
function reset_game(){
    reset_case();
    player = ["", ""];
}

for (let i = 0; i < list_carre_2.length; i++) {
  list_carre_2[i].addEventListener("click", function () {
    if (player[0] != "" && player[1] != ""){
        if (case_vide() && !winner()) {
        this.innerText = player[0];
        list_index.push(list_copy.splice(list_copy.indexOf(i), 1));
        if (case_vide() && !winner()) {
            j = recup_index_vide(list_copy)[0];
            list_carre_2[j].innerText = player[1];
            list_index.push(list_copy.splice(0, 1));
        } else if (!case_vide() && !winner()) {
            setTimeout(function () {
            reset_case();
            }, 10);
        }
        else{
            reset_game();
        }
        } 
        else {
        setTimeout(function () {
            reset_case();
        }, 10);
        }
    }
    else {
        alert("Veuillez choisir un mode de jeu");
    }
  });
}
function recupe(n) {
   /* fonction qui recuperer la valeur de la case */
  return list_carre_2[n].innerText;
}
function winner() {
  /* fonction qui teste si on a une combinaison gagnante */
  for (let i of player) {
    if (recupe(0) == i && recupe(1) == i && recupe(2) == i) {
      alert("le Joueur jouant avec " + i + " a gagné");
      display_score(i)
      return true;
    } else if (recupe(3) == i && recupe(4) == i && recupe(5) == i) {
      alert("le Joueur jouant avec " + i + " a gagné");
      display_score(i)
      return true;
    } else if (recupe(6) == i && recupe(7) == i && recupe(8) == i) {
      alert("le Joueur jouant avec " + i + " a gagné");
      display_score(i)
      return true;
    } else if (recupe(0) == i && recupe(3) == i && recupe(6) == i) {
      alert("le Joueur jouant avec " + i + " a gagné");
      display_score(i)
      return true;
    } else if (recupe(1) == i && recupe(4) == i && recupe(7) == i) {
      alert("le Joueur jouant avec " + i + " a gagné");
      display_score(i)
      return true;
    } else if (recupe(2) == i && recupe(5) == i && recupe(8) == i) {
      alert("le Joueur jouant avec " + i + " a gagné");
      display_score(i)
      return true;
    } else if (recupe(0) == i && recupe(4) == i && recupe(8) == i) {
      alert("le Joueur jouant avec " + i + " a gagné");
      display_score(i)
      return true;
    } else if (recupe(2) == i && recupe(4) == i && recupe(6) == i) {
      alert("le Joueur jouant avec " + i + " a gagné");
      display_score(i)
      return true;
    }
  }
  return false;
}

function display_score(e){
    let quote = " : ";
    if (e == "X") {
      countp1 += 1;
      document.getElementById("score").innerText = countp1 + quote + countp2;
      console.log(countp1);
    } else if ((e = "O")) {
      countp2 += 1;
      document.getElementById("score").innerText = countp1 + quote + countp2;
      console.log(countp2);
    }
}