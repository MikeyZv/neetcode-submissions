class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list) 
        squares = defaultdict(list) 
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                square_key = math.floor(row / 3) * 3 + math.floor(col / 3)
                if board[row][col] == ".":
                    continue
                elif board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[square_key]:
                    return False
                else:
                    rows[row].append(board[row][col])
                    cols[col].append(board[row][col])
                    squares[square_key].append(board[row][col])

        return True