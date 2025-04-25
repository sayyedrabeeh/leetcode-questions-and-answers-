'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Solution:
    def countPairs(self, nums, target) :
        c=0
        for i in range(len(nums)+1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]<target:
                     
                    c=c+1
        return  c
ss=Solution()
s1=[-6,2,5,-2,-7,-1,3]
s2=ss.countPairs(s1,-2)
print(s2)