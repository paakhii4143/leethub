class Solution(object):
    def maxIceCream(self, costs, coins):
        count = [0] * 100001

        for cost in costs:
            count[cost] += 1

        ans = 0

        for cost in range(1, 100001):
            if count[cost] == 0:
                continue

            buy = min(count[cost], coins // cost)

            ans += buy
            coins -= buy * cost

            if coins == 0:
                break

        return ans