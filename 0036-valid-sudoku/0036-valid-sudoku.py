class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
class Solution(object):
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                num = board[r][c]

                if num == ".":
                    continue

                box_index = (r // 3) * 3 + (c // 3)

                if num in rows[r]:
                    return False

                if num in cols[c]:
                    return False

                if num in boxes[box_index]:
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)

        return True
