
class Solution(object):
    def insert(self, intervals, newInterval):
        result = []

        for interval in intervals:
            # Case 1: Current interval is before newInterval
            if interval[1] < newInterval[0]:
                result.append(interval)

            # Case 2: Current interval overlaps with newInterval
            elif interval[0] <= newInterval[1]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

            # Case 3: Current interval is after newInterval
            else:
                result.append(newInterval)
                newInterval = interval

        result.append(newInterval)

        return result
