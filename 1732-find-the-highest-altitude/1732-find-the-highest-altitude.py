
class Solution(object):
    def largestAltitude(self, gain):
        curr = 0
        highest = 0

        for num in gain:
            curr += num
            highest = max(highest, curr)

        return highest

