#2.22.2019 - shashi
#wheel of fortune simulator.
#input sent is contestname and scores. winner is one who is closest to 100 (while still being lower or equal to 100). 

def WOF_Winner(playerData): #get array data
    
    winnerName= ""          #to hold name of winner
    winnerScore = 0         
    playerTotal = 0
    
    #loop through each player data in the object array
    for eachPlayer in playerData:                   
        playerName = eachPlayer['name']             #load player name
        playerScore = eachPlayer['scores']          #load player score

            
        totalScore = 0                  
        spinCount = 0
        
        playerTotal += 1                #number of players
        
        for eachScore in playerScore:       #nested loop to track each score entry for each player
            if eachScore > 100 or eachScore % 5:        #if invalid value in scores
                return False                            #no point going on. so return false.
                
            totalScore += eachScore                     #else increment totalScore for this player.
            spinCount += 1                              #increment spins he/she got.
            
        if spinCount not in (1, 2):                     #invalid spin counts (only one or two allowed)        
            return False                                #return false

        elif totalScore > winnerScore:                  #get highest winner's score and name
            winnerScore = totalScore
            winnerName = playerName
    #end of for loop here

    #check if score is within 100 and there were 3 players
    if winnerScore<=100 and playerTotal ==3:
        return winnerName                   #get the winner's name
    else:
        return False

#testing function trial 1
player1 = {"name": "Alice", "scores": [10, 45,5]}
player2 = {"name": "Bob", "scores": [70,5]}
player3 = {"name": "Cathy", "scores": [35, 55]}
print(WOF_Winner([player1, player2, player3])) #Returns False because Alice got 3 spins. Not allowed.

#testing function trial 2
player1 = {"name": "John", "scores": [20, 40]}
player2 = {"name": "Jane", "scores": [80,15]}
player3 = {"name": "Erik", "scores": [30]}      #this is OK since 1 or 2 spins allowed.
print(WOF_Winner([player1, player2, player3])) #Returns Jane since she is closer to 100.
