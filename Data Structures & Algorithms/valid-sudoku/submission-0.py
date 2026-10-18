class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n,m = len(board),len(board[0])
        # Check row
        for row in board:
            nums = [x for x in row if x!= '.'] 
            if len(nums) != len(set(nums)):
                return False

        #Check column
        for j in range(9):
            column = [board[i][j] for i in range(9) if board[i][j] != '.']
            if len(column) != len(set(column)):
                return False
        # Create box and check 
        for i in range(0,9,3):
            for j in range(0,9,3):
                box = []
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        if board[r][c] != ".":
                            box.append(board[r][c])


                if len(box) != len(set(box)):
                    return False
        return True           
               
                

        

        