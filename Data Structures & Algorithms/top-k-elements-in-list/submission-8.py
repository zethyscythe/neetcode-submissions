class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map_k = defaultdict(int)
        map_v = defaultdict(list)
        for num in nums:
            map_k[num]+=1
            map_v[map_k[num]].append(num)
            # if len(map_v[map_k[num]])==k and len(map_v[map_k[num]]) <= len(map_v[last_idx]):
            #     return map_v[last_idx] 
            # last_idx=map_k[num]                
           #print("key:",map_k[num],"val:",map_v[map_k[num]])

        for val in reversed((map_v.values())):
            print(val)
            if len(val)>=k:
                return val[:k]
        #print(list(map_v.values())) 
        return map_v[k]    
                 



        