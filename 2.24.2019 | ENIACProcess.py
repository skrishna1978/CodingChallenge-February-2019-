#2.24.2019 - shashi
#Comprised of a team of five incredibly brilliant women, "The ladies of ENIAC" were the first “computors” working at the 
#University of Pennsylvania’s Moore School of Engineering (1945). Through their contributions, we gained the first software 
#application and the first programming classes! The ladies of ENIAC were inducted into the WITI Hall of Fame in 1997!
#Write a function which reveals "The ladies of ENIAC" names, so that you too can add them to your own hall of tech fame!
#To keep: only alpha characters, space characters and exclamation marks.
#To remove: numbers and these characters: %$&/£?@

import re #for regular expression operations

def eniacExtract(pattern):  #function starts here
    stringVar = re.findall(r'[a-zA-Z! ]', pattern)   #load up all entries that match a-z, A-Z, spaces and !s
    #stringVar gets individual elements as items in an array/list. Next we loop through this to make one readable pattern
    
    output =''  #to hold final extracted/formatted output
    
    for loop in range(len(stringVar)):  #loop within the extracted string from findAll()
        output = output + stringVar[loop]  #add every found element one by one one into output

    output = output.upper()  #convert output to UPPER case
    return output           #return output back

#testing method
print(eniacExtract("k?%35a&&/y@@@£5599 m93753&$$$c$n///79u??@@%l?975$t?%5y%&$3$1!"))   #retains only alphas, spaces and !s
print(eniacExtract("9?9?9?m335%$£@a791%&$r$$$l£@53$&y&n%$5@ $£5577w&7e931%s$£c$o%%%f351f??%!%%"))   #retains alphas, spaces and !s



Language Version:  3.6.5
