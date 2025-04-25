'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Solution:
    def buildArray(self, nums):
        n=len(nums)
        ans=[0]*n
        for i in range(n):
            ans[i]=nums[nums[i]]
        return  ans
ss=Solution()
s1=[0,2,1,5,3,4]
s2=ss.buildArray(s1)
print(s2)