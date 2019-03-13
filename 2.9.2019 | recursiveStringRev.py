#2.9.2019 - shashi
#program that accepts a string and returns its reversed version via recursion.

def revStringRecursive(stringVar): #function starts here
	
	if not stringVar:                       #if empty string sent
	    return "Invalid"                    #return error message
	if len(stringVar) == 1:                 #if only a single letter was sent
		return stringVar                    #return the same back
	else:
		output =  stringVar[-1]             #load the last character into output      
		output += revStringRecursive(stringVar[0:len(stringVar)-1]) #append it with a shorter version of string
		return output                #if string was "hello world", this function call will take:
		                             # 'd' + functionCall("hello worl")
		                             # 'dl' + functionaCall("hello wor")
		                             # 'dlr' + functionCall("hello wo") ...and so on until complete string is done.
		                            
#testing the function
print(revStringRecursive("sample text"))        #valid value test
print(revStringRecursive("12345678"))           #numeric value test
print(revStringRecursive("Hello 1 World 2"))    #mixed type test
print(revStringRecursive("a"))                  #single value test
print(revStringRecursive(""))                   #empty value test
