class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)

        i = n - 2

        # Step 1: Find pivot
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: Find next greater element
        if i >= 0:
            j = n - 1

            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the remaining elements
        left = i + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
