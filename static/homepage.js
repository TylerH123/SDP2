var rand = function(){
  var num1 = Math.floor(Math.random() * 5 + 1);
  var num2 = Math.floor(Math.random() * 5 + 1);
  var ele = document.getElementById("nums");
  ele.innerHTML = num1 + " " + num2;
}

var button = document.getElementById("roll");
button.addEventListener('click', rand);
