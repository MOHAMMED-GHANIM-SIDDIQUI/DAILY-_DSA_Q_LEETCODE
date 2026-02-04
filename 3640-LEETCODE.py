class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        ans = float("-inf")
        i = 0

        while i < n - 2:
            j = i + 1

            # inc
            while j < n and nums[j] > nums[j - 1]:
                j += 1
            p = j - 1
            if p == i:
                i += 1
                continue

            # dec
            while j < n and nums[j] < nums[j - 1]:
                j += 1
            q = j - 1
            if q == p:
                i += 1
                continue

            # inc
            while j < n and nums[j] > nums[j - 1]:
                j += 1
            r = j - 1
            if r == q:
                i += 1
                continue

            # core sum O(1)
            core_sum = pref[q + 1] - pref[p]

            # left max (only once per i → amortized O(n))
            max_left = 0
            cur = 0
            k = p - 1
            while k >= i:
                cur += nums[k]
                max_left = max(max_left, cur)
                k -= 1

            # right max (only once per i → amortized O(n))
            max_right = 0
            cur = 0
            k = q + 1
            while k <= r:
                cur += nums[k]
                max_right = max(max_right, cur)
                k += 1

            ans = max(ans, core_sum + max_left + max_right)

            # CRUCIAL: skip entire valley
            i = q

        return ans if ans != float("-inf") else -1
