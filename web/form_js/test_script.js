let push_name = document.querySelector("#push_name");
let divList = document.querySelector("#divList");
let divGrp = document.querySelector("#divGrp");
let createGrp = document.querySelector("#grpName");
let mixName = document.querySelector("#mixName");
let listName = [];
let nbGrp = 0;
let countGrp = 1;

push_name.addEventListener("click", function() {
    let myName = document.querySelector("#myName").value;
    const exp = new RegExp("^[a-zA-Z]+$");
    if ((exp.test(myName)) && (myName != "")){
        listName.push(myName);
        let oneName = document.createElement("div")
        oneName.innerText += myName;
        divList.appendChild(oneName);
    }
    else{
        alert("Votre saisie est incorrect !");
    }
})

mixName.addEventListener("click", function() {
    console.log(listName);
    listName.sort(function(){return (Math.random() - 0.5)});
    console.log(listName);
})

createGrp.addEventListener("click", function() {
    nbGrp = document.querySelector("#nbGrp").value;
    const exp = new RegExp("^[1-9]+$");
    if(exp.test(nbGrp)){
        let nb_par_grp = Math.floor(listName.length / nbGrp);
        let rest = listName.length % nbGrp;
        
        while(listName.length > 0){
            let newList = document.createElement("div");
            newList.innerText += "Groupe " + countGrp + " : \n";
            let count = 0
            
                if (nbGrp > 1){
                    while(count < nb_par_grp){
                        newList.innerText += listName.pop() + "\n";
                        count++;
                    }                    
                }
                else if (nbGrp == 1){
                    while (count < (rest + nb_par_grp)) {
                    
                        newList.innerText += listName.pop() + "\n";
                        count++;
                    }
                }
                divGrp.appendChild(newList);
                countGrp++;
                nbGrp--;
        }
        
    }
    else{
        alert("Votre saisie est incorrect !")
    }
})
