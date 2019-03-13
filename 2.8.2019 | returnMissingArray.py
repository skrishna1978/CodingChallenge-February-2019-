#2.8.2019 - shashi
#program that takes an array of arrays. when sorted by length, the size values are consecutive.
#program needs to find the missing array in them. 
#ex: [[1,2], [1,1,2], [2,3,4,5,5]]  should return 4.


def findMissingArraySize(masterArray): #function starts here
    
    #STEP 1: first we check for all error possibilities.
    if masterArray is None or len(masterArray) == 0: #if master array is empty or contains no elements
        return 0  #return 0
    else: #then we loop inside the array and check size of EACH array
        for array in masterArray:
            if array is None or len(array) == 0:  #if any array there is empty
                return 0 #return 0


    #STEP 2: We load the sizes of all valid arrays into another array
    arrayLength = [] #to hold sizes of all valid arrays
    
    for array in masterArray: #loop through each array in master array
        arrayLength.append(len(array)) #add the length of each array inside it
        #loop ends
    arrayLength = sorted(arrayLength) #sort the array by length
    
    #STEP 3: Now we check the array of sizes and see which value is missing (since its sorted)
    loop = 0
    while loop < len(arrayLength)-1: #loop through the array
        if arrayLength[loop+1] - arrayLength[loop] > 1: #check neighboring values. does subtracting them give us more than 1?
            return arrayLength[loop] + 1 #if so, then that is the missing array size in the master array. return it.
        loop += 1 #else loop on and complete.



#running the function with different values
print(findMissingArraySize(
    [[3, 4], [8, 4, 2, 4], [6,7,8,9,10], [5]]))     #[2,4,5,1] are the array sizes. so return value is 3
print(findMissingArraySize([[1],[],[2,2]])) #check error conditions. none of the mini-arrays should be blank/none.
print(findMissingArraySize(
    [['x','x', 'x'], ['x','x','x','x'],['x','x','x','x','x'],['x']])) #[3,4,5,1] are array sizes. so return value is 2.
#end of program
