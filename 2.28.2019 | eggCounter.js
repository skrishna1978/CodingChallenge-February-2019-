2.28.2019 - shashi<br>
Ronald's uncle left him 3 fertile chickens in his will. When life gives you chickens, you start a business 
selling chicken eggs which is exactly what Ronald decided to do.A chicken lays 300 eggs in its first year. 
However, each chicken's egg production decreases by 20% every following year (rounded down) until when it 
dies (after laying its quota of eggs).
After his first successful year of business, Ronald decides to buy 3 more chickens at the start of each year. 
<br><br>
<b>Your Task:</b><br>
For a given [YEAR], and life span of chicken [SPAN], calculate how many eggs Ronald's chickens will 
lay him that year, whereby year=1 is when Ronald first got his inheritance and span>0.
<br><br>If year=0, make sure to return "No chickens yet!".
<p id = "code"></p>
<script>

function eggCount(year,span) 	//function accepts year and span
{ 
  if (year<=0) return 'No chickens yet!';	//error check
  	
  var chickens = 3;  			//base value for chickens
  var eggProduction = 0;		//eggCount
  var maxPerYear = 300;			//eggs produced by a chicken per year
  
  var productiveYears = Math.min(year, span);	//get the least value 
  
  while(productiveYears>=1) {							//loop under years are !=0
    eggProduction += maxPerYear * chickens;				//total for egg production/chicken x chicken Count
    productiveYears--;									//reduce years
    maxPerYear = Math.floor(maxPerYear * 0.8);			//reduce years by 20%.
 }//end of loop
   return eggProduction; //return final value back.
}

document.getElementById("code").innerHTML = "2,1 is " + eggCount(2,1) + "<br>";
document.getElementById("code").innerHTML += "3,3 is " + eggCount(3,3) + "<br>";
document.getElementById("code").innerHTML += "0,4 is " + eggCount(0,4) + "<br>";
document.getElementById("code").innerHTML += "2,3 is " + eggCount(2,3) + "<br>";
</script>
