Daily Code Challenge - 2.18.2019 - shashi <br>
Program that accepts money total and coin denominations available. Then it returns the number of ways
that total can be changed. For ex: If you had 1 and 2 denomination coins of any currency (I am using ₹)
then how many ways are there are to convert that to 4? Order does not matter. So:<br>
1+1+1+1 = 4<br>
2+2 = 4<br>
2+1+1 = 4<br>
Hence, 3 ways. <br>

<p id = "code"></p>
<script>
function changeCounter(totalAmount, coinDenominations) { //function starts here

var denomArray = new Array(totalAmount + 1).fill(0); //make an array of (totalAmount +1) elements and fill it with 0s
  denomArray[0] = 1;							     //make the first element in the array a 1
  
  for (var eachDenom in coinDenominations) {		//loop through denomination array			
    for (var loop = coinDenominations[eachDenom]; loop <= totalAmount; loop++) {   //inner loop to traverse coinDenom array
     //limiting it to the total amount required.
     //The idea here is that totalAmount is assigned an index in denomArray to hold the # of ways changes can be created
     denomArray[loop] += denomArray[loop - coinDenominations[eachDenom]];  //Ex: [0]1  [1]1  [2]2  [3]2   [4]3
    } //inner loop ends
  }//outer loop ends
  
 return denomArray[totalAmount]; //return total summed up for the index that matches total amount
}

document.getElementById("code").innerHTML = "Change 4₹ (1₹ and 2₹ coins) = " +changeCounter(10, [5,2]) + " ways<br>";
document.getElementById("code").innerHTML += "Change 10₹ (5₹ and 2₹ coins) = " +changeCounter(10, [5,2]) + " ways<br>";
document.getElementById("code").innerHTML += "Change 18₹ (10₹ and 2₹ coins) = " +changeCounter(10, [5,2]) + " ways<br>";
</script>
