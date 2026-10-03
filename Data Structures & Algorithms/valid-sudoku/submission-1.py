class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row=[set() for _ in range(9)]

        for i in range(9):
            if i%3==0:
                sub_box=[set() for _ in range(3)]
            col=set()  
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row[j] or board[i][j] in col or board[i][j] in sub_box[j//3]:
                    #print(f"i={i} j={j}")
                    return False

                #print(f"i={i} j={j} val={board[i][j]}")
                sub_box[j//3].add(board[i][j])
                col.add(board[i][j])
                row[j].add(board[i][j]) 

        #print(sub_box)
        return True    
                


        