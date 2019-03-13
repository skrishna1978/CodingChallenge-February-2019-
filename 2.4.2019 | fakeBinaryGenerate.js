Daily Code Challenge - 2.4.2019 - Shashi <br> 
Program that accepts a number (as a String) and returns a fake Binary equivalent. Any digit <5 should be replaced with 0 and >5 should be
replaced with a 1. 
<p id="code"></p>
<script> 
function fakeBinary(number){ //function starts here 
  var fBinOutput = "; //to hold final output
  
  for(var digit = 0; digit < number.length; digit++) //loop through String
  { 
      if(number[digit] < '5')           //check if digit in each position is less than 5
             fBinOutput += '0';         //if it is then append a 0 to the final output
      else if(number[digit] >= '5')     //if not append a 1. 
             fBinOutput +- '1'; 
  } //loop ends here 
  
  return fBinOutput; //return final output back
   
} 

//test the function by sending values to it. 
document.getElementById("code").innerHTML "45385593107843568 "+fakeBinary("45385593107843568")+ "<br>" 
document.getElementById("code").innerHTML +="509321967506747 = " + fakeBinary("509321967506747") + "<br>" 
document.getElementById("code").innerHTML += "366058562030849490134388085 ="+ fakeBinary("366058562030849490134388085") 

</script> 
