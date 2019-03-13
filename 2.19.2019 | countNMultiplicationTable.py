#2.19.2019 - shashi
#program that accepts N and X and returns the number of times X appears in an NxN multiplication table.
#for ex: N=4, X= 6.
#1 2 3
#2 4 6
#3 6 9
#4 8 12
#so, 6 appears 2 times in the multiplication table.

def getCountMultiply(sourceNumber, finderValue):
    if sourceNumber == 1:           #checking for 1
        return sourceNumber
        
    count =0        #count of occurrences

    #STEP 1: Generating the NxN table and populating it. Shorter version possible but expanding it here.
    table = [[0 for x in range(sourceNumber)] for y in range(sourceNumber)] 
    for row in range(sourceNumber):
        for col in range(sourceNumber):
            table[row][col]=(row+1)*(col+1)
    
    #STEP 2: Going through NxN table and looking for value needed
    for row in range(sourceNumber):
        for col in range(sourceNumber):
            if(table[row][col] == finderValue): #if value found
                count = count+1                 #increase counter hit
    
    return count  #return final count back to calling function

#testing function
print(getCountMultiply(4,6))    #2 6s
print(getCountMultiply(5,14))    #0 14s
print(getCountMultiply(10,20))    #4 20s
print(getCountMultiply(1,5))    #1 sent. so 1 returns regardless of second parameter.
