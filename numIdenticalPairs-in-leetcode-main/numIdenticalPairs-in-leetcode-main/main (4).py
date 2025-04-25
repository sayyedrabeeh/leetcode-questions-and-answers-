'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Solution:
    def numIdenticalPairs(self, nums):
         n=0
         for i in range(len(nums)):
            for j in range(len(nums)):
                if nums [i]==nums[j] and i<j:
                    n=n+1
         return n
ss=Solution()
s1=[1,2,3,1,1,3]
s2=ss.numIdenticalPairs(s1)
print(s2)