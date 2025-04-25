'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Solution:
    def maxProductDifference(self, nums) :
        a=sorted(nums)
        b=(a[-1]*a[-2])-(a[0]*a[1])
        return b
ss=Solution()
s1=[5,6,2,7,4]
s2=ss.maxProductDifference(s1)
print(s2)