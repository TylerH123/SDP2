// var phase = 1;
// var point = 0;
//
// var roll = function(e){
//   var dieOne = Math.floor(Math.random() * 6 + 1);
//   var dieTwo = Math.floor(Math.random() * 6 + 1);
//   var dice = dieOne+dieTwo;
//   document.getElementById("dieOne").innerHTML = dieOne;
//   document.getElementById("dieTwo").innerHTML = dieTwo;
//   if (phase == 1){
//     if (dice == 7){
//       document.getElementById("winLose").innerHTML = "Win";
//     }
//     else if (dice == 11){
//       document.getElementById("winLose").innerHTML = "Win";
//     }
//     else if (dice == 2){
//       document.getElementById("winLose").innerHTML = "Lose";
//     }
//     else if (dice == 3){
//       document.getElementById("winLose").innerHTML = "Lose";
//     }
//     else if (dice == 12){
//       document.getElementById("winLose").innerHTML = "Tie";
//     }
//     else{
//       document.getElementById("winLose").innerHTML = "Point Number is " + dice;
//       point = dice;
//       phase++;
//       document.getElementById("round").innerHTML = phase;
//     }
//   }
//   else{
//     if (dice == point){
//       document.getElementById("winLose").innerHTML = "Win";
//       phase = 1;
//       document.getElementById("round").innerHTML = phase;
//     }
//     else if (dice == 7){
//       document.getElementById("winLose").innerHTML = "Lose";
//       phase = 1;
//       document.getElementById("round").innerHTML = phase;
//     }
//     else{
//       document.getElementById("winLose").innerHTML = "Tie";
//     }
//   }
// }
//
// document.getElementById("rollDice").addEventListener("click", roll);
//
//




var elDiceOne = document.getElementById('dice1');
var elDiceTwo = document.getElementById('dice2');
var elComeOut = document.getElementById('comeOutButton');
var elPointRoll = document.getElementById('pointRollButton');
var elWinOrLoss = document.getElementById('winOrLoss');
var elCrapsWins = document.getElementById('crapWins');
var elCrapsLosses = document.getElementById('crapLosses');


elComeOut.onclick = function () {comeOutRoll();};

elPointRoll.onclick = function () {pointRoll();};

// Come Out Roll Function
function comeOutRoll() {

  // Initial dice variables
  var diceOne = Math.floor(Math.random() * 6 + 1);
  var diceTwo = Math.floor(Math.random() * 6 + 1);
  var rollTotal = diceOne + diceTwo;

  // console.log(rollTotal + ' ' + diceOne + ' ' + diceTwo);
  elDiceOne.classList.toggle('animate');
  elDiceTwo.classList.toggle('animate');

  //Dice reset and display
  for (var i = 1; i <= 6; i++) {if (window.CP.shouldStopExecution(0)) break;
    elDiceOne.classList.remove('show-' + i);
    if (diceOne === i) {
      elDiceOne.classList.add('show-' + i);
    }
  }window.CP.exitedLoop(0);

  for (var k = 1; k <= 6; k++) {if (window.CP.shouldStopExecution(1)) break;
    elDiceTwo.classList.remove('show-' + k);
    if (diceTwo === k) {
      elDiceTwo.classList.add('show-' + k);
    }
  }

  // if rollTotal = 7 or 11; Player wins
  window.CP.exitedLoop(1);if (rollTotal === 7 || rollTotal === 11) {
    console.log('You won!');
    elWinOrLoss.innerHTML = 'You Won!';

    // cash += betField;
  } else if (rollTotal === 2 || rollTotal === 3 || rollTotal === 12) {
    console.log('You lost!');
    elWinOrLoss.innerHTML = 'LOSER!';

    // cash -= betField;
  } else {
    // sets the point and changes button display
    thePoint = rollTotal;
    elWinOrLoss.innerHTML = 'Roll the Point!';

    //  sets value for the point and changes the button displayed
    document.getElementById('theRoll').innerHTML = 'Roll a ' + thePoint + ' to win';
    elComeOut.style.display = 'none';
    elPointRoll.style.display = 'block';
  }

  setTimeout(winLossCount(), 1500);
} // END Come out roll function

//POINT ROLL FUNCTION
function pointRoll() {

  // sets dice variables
  var diceOne = Math.floor(Math.random() * 6 + 1);
  var diceTwo = Math.floor(Math.random() * 6 + 1);
  var rollTotal = diceOne + diceTwo;

  //Dice reset and display

  for (var i = 1; i <= 6; i++) {if (window.CP.shouldStopExecution(2)) break;
    elDiceOne.classList.remove('show-' + i);
    if (diceOne === i) {
      elDiceOne.classList.add('show-' + i);
    }
  }window.CP.exitedLoop(2);

  for (var k = 1; k <= 6; k++) {if (window.CP.shouldStopExecution(3)) break;
    elDiceTwo.classList.remove('show-' + k);
    if (diceTwo === k) {
      elDiceTwo.classList.add('show-' + k);
    }
  }

  // if player rolls a 7, player loses
  window.CP.exitedLoop(3);if (rollTotal === 7) {
    console.log('LOSER');
    thePoint = 0;
    lossCount++;
    gameCount++;
    elWinOrLoss.innerHTML = 'Loser!';

    // cash -= betField;
    elComeOut.style.display = 'block';
    elPointRoll.style.display = 'none';

  } else if (rollTotal === thePoint) {
    // If player rolls the point; player wins

    console.log('you won!');
    winCount++; // updates win count
    gameCount++;
    elWinOrLoss.innerHTML = 'You Won!';

    // cash += betField;
    thePoint = 0; // resests the point

    // Resets buttons
    elComeOut.style.display = 'block';
    elPointRoll.style.display = 'none';

  } else {
    // Roll again if no winner

    console.log('roll again');
  }

  setTimeout(winLossCount(), 1500);
} // END POINT ROLL FUNCTION

function winLossCount() {
  // Update win and loss count
  elCrapsLosses.innerHTML = 'Losses: ' + lossCount;
  elCrapsWins.innerHTML = 'Wins: ' + winCount;

  // document.getElementById('score').innerHTML = 'CASH:' + cash;
}
//# sourceURL=pen.js
