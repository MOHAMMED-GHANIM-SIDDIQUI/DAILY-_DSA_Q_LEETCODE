class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        total_nums = "123456789"
        res = []

        for i in range(9):
            for j in range(i, 9):
                num = int(total_nums[i:j+1])
                if low <= num <= high:
                    res.append(num)

        return sorted(res)
