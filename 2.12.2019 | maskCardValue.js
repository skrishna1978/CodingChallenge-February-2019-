Daily Code Challenge - 2.12.2019 - shashi <br>
Program that accepts a 16 digit number (as String) and converts all of it to # except the 
last 4 digits. Sort of like masking a credit card number.

<p id = "code"></p>
<script>
function maskValue(cardNumber) //function starts here
{
	//STEP 1: check if its all numbers
    if(isNaN(cardNumber)==true || cardNumber.length!=16) //check if its all numbers of size 16
    { return "Invalid Value"; } //if either of them is TRUE then return error
   
   else {  
    var i=0;	//else keep a counter
    	while(i<cardNumber.length-4)	//loop from first position till (last position - 4)
    	{
        	cardNumber=cardNumber.replace(cardNumber[i],'#');	//replace number with #
        	i++;			//move forward
    	}//end of while loop
        return cardNumber; //return final masked number
    } //end of else
} //end of function

document.getElementById("code").innerHTML = maskValue("6011920613080285") + "<BR>"
document.getElementById("code").innerHTML += maskValue("1") + "<BR>"
document.getElementById("code").innerHTML += maskValue("Mixed 124 text.") + "<BR>"
document.getElementById("code").innerHTML += maskValue("5160099401494817") + "<BR>"
</script>
