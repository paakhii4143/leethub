
class Solution(object):
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            line_length = 0

            # Step 1: Find maximum words that fit
            while j < n and line_length + len(words[j]) + (j - i) <= maxWidth:
                line_length += len(words[j])
                j += 1

            # Step 2: Calculate spaces
            gaps = j - i - 1

            # Step 3: Last line or single word
            if j == n or gaps == 0:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))

            else:
                total_spaces = maxWidth - line_length
                space_each = total_spaces // gaps
                extra = total_spaces % gaps

                line = ""

                for k in range(i, j - 1):
                    spaces = space_each

                    if k - i < extra:
                        spaces += 1

                    line += words[k] + " " * spaces

                line += words[j - 1]

            res.append(line)
            i = j

        return res
