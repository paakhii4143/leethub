class Solution(object):
    def processStr(self, s, k):
        n = len(s)
        length = 0
        lens = []

        for ch in s:
            if ch == '*':
                length = max(0, length - 1)
            elif ch == '#':
                length *= 2
            elif ch == '%':
                pass
            else:
                length += 1

            lens.append(length)

        if k >= length:
            return "."

        for i in range(n - 1, -1, -1):
            ch = s[i]
            prev = lens[i - 1] if i > 0 else 0

            if ch == '*':
                length = prev
            elif ch == '#':
                length = prev
                if k >= length:
                    k -= length
            elif ch == '%':
                length = prev
                k = length - 1 - k
            else:
                if k == prev:
                    return ch
                length = prev

        return "."