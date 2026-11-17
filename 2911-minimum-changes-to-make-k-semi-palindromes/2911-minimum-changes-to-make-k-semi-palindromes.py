
class Solution(object):
    def minimumChanges(self, s, k):
        n = len(s)

        # Step 1: Precompute cost
        cost = [[float('inf')] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Check all proper divisors
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    # Check palindrome groups
                    for r in range(d):
                        left = i + r
                        right = j - ((length - 1 - r) % d)

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    cost[i][j] = min(cost[i][j], changes)

        # Step 2: DP
        dp = [[float('inf')] * (k + 1)
              for _ in range(n + 1)]

        dp[0][0] = 0

        for parts in range(1, k + 1):
            for i in range(2 * parts, n + 1):

                for t in range(2 * (parts - 1), i - 1):
                    if dp[t][parts - 1] != float('inf'):
                        dp[i][parts] = min(
                            dp[i][parts],
                            dp[t][parts - 1] + cost[t][i - 1]
                        )

        return dp[n][k]
  