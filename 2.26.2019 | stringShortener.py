#2.26.2019 - shashi
#program that take a sentence to shortens it to a given length. 

def stringShorten(sentence, maxLength, connector):  #function starts here

    if not sentence or maxLength<=0:                    #error check
        return "Invalid"
    if maxLength >= len(sentence):                      #if sentence length matches required length
        return sentence                                 #return original sentence. no change.
    
    #if length required matches connector length + 1 
    #or if connector length > maxLength
    # return sentence from start to maxLength. As in, the first maxLength characters in sentence.
    if maxLength == len(connector) + 1 or len(connector) > maxLength:
        return sentence[:maxLength] 
    
    #if none of the above are true, then we shrink the sentence. 
    #logic here is:
    #maxLength - length of connector = gives us how much is left to use for the sentence.
    #that value needs to be divided so that first half and last half can share it.
    
    shortenLength = maxLength - len(connector)          #first we figure out how much sentence to use.
    shortenedSentence = sentence[:int(shortenLength/2)]  #first half of the sentence based on length
    shortenedSentence += connector                      #add the connector pattern next
    #second half starts at the end of the sentence and adds it with remainder of dividing length by 2.
    
    #maxLength - (firtHalf + connector length) = second half length.  
    shortenedSentence += sentence[-(int(shortenLength/2) + (shortenLength % 2)):]  #second half of the sentence based on remaining length
     
    return shortenedSentence  #return final version of the shortened sentence.
    

#testing the function
sentence = "The quick brown fox jumps over the lazy dog"
print(stringShorten(sentence, 24,"..."))            #where max length is < total sentence length. Shortened version returned.
print(stringShorten(sentence,812,"..."))            #where max length is > total sentence length. Sentence returned as is.
print(stringShorten(sentence,0,"..."))              #where max length is 0. Invalid returned.
