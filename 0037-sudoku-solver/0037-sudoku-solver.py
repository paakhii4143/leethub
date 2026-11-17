
class Solution(object):
    def solveSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Store existing numbers
        empty = []

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    empty.append((r, c))
                else:
                    box = (r // 3) * 3 + (c // 3)

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

        # Backtracking function
        def solve(index):

            if index == len(empty):
                return True

            r, c = empty[index]
            box = (r // 3) * 3 + (c // 3)

            for num in "123456789":

                if (num not in rows[r] and
                    num not in cols[c] and
                    num not in boxes[box]):

                    # Place number
                    board[r][c] = num

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

                    # Recursive call
                    if solve(index + 1):
                        return True

                    # Backtrack
                    board[r][c] = "."

                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box].remove(num)

            return False

        solve(0)
