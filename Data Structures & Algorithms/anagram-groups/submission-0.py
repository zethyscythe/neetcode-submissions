class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = {}
        for s in strs:
            sorted_str="".join(sorted(s))
            if (sorted_str not in map):
                map[sorted_str]=[s]
            else:
                map[sorted_str].append(s)
        return list(map.values())        

                    


        