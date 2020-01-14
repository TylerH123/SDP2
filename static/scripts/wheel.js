

var a = []; // the array that holds the current numbers that have been spun

var array1 = []; // These 3 arrays are the zero, red and black filling arrays to determine the current colour streaks
var array2 = [];
var array3 = [];

var zero = [0]; // array to check for zeros
var red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 28, 30, 32, 34, 36]; // array to check for reds
var black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 20, 22, 24, 26, 29, 31, 33, 35]; // array to check for blacks

var s = document.getElementById("moneyPouch");
var r = document.getElementById("rollAmount");
// s.innerHTML = "100"; //Initializing your wallet at 100
r.innerHTML = "Round 0"; //Initializing at 0 but cheating through making it a string.
var countClicks = 0; // Used for "rolleAmount" for counting the rounds

function myFunction() {

  var x = document.getElementById("demo"); // Various calls to grab the elements of the HTML DOM
  var y = document.getElementById("results"); //Prints out the current results
  var w = document.getElementById("test"); //
  var t = document.getElementById("colourRows"); // Tells you the current colour streak, eg 4 reds in a row

  var yourBet = document.getElementById("theBet"); //the bet you make

  z = Math.floor(Math.random() * 37); // Random Integer between 0 - 36

  a.push(z);

  if (a.length > 20) {
    a.shift(); // Removes the oldest numbers in the array, taking a max of 20
  }
  var i;
  var text = "";
  for (i in a) {
    text += a[i] + " ";
  }
  w.innerHTML = text; // Prints out the array

  function colourStreak(c) {
    return c == z;

  }

  // Below are the calculations for checking how many of the same colours are in a row (the current streak)

  if (red.find(colourStreak) == undefined && black.find(colourStreak) == undefined) {// zero
    y.innerHTML = zero.find(colourStreak);
    document.getElementById("results").style.color = "green";
    array1.push("zero");
    array2 = [];
    array3 = [];
    t.innerHTML = array1.length + " Green(s) in a row";
  } else if (black.find(colourStreak) == undefined) {// red
    y.innerHTML = red.find(colourStreak);
    document.getElementById("results").style.color = "red";
    array2.push("red");
    array1 = [];
    array3 = [];
    t.innerHTML = array2.length + " red(s) in a row.";
  } else {// black
    y.innerHTML = black.find(colourStreak);
    document.getElementById("results").style.color = "black";
    array3.push("black");
    array1 = [];
    array2 = [];
    t.innerHTML = array3.length + " black(s) in a row.";
  }

  if (array2.length >= 3 || array3.length >= 3) {

  }

  var radioChoice = document.getElementsByName('colour');
  var radio_value;
  for (var j = 0; j < radioChoice.length; j++) {if (window.CP.shouldStopExecution(0)) break;
    if (radioChoice[j].checked) {
      radio_value = radioChoice[j].value;
    }
  }window.CP.exitedLoop(0);

  if (radio_value == "red") {// If Red is checked...
    if (red.find(colourStreak) != undefined) {// If red IS in the array
      s.innerHTML = Number(s.innerHTML) + Number(document.getElementById("theBet").value);
      $.ajax({
        url: '/roulette/change',
        type: 'GET',
        data: {'coins': s.innerHTML}
      }); // Add money
    } else
    {
      s.innerHTML = Number(s.innerHTML) - Number(document.getElementById("theBet").value);
      $.ajax({
        url: '/roulette/change',
        type: 'GET',
        data: {'coins': s.innerHTML}
      }); // Subtract money
    }
  } else
  if (radio_value == "black") {// If Black is checked...
    if (black.find(colourStreak) != undefined) {// If black IS in the array
      s.innerHTML = Number(s.innerHTML) + Number(document.getElementById("theBet").value);
      $.ajax({
        url: '/roulette/change',
        type: 'GET',
        data: {'coins': s.innerHTML}
      }); // Add money
    } else
    {
      s.innerHTML = Number(s.innerHTML) - Number(document.getElementById("theBet").value);
      $.ajax({
        url: '/roulette/change',
        type: 'GET',
        data: {'coins': s.innerHTML}
      }); // Subtract money
    }
  } else
  if (radio_value == "green") {// If green is checked...
    if (zero.find(colourStreak) != undefined) {// If green IS in the array
      s.innerHTML = Number(s.innerHTML) + (17 *(Number(document.getElementById("theBet").value)));
      $.ajax({
        url: '/roulette/change',
        type: 'GET',
        data: {'coins': s.innerHTML}
      });// Add money
    } else
    {
      s.innerHTML = Number(s.innerHTML) - Number(document.getElementById("theBet").value);
      $.ajax({
        url: '/roulette/change',
        type: 'GET',
        data: {'coins': s.innerHTML}
      });// Subtract money
    }
  } else {//If both buttons arent checked (or if None is checked)
    s.innerHTML = Number(s.innerHTML);
    $.ajax({
      url: '/roulette/change',
      type: 'GET',
      data: {'coins': s.innerHTML}
    });
  }

  countClicks++;
  r.innerHTML = "Round " + Number(countClicks);

}
