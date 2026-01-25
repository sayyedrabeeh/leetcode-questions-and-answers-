class Solution:
    def climbStairs(self, n ,a={}):
        if n in a:
            return a[n]
        if n==1:
            return 1
        if n==2:
            return 2
        a[n]=self.climbStairs(n-1,a)+self.climbStairs(n-2,a)
        return a[n]
        
            
            
ss=Solution()
n=5
s1=ss.climbStairs(n)
print(s1)