Daily Code Challenge - 2.11.2019 - shashi <br>
Program that takes a String and returns all positions that contain UPPERCASE letters.

<p id = "code"></p>
<script>
function capitalPositions(sentence) {  //function starts here
  var locationsArray = []; //empty array for position numbers
  
  for (var letter = 0; letter < sentence.length; letter++) { //loop through sentence
    if (sentence[letter].toUpperCase() == sentence[letter] && sentence[letter]!= " ") //if uppercase letter found
    	//push it into array
      	locationsArray.push(letter); //(letter+1) for actual position while reading, not array.  
  }//end of for loop

  return locationsArray; //return array back to calling function
} //end of function

document.getElementById("code").innerHTML = "hellO World = " +capitalPositions('hellO World') + "<br>"; 
document.getElementById("code").innerHTML +="This Is A tEsT = "+ capitalPositions('This Is A tEsT')+ "<br>";
document.getElementById("code").innerHTML += "SAMple woRD = "+ capitalPositions('SAMple woRD'); 

</script>
