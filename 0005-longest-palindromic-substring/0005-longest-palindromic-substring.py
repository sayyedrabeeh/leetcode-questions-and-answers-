class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        result = ''
        for i in range(len(s)):
            oddExpand = expand(i,i)
            evenExpand = expand(i,i + 1)

            if len(oddExpand) > len(result):
                result = oddExpand
            if len(evenExpand) > len(result):
                result = evenExpand
        return result 