class Solution:

    def is_valid(self, tasks, energy):

        # DO NOT mutate original list
        arr = sorted(tasks, key=lambda x: (x[1] - x[0]), reverse=True)

        for actual, minimum in arr:
            if energy < minimum:
                return False

            energy -= actual

        return True

    def minimumEffort(self, tasks: List[List[int]]) -> int:

        low, high = 0, 10**9
        ans = high

        while low <= high:

            mid = low + (high - low) // 2

            if self.is_valid(tasks, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans



