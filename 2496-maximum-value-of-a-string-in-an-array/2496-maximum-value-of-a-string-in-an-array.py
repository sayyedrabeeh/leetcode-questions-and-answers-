class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        
        max_n = 0 
        for i in strs:
            if i.isdigit():
                max_n = max(max_n,int(i))
            else:
                max_n = max(max_n,len(i))
                 
        return max_n     

                 
        

            