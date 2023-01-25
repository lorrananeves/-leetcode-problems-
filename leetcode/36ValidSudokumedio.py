"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        total = len(board[0])

        for i in range(total):
            check_x_axis = list(range(1,10))
            check_y_axis = list(range(1,10))
            for j in range(total):
                try:
                    if board[i][j] !="." :
                        check_x_axis.remove(int(board[i][j]))
                    if board[j][i] !=".":
                        check_y_axis.remove(int(board[j][i]))
                except ValueError:
                            return False

        l = 0
        while l < total-1:
            for k in range(0,total,3):
                check_3X3 = list(range(1,10))     
                for i in range(k,k+3):
                    for j in range(l,l+3):
                        try:
                            if board[i][j] !="." :
                                check_3X3.remove(int(board[i][j]))
                        except ValueError:
                            return False
            l=l+3

        return True
            
