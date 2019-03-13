#2.16.2019 - shashi
#program accepts a string made up of numbers (spelt out)
#it has to then return the average of these numbers back as a string (spelt out)
#ex: "one two three four" returns "1+2+3+4 = 10/4 = 2 = two.
#only 0-9 are valid inputs.

def averageOfStringInts(stringInts):    #function starts here
    if not stringInts: return "Invalid"         #invalid/empty value check
    #create a lookup array for each of the digits to correspond with a number
    valueLookUp = { 'zero'  : 0,
            'one'   : 1,
            'two'   : 2,
            'three' : 3,
            'four'  : 4,
            'five'  : 5,
            'six'   : 6,
            'seven' : 7,
            'eight' : 8,
            'nine'  : 9 }
    
    #variable to hold int total        
    total = 0
    #split the original string into an array[]        
    stringInts = stringInts.split(' ')
    for number in range(len(stringInts)):            #loop through the array
        if stringInts[number] in valueLookUp:        #if string number found in lookup array
            total += valueLookUp[stringInts[number]] #get the int equivalent and add to result
        else: 
            return "N/A"                             #if not found return error.
            
    averageResult = total // len(stringInts)          #now get the average value as integer.

    for number in valueLookUp:                          #finally look up word equivalent of average number    
        if valueLookUp.get(number) == averageResult:    #if value found in lookup array, then return it.
            averageResult = number
    return averageResult
#end of function

print(averageOfStringInts("one two three"))    #1+2+3+4 = 10/4 = 2 = two
print(averageOfStringInts("six one eight"))         #6+1+8 = 15/3 = 5 = five
print(averageOfStringInts(""))                      #error check - invalid
print(averageOfStringInts("nineteen eight five"))   #missing value check - N/A
