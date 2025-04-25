'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Solution:
    def returnToBoundaryCount(self, nums) :
      k=0
      c=0
      for i in nums:
        if i > 0:
            k=k+i
        else:
            k=k+i
        if k ==0:
            c=c+1
      return c
                    
ss=Solution()
li=[3,2,-3,-4]
s=ss.returnToBoundaryCount(li)
print(s)