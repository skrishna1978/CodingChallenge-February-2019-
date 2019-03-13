2.21.2019 - shashi<br>
Program that accepts a paragraph and prints out how many sentences it has. 
Count is based on periods (.), question marks (?) and exclamation marks (!)<br>

<p id = "code"></p>
<script>
function sentenceCount(string) { //get the para here
  //regular expression comparison allows for quicker/efficent search based on symbols.
  //the pattern being looked for is enclosed within / / slashes.
  //symbols being searched for are . ? and !
  // /g is looking for a global match in the input for these symbols.
  //when found, load all the symbols into an array [] and get its length (ergo: sentence count).
  
  var matchArray = string.match(/\.|\?|!/g);
  return matchArray.length;
}

var para = "Hey! How are you? Long time! Hope all is well.";
document.getElementById("code").innerHTML = para + "= " +sentenceCount(para) + " sentences.<br><br>";
para = "hey there! i have been well. thanks. lots happening at work. hows the baby doing? how old is she now? two, right?";
document.getElementById("code").innerHTML += para + "= " +sentenceCount(para) + " sentences.<br>";

</script>
