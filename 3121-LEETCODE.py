from string import ascii_lowercase, ascii_uppercase

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first = {}
        last = {}

        for i, ch in enumerate(word):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        ans = 0

        for low, up in zip(ascii_lowercase, ascii_uppercase):
            if low in last and up in first:
                if last[low] < first[up]:
                    ans += 1

        return ans
