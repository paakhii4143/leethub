class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, path, remaining):
            # Target complete ho gaya
            if remaining == 0:
                result.append(path[:])
                return

            # Target exceed ho gaya
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])

                # Same element dobara use kar sakte hain
                backtrack(i, path, remaining - candidates[i])

                # Backtracking: last element remove karo
                path.pop()

        backtrack(0, [], target)
        return result