class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        res = []
        i = 0  # start index of current special substring

        for j, char in enumerate(s):
            if char == '1':
                count += 1
            else:
                count -= 1

            # When count == 0, we found a special substring
            if count == 0:
                # Recursively optimize the middle part
                middle_optimized = self.makeLargestSpecial(s[i + 1:j])
                # Add the optimized special substring
                res.append('1' + middle_optimized + '0')
                i = j + 1

        # Sort substrings in descending order to get lexicographically largest
        res.sort(reverse=True)

        return "".join(res)
