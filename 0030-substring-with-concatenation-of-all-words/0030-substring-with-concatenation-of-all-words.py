
class Solution(object):
    def findSubstring(self, s, words):
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1

        ans = []

        for i in range(word_len):
            left = i
            right = i
            seen = {}
            count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in freq:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1

                    while seen[word] > freq[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len

                    if count == word_count:
                        ans.append(left)

                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len

                else:
                    seen = {}
                    count = 0
                    left = right

        return ans
