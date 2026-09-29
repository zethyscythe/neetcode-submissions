class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map_k = defaultdict(int)
        map_v = defaultdict(list)
        for num in nums:
            map_k[num]+=1
            map_v[map_k[num]].append(num)

        for val in reversed((map_v.values())):
            if len(val)>=k:
                return val[:k]
            
                 



        