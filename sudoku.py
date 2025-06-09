def find_next_empty(puzzle):#finds the next row or colum with a sapce not filled yet
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]== -1:
                return r,c 
    return  None, None # no spaces in the puzzle are empty

def is_valid(puzzle, guess, row, col):#figures out if guess at row or col is valid
    #returns true or false
    row_vals=puzzle[row]
    if guess in row_vals:
        return False
    #columns
    col_vals=[puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    #position in the grid
    row_start = (row//3) *3
    col_start = (col//3) *3

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False
    #if checks pass then should return True
    return True

    
def solve(puzzle):
    row, col = find_next_empty(puzzle) #choose seomwhere to mamek
    if row is None:
        return True
    for guess in range(1,10):
        if is_valid(puzzle, guess, row , col):
            puzzle[row][col] = guess
            #recursively call our function
            if solve(puzzle):
                return True
            #if guess not valid
            #backtrack and try new number
            puzzle[row][col] =-1

            #if no numbers work
    return False

#if __name__ == '__main__':
example_board = [
    [3,9,-1,  -1,5,-1,  -1,-1,-1],
    [-1,-1,-1,  2,-1,-1,  -1,-1,5],
    [-1,-1,-1,  7,1,9,  -1,8,-1],

    [-1,5,-1,  -1,6,8,  -1,-1,-1],
    [2,-1,6,  -1,-1,3,  -1,-1,-1],
    [-1,-1,-1,  -1,-1,-1,  -1,-1,4],

    [5,-1,-1,  -1,-1,-1,  -1,-1,-1],
    [6,7,-1,   1,-1,5,  -1,4,-1],
    [1,-1,9,  -1,-1,-1,  2,-1,-1]
     ]
print(solve(example_board))
print(example_board)