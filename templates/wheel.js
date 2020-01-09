function randomnumber(){
  var x = document.getElementById("demo");
  var y = Math.floor(Math.random() * 36);
  x.innerHTML = Math.floor(Math.random() * 36);
  if (y % 2 == 1) x.innerHTML = y + " RED";
  if (y % 2 == 0) x.innerHTML = y + " BLACK";

}
var rand = randomnumber;
document.getElementById("1").addEventListener("click", () => console.log(rand()));
