var nums = {
	"roll1":"",
	"roll2":""
};

var rand = function(){
  var num1 = Math.floor(Math.random() * 6 + 1);
  var num2 = Math.floor(Math.random() * 6 + 1);
  var ele = document.getElementById("nums");
  ele.innerHTML = num1 + " " + num2;
  nums["roll1"] = num1;
  //console.log("num1: " + num1 + " nums[roll1]: " + nums["roll1"]);
  nums["roll2"] = num2;
  //console.log(JSON.stringify(nums));
	$.ajax({
    url: '/dice',
    type: 'POST',
    data: JSON.stringify(nums),
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    async: false,
  });
}

var button = document.getElementById("roll");
button.addEventListener('click', function(){rand()});
