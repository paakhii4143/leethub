
class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        offset = n + 1

        bit = [0] * (2 * n + 3)

        def update(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def query(i):
            total = 0
            while i > 0:
                total += bit[i]
                i -= i & -i
            return total

        prefix = 0
        ans = 0

        # Insert initial prefix sum 0
        update(offset)

        for num in nums:
            if num == target:
                prefix += 1
            else:
                prefix -= 1

            idx = prefix + offset

            # Count previous prefix sums smaller than current
            ans += query(idx - 1)

            # Insert current prefix sum
            update(idx)

        return ans
