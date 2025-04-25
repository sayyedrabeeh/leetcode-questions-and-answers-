'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Solution:
    def minimumOperations(self, nums):
        c=0
        for i in range(len(nums)):
            if nums[i]%3!=0:
                if (nums[i]+1)%3==0:
                    nums[i]+=1
                    c=c+1
                else:
                    nums[i]-=1
                    c=c+1
        return c
ss=Solution()
s1=[3,6,9]
s2=ss.minimumOperations(s1)
print(s2)