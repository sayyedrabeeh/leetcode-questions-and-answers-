class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        a = {}
        t = 0
        for i in nums:
            if i  in a :
                a[i] +=1
            else:
                a[i] = 1
        b = max(a.values())
        for k,v in a.items():
            if v == b:
                t+=v
        return t
