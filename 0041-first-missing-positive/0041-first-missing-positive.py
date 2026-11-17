
class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Step 1: Place each number at its correct index
        i = 0
        while i < n:
            correct = nums[i] - 1

            if 1 <= nums[i] <= n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        # Step 2: Find the first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # Step 3: All numbers from 1 to n are present
        return n + 1
