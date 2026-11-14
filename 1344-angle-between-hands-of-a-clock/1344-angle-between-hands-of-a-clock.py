
class Solution(object):
    def angleClock(self, hour, minutes):
        minuteAngle = minutes * 6

        hourAngle = (hour % 12) * 30 + minutes * 0.5

        angle = abs(hourAngle - minuteAngle)

        return min(angle, 360 - angle)
