#2.3.2019 - shashi
#program that accepts 2 arrays and checks if they are balanced. as in, contain the same kind of elements.
#ex: a,a,a,a,b,b,c  and d,d,d,d,e,e,f
# both have similar kind of unique elements appearing same # of times. so these arrays are balanced.

def arrayBalanceCheck(array1, array2): #function starts here

    
    #STEP 1: Loading all unique elements from both arrays
    set1 = set(array1)  #creating a set loads all the UNIQUE elements only
    set2 = set(array2)  #so create such a set of unique elements for both arrays
    
    #STEP 2: Create container arrays to hold the final versions of original arrays
    array1_balance = []  #These arrays are empty to begin with but get re-loaded with items
    array2_balance = []
    
    for item in set1:  #go through each item in set 1
        array1_balance.append(array1.count(item)) #add counts of each element of original array into new balance array
        #the purpose of this step is to then compare it with the 2nd array to see if the counts match.

    for item in set2: #repeat the loop for all items in set 2
        array2_balance.append(array2.count(item)) #add counts of items in original 2nd array into new balance array


    if sorted(array1_balance) == sorted(array2_balance):    #if the sorted versions of both arrays match
        return "Arrays are balanced."                       #the balance is TRUE
    else:                                                   #else 
        return "Arrays are not balanaced."                  #the balance is FALSE

#end of function


array1 = ["a","b","a","a","b","c"]
array2 = ["f","f","f","g","g","h"]
print(arrayBalanceCheck(array1, array2))        #elements in both arrays are of same counts.
array1 = ["a","a","a","a","b","c"]
array2 = ["f","f","g","g","g","h"]
print(arrayBalanceCheck(array1, array2))        #elements in both arrays are not of same counts.
