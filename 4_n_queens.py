def solveNQueens(n):
    result = []
    cols, diag1, diag2 = set(), set(), set()

    def backtrack(row, board):
        if row == n:
            result.append(["".join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col); diag1.add(row - col); diag2.add(row + col)
            board[row][col] = 'Q'
            backtrack(row + 1, board)
            board[row][col] = '.'
            cols.remove(col); diag1.remove(row - col); diag2.remove(row + col)

    board = [['.' ] * n for _ in range(n)]
    backtrack(0, board)
    return result

# Test Cases
print("Test 1:", solveNQueens(4))
# Expected: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
print("Test 2:", solveNQueens(1))
# Expected: [["Q"]]
