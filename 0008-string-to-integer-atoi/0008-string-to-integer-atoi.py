class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # Step 1: Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check sign
        sign = 1
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # Step 3: Convert digits manually
        num = 0
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            num = num * 10 + digit
            i += 1

        num = num * sign

        # Step 4: Check 32-bit range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num