# 2.23.2019 - shashi
# program accepts a +ve number and adds dashes (-) in between each odd number/digit.
# even numbers are left as they are.


def addOddDash(number):                  #function starts here
 
    if number == None or number<=0:
        return 'Invalid'
    finalString = ''
    
    #step 1: convert number to string so -s can be added
    processString = str(number)
    
    #step 2 : add the dashes based on even/odd check
    for eachChar in processString:      #loop through the string now
        if int(eachChar) % 2 == 0:      #and check if the digit is even or odd
            finalString += eachChar     #if even then add it to final as is
        else:                           
            finalString += '-' + eachChar + '-'    #if odd, then prefix and suffix it with a dash
    #end of loop
    
    #step 3 : get rid of any extra/unwanted dashes 
    finalString = finalString.replace('--','-')  #replace any -- with -
    finalString = finalString.strip('-')         #get rid leading/trailing -s
   
    return finalString   #return final output


#testing function
print(addOddDash(1443))  #should return 1-44-1
print(addOddDash(0))     #should return "Invalid"
print(addOddDash(9899))  #should return 9-8-9-9
print(addOddDash(228899))     #should return "2288-9-9"
print(addOddDash(-775))     #should return "Invalid"

