class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cur_cost = 0
        ans = 0
        for cost in costs:
            cur_cost+=cost
            if coins<cur_cost:
                return ans
            ans +=1
            
        return ans
        
