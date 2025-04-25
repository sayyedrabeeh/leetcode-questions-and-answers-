'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Solution:
    def searchInsert(self, nums, target):
         
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if  nums[i]>target:
                    return i 
                
            return len(nums)
  
ss=Solution()
s=2
s1=[1,3,5,6]
s2=ss.searchInsert(s1,s)
print(s2)