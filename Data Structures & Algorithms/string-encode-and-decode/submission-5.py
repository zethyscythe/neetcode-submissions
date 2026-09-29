class Solution:

    def encode(self, strs: List[str]) -> str:
        tot_all_len=0
        for i in range(len(strs)):
            tot_all_len+=len(strs[i])
            strs.append(f"#{len(strs[i])}")
        strs.append(f"|{tot_all_len}")
        return ''.join(strs)    

    def decode(self, s: str) -> List[str]:
        result=[]
        #print(s)
        idx_of_tot_all_len=s.rfind('|')
        tot_all_len= int(s[idx_of_tot_all_len + 1:]) 
        if tot_all_len ==0 and s[0]=="|":
            return result
        
        list_of_length=s[tot_all_len+1:idx_of_tot_all_len].split("#")
        #print(list_of_length)
        next_counter=0
        for len in list_of_length:
            #print(s[next_counter:int(len)+next_counter])
            result.append(s[next_counter:int(len)+next_counter])
            next_counter+=int(len)

        return result
