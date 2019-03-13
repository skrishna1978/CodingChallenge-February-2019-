#2.13.2019 - shashi
#program that takes a number and reverses its digits
#ex: 1234 becomes 4321

def reverseNumber(number):  #function starts here

    if not number:          #erraneous invalid values
        return "Invalid"
    reverse = int(str(abs(number))[::-1])
    #abs(number) > get absolute value of the original number without signs
    #str(abs(number)) >  get String/printable version of the absolute number
    #int(str(abs(number)) [::-1])  >  reverse all items in the string/printable version and convert it back to int()
    
    #return signed version of number if less than 0. If not then return reverse.
    return -reverse if number < 0 else reverse
    

#testing reverseNumber() with values
print(reverseNumber(4321))
print(reverseNumber(-117))
print(reverseNumber(87))
print(reverseNumber(0))
#end of program
