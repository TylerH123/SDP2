var broc = document.getElementById("broc");
var msg = document.getElementById("msg");
var lvl = document.getElementById("lvl");
var coins = document.getElementById("coins");
var up = document.getElementById("up");
var clicker = function() { //function to GROW BROCCOLi
  //console.log(broc + 2);
  //console.log(typeof broc)
  //console.log(parseInt(broc))
  broc.innerHTML = parseInt(broc.innerHTML) + 2 * parseInt(lvl.innerHTML);
  msg.innerHTML = "";
}
var sell = function() { //converts the grown broccoli to coins
  //console.log(document.getElementById("broc").innerHTML)
  //console.log(parseInt(coins.innerHTML) + 1);
  coins.innerHTML = parseInt(coins.innerHTML) + parseInt(broc.innerHTML);
  if (parseInt(broc.innerHTML) == 0){
    msg.innerHTML = "No broccoli to sell...";
  }
  else {
    msg.innerHTML = "Successfully sold " + broc.innerHTML + " broccoli";
    broc.innerHTML = 0;
    $.ajax({
      url: '/makeItRain/sell',
      type: 'GET',
      data: {'coins': coins.innerHTML}
    });
  }
}
var upgrade = function() { //upgrades the farm
  //console.log(coins.innerHTML);
  if (parseInt(coins.innerHTML) >= parseInt(lvl.innerHTML * 200)) {
    coins.innerHTML = parseInt(coins.innerHTML) - parseInt(lvl.innerHTML) * 200;
    lvl.innerHTML++;
    //console.log(lvl.innerHTML);
    up.innerHTML = parseInt(lvl.innerHTML) * 200;
    msg.innerHTML = "Upgrade success";
    //console.log(document.getElementById("lvl").innerHTML);
    $.ajax({
      url: '/makeItRain/upgrade',
      type: 'GET',
      data: {'lvl': lvl.innerHTML, 'coins': coins.innerHTML}
    });
  }
  else {
    msg.innerHTML = "Insufficient funds";
  }
}
var button = document.getElementById("gbutton");
button.addEventListener('click', clicker);
var sbutton = document.getElementById("sellbutton");
sbutton.addEventListener('click', sell);
var ubutton = document.getElementById("upbutton");
ubutton.addEventListener('click', upgrade);
