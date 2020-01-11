function randomnumber(){
  var x = document.getElementById("demo");
  var y = Math.floor(Math.random() * 36);
  x.innerHTML = y;
  if (y == 0)   document.getElementById("demo").style.color = "green";
  if (y % 2 == 1)   document.getElementById("demo").style.color = "red";
  if ((y % 2 == 0) && (y != 0))   document.getElementById("demo").style.color = "black";
  alert("the color is: " + document.getElementById("demo").style.color);
}
var color = document.getElementById("demo").style.color;
var Cred = document.getElementById("red").style.color;
var Cblack = document.getElementById("black").style.color;
var rand = randomnumber;

function bet(a, b){
    if (a === b) document.getElementById("demo").innerHTML = "YOU WIN"
    if (a !== b) document.getElementById("demo").innerHTML = "YOU LOST"

}

var betting = bet;
document.getElementById("1").addEventListener("click", () => console.log(rand()));
document.getElementById("2").addEventListener("click", () => console.log(betting(color,Cred)));
document.getElementById("3").addEventListener("click", () => console.log(betting(color,Cblack)));
