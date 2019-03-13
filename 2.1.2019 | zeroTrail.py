#2.1.2019 - Shashi
#program to print trailing 0s of a factorial operation.

def zeroTrail(number):  #ex: 5 is sent
     #Trailing 0 will come into number when any number is multiplied by 10.
    zeroCounter = 0  #to track the number of 0s at the end of the final output
   
    while number > 0:  #as long as number > 0
        zeroCounter = zeroCounter + number//5  #dividing the number by 5 successfully extracts a 0. 
        number = number//5 #reduce original number by dividing it by 5.
    #end of the loop once number is lesser than 0.
    
    return zeroCounter #out of the loop, return value back to calling function


# values <5 do not have factorials ending in 0.
print(zeroTrail(5)) #120 - which as 1 0 at the end.
print(zeroTrail(10)) #3628800 - which has 2 0s at the end.  
print(zeroTrail(12)) #479001600 - which has 2 0s at the end.
