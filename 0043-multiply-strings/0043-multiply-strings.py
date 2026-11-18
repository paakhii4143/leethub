
class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        n = len(num1)
        m = len(num2)

        result = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                mul = int(num1[i]) * int(num2[j])

                total = mul + result[i + j + 1]

                result[i + j + 1] = total % 10
                result[i + j] += total // 10

        ans = ""

        for digit in result:
            if not (len(ans) == 0 and digit == 0):
                ans += str(digit)

        return ans
