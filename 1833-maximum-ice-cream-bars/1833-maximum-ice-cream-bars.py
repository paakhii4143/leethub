
class Solution(object):
    def maxIceCream(self, costs, coins):
        count = [0] * 100001

        for cost in costs:
            count[cost] += 1

        ans = 0

        for cost in range(1, 100001):
            while count[cost] > 0 and coins >= cost:
                coins -= cost
                ans += 1
                count[cost] -= 1

            if coins < cost:
                break

        return ans
