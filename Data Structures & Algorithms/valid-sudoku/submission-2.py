class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hs = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != "." and board[i][j] in hs:
                    return False
                hs.add(board[i][j])
            hs.clear()
        for j in range(9):
            for i in range(9):
                if board[i][j] != "." and board[i][j] in hs:
                    return False
                hs.add(board[i][j])
            hs.clear()
        for i in range(9):
            for j in range(9):
                r = (i%3) *3 + j // 3 
                c = (i // 3) * 3 + j % 3
                print(r,c)
                if board[r][c] != "." and board[r][c] in hs:
                    return False
                hs.add(board[r][c])
            hs.clear()
        return True
        