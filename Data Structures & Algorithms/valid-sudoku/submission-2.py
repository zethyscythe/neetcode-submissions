class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_set=[set() for _ in range(9)]
        for i in range(9):
            if i%3==0:
                box_set=[set() for _ in range(3)]
            col_set=set()  
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row_set[j] or board[i][j] in col_set or board[i][j] in box_set[j//3]:
                    return False

                box_set[j//3].add(board[i][j])
                col_set.add(board[i][j])
                row_set[j].add(board[i][j]) 

        return True    
                


        