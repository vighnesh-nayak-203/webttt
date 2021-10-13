function retval(i){
    return document.getElementById(i).textContent;
}
let wincombs=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]];
function wincheck(){
    let pl1n=document.getElementById("pl1n").textContent;
    let pl2n=document.getElementById("pl2n").textContent;
    let pl1s=document.getElementById("pl1s").textContent;
    let pl2s=document.getElementById("pl2s").textContent;
    let alert=document.getElementById("alert")
    let winner="";
    for(let j=0;j<8 ;j++){
        i=wincombs[j];
        if((retval(i[0])==retval(i[1]) && retval(i[0])==retval(i[2])) && !(retval(i[0])=="")){
            if(retval(i[0])==pl1s){
                winner=pl1n
            }else{
                winner=pl2n
            }
            alert.textContent=winner+" won";
            break
        }
    }
}
let c=1
function play(i){
    let pl1s=document.getElementById("pl1s").textContent;
    let pl2s=document.getElementById("pl2s").textContent;
    let alert=document.getElementById("alert")
    var b=document.getElementById(i);
    if(b.textContent==""){
        if(c%2==1){
            b.textContent=pl1s
        }else{
            b.textContent=pl2s
        }
        c=c+1
        alert.textContent=""
    }else{
        alert.textContent="preoccupied,choose other."
    }
    wincheck();
};