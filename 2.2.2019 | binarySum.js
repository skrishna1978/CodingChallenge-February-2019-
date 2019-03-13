Daily Code Challenge - 2.2.2019 - shashi<br>
Program accepts 2 numbers and returns its sum in Binary.<br>

<p id = "code"></p>
<script>
function binarySum(num1,num2){   //function starts here
  var sum = num1 + num2, bSumStr = '';  //declare variables here

  while (sum > 0) { //as long as sum remains positive
    bSumStr = (sum % 2) + bSumStr;	//get remainder of division by 2 and add to bSumStr
    sum = Math.floor(sum / 2);	//re-calculate sum to reduce it
  }//end of loop
  
  return bSumStr; //return final value back.
}

document.getElementById("code").innerHTML = "1+2 = 3  >> " + binarySum(1,2) + "<br>";
document.getElementById("code").innerHTML += "4+5 = 9  >> " + binarySum(4,5);
</script>
