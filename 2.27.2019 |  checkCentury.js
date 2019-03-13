2.27.2019 - shashi<br>
Program that accepts a year and prints out the century that year belongs to.

<p id = "code"></p>
<script>
function checkCentury(year)  //function starts here
{
 if (year<0) return year + " is an invalid year!";  //error check
 var century = String(Math.ceil(year / 100));  //get century number
 
 if(century>10 && century<20)
  century = century + "th "    //any value between 11 and 19 automatically is suffixed "th"
else{
 var secondDigit = century%10;    //get the 2nd digit from century number
 if(secondDigit == 1) century = century + "st "  //add "st" if 1
 if(secondDigit == 2) century = century + "nd "  //add "nd" if 2
 if(secondDigit == 3) century = century + "rd "  //add "rd" if 3
 if(secondDigit > 3)  century = century + "th "  //add "th" for all >3 values
 } //end of IF
 
 return year + " belongs to " + century + " century";  //return formatted message
}

//testing the function with different values.
document.getElementById("code").innerHTML = checkCentury(-19) + "<br>";
document.getElementById("code").innerHTML += checkCentury(2019) + "<br>";
document.getElementById("code").innerHTML += checkCentury(1867) + "<br>";
document.getElementById("code").innerHTML += checkCentury(1234) + "<br>";
document.getElementById("code").innerHTML += checkCentury(123) + "<br>";
document.getElementById("code").innerHTML += checkCentury(210) + "<br>";

</script>
