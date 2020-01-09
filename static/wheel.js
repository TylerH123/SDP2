function randomnumber(){
  var x = document.getElementById("demo");
  var y = Math.floor(Math.random() * 36);
  x.innerHTML = Math.floor(Math.random() * 36);
  if (y % 2 == 1)   document.getElementById("demo").style.color = "#ff0000";
  if (y % 2 == 0)   document.getElementById("demo").style.color = "#000000";

}
var rand = randomnumber;
document.getElementById("1").addEventListener("click", () => console.log(rand()));
