#2.17.2019 - shashi
#program that accepts a number and prints out all possible word combos as represented on a phone dialpad.
#So: 2 = "abc", 3 = "def", 4 = "ghi"....etc until 9.
#If 235 is sent, then "abc","def" and "jkl" are combined to generate word combos.


def wordCombosDialpad(number):
    
    #error check:
    if not number: return "Invalid"
    
    #step 1: create lookup for each of the digits.
    dialPadLookUp = {'2': 'abc','3': 'def','4': 'ghi','5': 'jkl','6': 'mno','7': 'pqrs','8': 'tuv','9': 'wxyz',}
   
    #step 2: convert int input to string and set up output array
    strNumber = str(number)
    comboArray = [''] #empty array to hold all combos
 
    #step 3 : loop through each letter of converted string and lookup its combo from lookup array
    for char in strNumber:  #loop through each character in strNumber
        letters = dialPadLookUp.get(char, '')   #look up its mapped combo string in dialPadLookUp
        
        #something new I learnt. Combining loops within the array value assignment to continously loop through each pattern and join with the other.
        #so, "abc" and "def" would go: "ad", "ae", "af", "bd","be","bf" "cd", "ce", "cf"
        comboArray = [value+eachLetter for value in comboArray for eachLetter in letters]
    #loop ends here
    
    #return final array back
    return comboArray
 
print(wordCombosDialpad(23))        #take mapping of 2 and 3 and combine them. 9 combinations
print(wordCombosDialpad(764))       #mapping of 7 (pqrs), 6 (mno) and 4 (ghi) together.  36 combinations
print(wordCombosDialpad(8324))      #mapping of 8 (tuv), 3 (def), 2(abc), 4(ghi) together. 81 combos
print(wordCombosDialpad(0))         #error handling. Invalid returned.
