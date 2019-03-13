#2.14.2019 - shashi
#program that accepts a list and returns the middle part of it, reversed.


def reverseMiddlePart(myList):                      #function starts here

    if not myList:                                  #if empty list sent, return error
        return "Invalid Entry"
    
    #else continue here    
    midPoint = len(myList)//2                      #get the middle point position for the list

    if len(myList) % 2 == 0:                       #if the list contains even number of elements
     return myList[midPoint-1: midPoint + 1][::-1] # return list[from mid-1 until mid + 1, reversed      else:                                    #if the list contains odd number of elements
     return myList[midPoint-1: midPoint + 2][::-1]   return list[mid-1 until mid + 2, reversed (::-1)]
    

print(reverseMiddlePart([10,11,12,13,14,15,16]))                                        #odd numbers
print(reverseMiddlePart(["quick","brown","fox","jumps","over","the","lazy","dog"]))     #even strings
print(reverseMiddlePart(['a','e','i','o','u']))                                         #odd characters
print(reverseMiddlePart([]))                                                            #empty list
print(reverseMiddlePart([10,'a',"mixed",20,'b',"types"]))                         #mixed data types even
print(reverseMiddlePart([10,'a',"mixed",20,'b']))                                 #mixed data types odd
