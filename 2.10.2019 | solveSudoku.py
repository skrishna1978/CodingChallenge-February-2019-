#2.10.2019 - shashi
#program that accepts values from a Sudoku board and returns a Boolean
#True means the array satisfies Sudoku. False means it does not.

solvedPattern = [1, 2, 3, 4, 5, 6, 7, 8, 9]  #array to hold the right values for a solve.

def sudokuSolver(sudokuBoard):

	#Check columns for the wrong values
	for column in sudokuBoard:              	#for every column in array
    	if sorted(column) != solvedPattern: 	#if sorted version of it doesn't match required pattern
        	return False                    	#return false
    
	#Check rows for the wrong values
	for row in sudokuBoard:                 	#for every row in array
    	if sorted(row) != solvedPattern:    	#if sorted row doesn't match required pattern
        	return False                    	#return false
    
	# check 3x3 grids for presence of 1..9 values
	for outerLoop in range(3):              	#loop 3 times outside
    	for innerLoop in range(3):          	#loop 3 times inside
        	grid = []                       	#array to load up the values in each 3x3 grid into it    
        	for line in sudokuBoard[outerLoop*3:(outerLoop+1)*3]:   	
                                        #each iteration loads a different 3x3 grid of the master array
            	grid += line[innerLoop*3:(innerLoop+1)*3]          	 
       	 
        	if sorted(grid) != solvedPattern:                       	#if such a grid doesn't match required pattern
            	return False                                        	#return false
           	 
            	#for Sudoku board to be solved, each 3x3 grid should contain all numbers from 1..9

    
	#if none of the above falses are returned and code reaches here, then rows/columns and grids are correct.
	return True #hence, return true.
    

#testing out the function by sending a giant array representing the Sudoku board.
print(sudokuSolver([ 	[5, 3, 4, 6, 7, 8, 9, 1, 2],
                     	[6, 7, 2, 1, 9, 5, 3, 4, 8],
                     	[1, 9, 8, 3, 4, 2, 5, 6, 7],
                     	[8, 5, 9, 7, 6, 1, 4, 2, 3],
                     	[4, 2, 6, 8, 5, 3, 7, 9, 1],
                     	[7, 1, 3, 9, 2, 4, 8, 5, 6],
                     	[9, 6, 1, 5, 3, 7, 2, 8, 4],
                     	[2, 8, 7, 4, 1, 9, 6, 3, 5],
                     	[3, 4, 5, 2, 8, 6, 1, 7, 9]]))
                    	 
                    	 
print(sudokuSolver([ 	[5, 3, 4, 6, 7, 8, 9, 1, 2],
                     	[6, 7, 2, 1, 9, 0, 3, 4, 9],
                     	[1, 0, 0, 3, 4, 2, 5, 6, 0],
                     	[8, 5, 9, 7, 6, 1, 0, 2, 0],
                     	[4, 2, 6, 8, 5, 3, 7, 9, 1],
                     	[7, 1, 3, 9, 2, 4, 8, 5, 6],
                     	[9, 0, 1, 5, 3, 7, 2, 1, 4],
                     	[2, 8, 7, 4, 1, 9, 6, 3, 5],
                     	[3, 0, 0, 4, 8, 1, 1, 7, 9]]))
