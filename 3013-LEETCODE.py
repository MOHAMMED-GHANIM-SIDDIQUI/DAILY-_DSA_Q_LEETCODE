class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        if k == 1:
            return nums[0]

        need = k - 1
        window = SortedList(nums[1: dist + 2])

        current_sum = sum(window[:need])
        min_cost = current_sum

        for i in range(1, len(nums) - dist - 1):
            outgoing = nums[i]
            incoming = nums[i + dist + 1]

            # Remove outgoing
            idx_out = window.bisect_left(outgoing)
            window.remove(outgoing)

            if idx_out < need:
                current_sum -= outgoing
                if len(window) >= need:
                    current_sum += window[need - 1]

            # Add incoming
            window.add(incoming)
            idx_in = window.bisect_left(incoming)

            if idx_in < need:
                current_sum += incoming
                if len(window) > need:
                    current_sum -= window[need]

            min_cost = min(min_cost, current_sum)

        return min_cost + nums[0]
