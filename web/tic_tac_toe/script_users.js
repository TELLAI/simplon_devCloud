/*
push.addEventListener("click", function() {
    let newL = document.createElement("div");
    newL.innerHTML = '<i class="fas fa-times"></i>';
    push.appendChild(newL);
})*/

// Ajout Marwa

//Selectionner tout les carre pour faire une liste

let X = '<i class="fas fa-times"></i>';
let O = '<i class="far fa-circle"></i>';
let cell = (n) => carre_list[n].innerText; //recupere text

let countp1 = 0;
let countp2 = 0;
let carre_list = document.querySelectorAll(".carre_1"); //selectorAll renvoie liste
let player_one = false; //permet de differencier player_one et player_two. L'un reste faux, l'autre est vrai
let stop_play = false;
let btn_user = document.querySelector("#users");
let containeur_1 = document.querySelector("#main_1");

btn_user.addEventListener("click", function () {
  containeur_1.style.display = "grid";
  containeur_2.style.display = "none";
});

function fswitch() {
  if (!player_one) {
    document.getElementById("carrep1").innerText = "X";
    document.getElementById("carrep2").innerText = "";
  }
  if (player_one) {
    document.getElementById("carrep1").innerText = "";
    document.getElementById("carrep2").innerText = "O";
  }
}

for (let item of carre_list) {
  /* cette for loop permet de parcourir une liste */
  item.addEventListener("click", (e) => {
    /* permet de cibler un carre specfique où cliquera l'user */

    if (!player_one) {
      item.innerText = "X"; /*<i class="fas fa-times"></i> (a ajouter) */
      player_one = true;
      fswitch();
      /* !player_one = player_two --> c'est pour ça que la condition change*/
      /* on renvoie un X  */
    } else if (player_one) {
      item.innerText = "O";
      player_one = false; /*'<i class="far fa-circle"></i>'*/
      fswitch();
    }
    /* on ré affirme condition = false pour avoir une alternance O / X */

    // https://stackoverflow.com/questions/40724697/javascript-do-something-before-alert

    setTimeout(function () {
      fswitch();
      win();
    }, 10);
  });
}

document.querySelector("#reset").addEventListener("click", function () {
  reset();
});

function reset() {
  for(item of carre_list){
        item.innerText = "";
    }
}
/*appelle l'index de la liste des carre, 
selectionne n pour basculer de "X" à "O", 
inner text pour renvoyer la valeur*/

function win() {
  let players = ["X", "O"];
  players.forEach((e) => {
    function display_player() {
      let quote = " : ";
      if (e == "X") {
        alert("Player one :" + " You're the winner ! :) ");
        countp1 += 1;
        document.getElementById("score").innerText = countp1 + quote + countp2;
        console.log(countp1);
        reset();
      } else if ((e == "O")) {
        alert("Player two :" + " You're the winner ! :) ");
        countp2 += 1;
        document.getElementById("score").innerText = countp1 + quote + countp2;
        console.log(countp2);
        reset();
      }
    }

    if (cell(0) == e && cell(1) == e && cell(2) == e) {
      display_player();
    } else if (cell(3) == e && cell(4) == e && cell(5) == e) {
      display_player();
    } else if (cell(6) == e && cell(7) == e && cell(8) == e) {
      display_player();
    } else if (cell(0) == e && cell(3) == e && cell(6) == e) {
      display_player();
    } else if (cell(1) == e && cell(4) == e && cell(7) == e) {
      display_player();
    } else if (cell(2) == e && cell(5) == e && cell(8) == e) {
      display_player();
    } else if (cell(0) == e && cell(4) == e && cell(8) == e) {
      display_player();
    } else if (cell(0) == e && cell(4) == e && cell(8) == e) {
      display_player();
    } else if (cell(2) == e && cell(4) == e && cell(6) == e) {
      display_player();
    } else {
      let i = 0;
      for (let item of carre_list) {
        console.log(item, item.innerText);
        if (item.innerText != "") {
          i++;
        }
        if (i == 9) {
          alert("Egality:) ");
          reset();
        }
      }
    }
  });
}

/*

Etape 1 : selectionner les carre pour en faire une liste
Etape 2: mettre une dition pour differencier joueur 1 et jour 2
Etape 3: click event, variable avec un if statement pour que la croix ou le rond d'affiche
Etape 4: changer la condition de joueur pour avoir une alternance "O" et "X"
Etape 5: Appeler l'index de la liste des carre pour voir si ce qu'il revoie est un X ou un O
Etape 6: avoir une vaiable  = ["X", "O"] pour voir leurs comportement
Etape 7: faire un forEach de la variable et faire des if statements pour voir si chaque ligne et colonne possede le meme element.
Etape 8: si c'est le cas, fin du jeu, le joeur à gagner

*/
