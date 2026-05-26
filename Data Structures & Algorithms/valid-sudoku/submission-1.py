class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        #check rows
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

            #check cols
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        #check boxes
        for square in range(9):
            s = set()
            for i in range(3):
                for j in range(3):
                    #loop through each row divided into 3
                    row = (square//3) * 3 + i
                    #loop through col continuously
                    col = (square % 3) * 3 + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in s:
                        return False

                    s.add(board[row][col])

        return True                        