var button = document.getElementById("roll");
button.addEventListener('click', rand);

var rand = function(){
  var num1 = Math.floor(Math.random() * 5 + 1);
  var num2 = Math.floor(Math.random() * 5 + 1);
  ele.innerHTML = fib(len);
  console.log(num1 + " " + num2);
}
