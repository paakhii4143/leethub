
class Solution(object):
    def merge(self, intervals):
        intervals.sort()

        result = []

        for start, end in intervals:
            if not result or start > result[-1][1]:
                result.append([start, end])
            else:
                result[-1][1] = max(result[-1][1], end)

        return result
