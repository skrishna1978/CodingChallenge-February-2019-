#2.20.2019 - shashi
#program accepts a number and returns whether or not it is a perfect number.
#perfect number is one whose proper divisors, when added up, equal to the number (excluding itself).
#ex: 6. 1, 2 and 3 divide it perfectly. So 1+2+3 = 6.
#ex: 28. 1,2,4,7 and 14 divide it perfectly. So, 1+2+4+7+14 = 28.
#Complete list of perfect numbers >> https://en.m.wikipedia.org/wiki/List_of_perfect_numbers


def perfectCheck(number):   #function starts here
	 
	if(number <1): return "Invalid"
	#STEP 1: Variable to hold sum of proper divisors of original number
	numberSum = 1
 	 
	#STEP 2: Look for proper divisors and add them together (except the number itself)
    
	looperValue = 2                               	#imagine number = 6
	while looperValue * looperValue < number:      	#loop until looperValue^2 < number	 
    	if number % looperValue == 0:                 	#if looperValue divides number properly         	numberSum = numberSum + looperValue          	#add that value to numberSum  
     #add quotient of division. We have to make numberSum equal to original number.
     	numberSum = numberSum + (number/looperValue) 	    	looperValue += 1                                 	#loop progress
   	 
	#STEP 3: if the sum of proper divisors of number matches number, then number is PERFECT.
	if(numberSum ==number and number!=1):   	#if divisor sum equals to number and number is not 1
    	return True                         	#it is a perfect number
	else:                                   	#else it is not.
    	return False

#end of function

print(perfectCheck(6))      	#true
print(perfectCheck(24))     	#false
print(perfectCheck(28))     	#true
print(perfectCheck(-1))     	#error check
