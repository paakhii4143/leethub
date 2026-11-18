
class Solution(object):
    def maximumLength(self, nums):
        from collections import Counter

        freq = Counter(nums)
        ans = 1

        for x in freq:
            if x == 1:
                ans = max(ans, freq[x] if freq[x] % 2 == 1 else freq[x] - 1)
                continue

            length = 0
            curr = x

            while freq[curr] >= 2:
                length += 2
                curr = curr * curr

                if curr not in freq:
                    break

            if curr in freq:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans
