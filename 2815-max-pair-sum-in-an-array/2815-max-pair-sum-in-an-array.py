class Solution:
    def maxSum(self, nums: List[int]) -> int:
        mx_d = {}
        mx_v = -1
        for i in nums:
            digit = max(str(i))
            prev = mx_d.get(digit)
            if prev is not None:
                mx_v = max(mx_v,prev + i)
            mx_d[digit] = max(prev or 0,i)
        return mx_v