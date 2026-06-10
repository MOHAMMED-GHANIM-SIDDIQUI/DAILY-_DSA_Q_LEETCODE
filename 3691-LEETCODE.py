class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        LOG = n.bit_length()

        mx = [nums[:]]
        mn = [nums[:]]

        j = 1
        while (1 << j) <= n:
            prev_mx = mx[j - 1]
            prev_mn = mn[j - 1]
            half = 1 << (j - 1)

            cur_mx = [
                max(prev_mx[i], prev_mx[i + half])
                for i in range(n - (1 << j) + 1)
            ]
            cur_mn = [
                min(prev_mn[i], prev_mn[i + half])
                for i in range(n - (1 << j) + 1)
            ]

            mx.append(cur_mx)
            mn.append(cur_mn)
            j += 1

        def value(l: int, r: int) -> int:
            length = r - l + 1
            p = length.bit_length() - 1
            mxv = max(mx[p][l], mx[p][r - (1 << p) + 1])
            mnv = min(mn[p][l], mn[p][r - (1 << p) + 1])
            return mxv - mnv

        heap = []

        for l in range(n):
            heapq.heappush(heap, (-value(l, n - 1), l, n - 1))

        ans = 0

        for _ in range(k):
            neg_v, l, r = heapq.heappop(heap)
            ans += -neg_v

            if r > l:
                heapq.heappush(heap, (-value(l, r - 1), l, r - 1))

        return ans
