Daily Code Challenge - 2.6.2019 - Shashi <br>
Program that accepts a number, converts it to Binary and returns the count of 1s in it.

<p id = "code"></p>
<script>
function countBits(n) {
   var base = (n).toString(2).split(''); //convert number to Binary and store in array
   var count = 0; //to hold 1 countsjavascript:;
   for (var i = 0; i < base.length; i++) //loop through array
        if(base[i]=='1') count++;  //if 1 found, add to counter

	return count; //return final count back
} //end of function

function decToBin(num){ //function that converts integer to Binary
    return (num >>> 0).toString(2); 
     } //end of function
//Testing out the functions
document.getElementById("code").innerHTML =  "1234 = " + decToBin(1234) + " = " + countBits(1234) + " 1-bits" + "<br>";
document.getElementById("code").innerHTML +=  "77 = " + decToBin(77) + " = " + countBits(77) + " 1-bits"+ "<br>";
document.getElementById("code").innerHTML +=  "901 = " + decToBin(901) + " = " + countBits(901) + " 1-bits";
</script>
</p>
