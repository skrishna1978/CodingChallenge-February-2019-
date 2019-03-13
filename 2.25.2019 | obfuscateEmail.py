#2.25.2919 - shashi
#program that accepts an email address and replaces @ and . with [at] and [dot]


import re  #for regex operation

def obfuscate(emailAddress):    #function starts here.
    
    #step 1: check if the email address is valid (Source: https://www.pythoncentral.io/how-to-validate-an-email-address-using-python/)
    if(re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', emailAddress)!=None):
        
        formattedEmail = ""
        
        #step 2 - process the valid email address
        for character in emailAddress:      #loop through the email address
          if character == "@":              #check for @ and . to replace them with words
            formattedEmail += " [at] "
          elif character == ".":
            formattedEmail += " [dot] "
          else:
            formattedEmail += character     #every other character append as is
        #end of loop
        
        return formattedEmail       #return formatted email back
    
#testing function    
print(obfuscate("john.smith@email.com"))        #valid
print(obfuscate("john.smith.com"))              #invalid (no @)
print(obfuscate(" "))                           #invalid
print(obfuscate("somename@someemail,co.uk"))    #invalid (has a comma)

