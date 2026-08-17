class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp=sorted(set(arr))
        hash_map=defaultdict(int)
        for idx,val in  enumerate(temp):
            hash_map[val]=idx+1
        ans=[]
        for val in  arr:
            ans.append(hash_map[val])
        return  ans       
