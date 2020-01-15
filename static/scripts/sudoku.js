var editable = function(e) {
    e.target.setAttribute("contenteditable", "true");
};

var lis = document.getElementsByTagName("td");
var pastErrors = [];

var checkColumn = function(id){
    col = parseInt(id.charAt(1));
    values = []; errors = [];
    for (var i = col; i < lis.length; i += 9){ //goes thru the column
      value = lis[i].innerText;
      if (values.includes(value) && value > 0){ //if the value is not unique then push its id into errors
          errors.push(lis[i].id);
          errors.push("xy".replace('x',values.indexOf(value)).replace('y',col)) //the row/column
      };
      values.push(value);//push the value in the list of values
    };
    return errors; //returns a list of ids with errors
};

var checkRow = function(id){
    row = parseInt(id.charAt(0));
    values = []; errors = [];
    for (var i = (row * 9); i < (row * 9) + 9; i++){
      value = lis[i].innerText;
      if (values.includes(value) && value > 0){ //if the value is not unique then push its id into errors
          errors.push(lis[i].id);
          errors.push("xy".replace('x',row).replace('y', values.indexOf(value))); //the row/column
      };
      values.push(value);//push the value in the list of values
    };
    return errors; //returns a list of ids with errors
};

var findBox = function(id){
    row = parseInt(id.charAt(0));
    col = parseInt(id.charAt(1));
    box = []
    for (var i = 0; i < 3; i++){
      newRow = (Math.floor(row / 3) * 3) + i;
      for (var j = 0; j < 3; j++){
          newCol = (Math.floor(col / 3) * 3) + j;
          box.push(document.getElementById("xy".replace('x', newRow).replace('y', newCol)));
      }
    }
    return box; //returns a list of the elements
}

var checkBox = function(id){
    box = findBox(id);
    values = []; errors = [];
    for (var i = 0; i < box.length; i++){
      value = box[i].innerText;
      if (values.includes(value) && value > 0){ //if the value is not unique then push its id into errors
          errors.push(box[i].id);
          errors.push(box[values.indexOf(value)].id); //the row/column
      };
      values.push(value);
    }
    return errors;
}

var fixErrors = function(){
    fixed = []
    for (var i = 0; i < pastErrors.length; i++){
      if (!checkColumn(pastErrors[i]).includes(pastErrors[i]) && (!checkRow(pastErrors[i]).includes(pastErrors[i])) && !checkBox(pastErrors[i]).includes(pastErrors[i])){
        document.getElementById(pastErrors[i]).style.backgroundColor = 'white';
        fixed.push(pastErrors[i]);
      };
    };
    for (var i = 0; i < fixed.length; i++){
      pastErrors.splice(pastErrors.indexOf(fixed[i]))
    }
};

var checkValid = function(e){
    value = e.target.innerText;
    errors = [];
    if (value > 9 || isNaN(value)){
      e.target.style.backgroundColor = 'red';
    } else {
      e.target.style.backgroundColor = 'white';
    }
    if (value > 0){
        errors = errors.concat(checkColumn(e.target.id));
        errors = errors.concat(checkRow(e.target.id));
        errors = errors.concat(checkBox(e.target.id));
    };
    for (var i = 0; i < errors.length; i++){
      if (!pastErrors.includes(errors[i])){
        pastErrors.push(errors[i]);
      };
      document.getElementById(errors[i]).style.backgroundColor = 'red';
    };
    fixErrors();
};

for (var i = 0; i < lis.length; i++){
    if (lis[i].innerText < 1){
      lis[i].addEventListener('click', editable);
      lis[i].addEventListener('mouseout', checkValid);
    };
};

var checkFinished = function(e){
  for (var i = 0; i < lis.length; i++){
    value = lis[i].innerText;
    if (value < 1){
      document.getElementById("h").innerHTML = "Not finished yet! Keep on going!";
      break;
    };
    if ((value > 1) && (i == lis.length - 1)){
      document.getElementById("h").innerHTML = "COMPLETED!";
    };
  };

}

var button = document.getElementById("b");
button.addEventListener('click', checkFinished);
