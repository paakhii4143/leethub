
class Solution(object):
    def isNumber(self, s):
        digit = False
        dot = False
        exp = False
        digit_after_e = True

        for i, ch in enumerate(s):

            if ch.isdigit():
                digit = True
                if exp:
                    digit_after_e = True

            elif ch == '+' or ch == '-':
                if i > 0 and s[i - 1] not in 'eE':
                    return False

            elif ch == '.':
                if dot or exp:
                    return False
                dot = True

            elif ch == 'e' or ch == 'E':
                if exp or not digit:
                    return False
                exp = True
                digit_after_e = False

            else:
                return False

        return digit and digit_after_e
