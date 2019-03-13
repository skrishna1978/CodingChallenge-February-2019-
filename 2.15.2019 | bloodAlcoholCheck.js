Daily Code Challenge - 2.15.2019 - shashi <br>
Program that accepts alcohol consumed (in ounces), body weight (lbs), gender and time passed since drinking (hours). <br>
<br>Alcohol consumed will be passed as a drinks object with two properties: ounces (the total volume of 
beverage consumed in ounces), and abv (the % of alcohol by volume of the beverage as a floating point number--
such as 0.05 for 5% abv beer or 0.4 for 40% abv whisky). <br><br>
The gender will be passed as a string, either "male" or "female".<br><br>
Output must be returned as a number data-type, greater than or equal to 0, with up to 4 decimal places. 
No error handling will be required.

<p id = "code"></p>
<script>
//function begins here
function bloodAlcoholContent(drinks, weight, sex, time){
  this.drinks = drinks; //set object value to current
  this.weight = weight; //set object value to current
  this.sex = sex;  	    //set object value to current
  
  if (sex == 'male') {   //if gender is MALE
    sex = 0.73;          //calculated value based on gender    
  } else if (sex == 'female') {   
    sex = 0.66;           //if gender is FEMALE
  };
  
  this.time = time;     
  var level = drinks.ounces * drinks.abv * 5.14 / weight * sex - 0.015 * time;
  return Number(level.toFixed(2));
}

document.getElementById("code").innerHTML = "Blood Alcohol Level = "+ bloodAlcoholContent({ounces:12.5, abv:0.4}, 190, 'male', 1) + "<BR>"
document.getElementById("code").innerHTML += "Blood Alcohol Level = "+ bloodAlcoholContent({ounces:15.0, abv:0.4}, 175, 'female', 2) + "<BR>"
</script>
