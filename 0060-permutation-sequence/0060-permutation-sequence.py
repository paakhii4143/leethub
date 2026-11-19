
class Solution(object):
    def getPermutation(self, n, k):
        nums = [str(i) for i in range(1, n + 1)]

        fact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        k -= 1
        result = ""

        for i in range(n - 1, -1, -1):
            index = k // fact[i]

            result += nums[index]
            nums.pop(index)

            k %= fact[i]

        return result
