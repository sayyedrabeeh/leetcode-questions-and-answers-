'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
       if b < a:
          c=b
       else:
          c=a
       k=0
       for i in range(1,c+1):
            if a % i==0 and b % i ==0:
                k=k+1
       return k

       

ss=Solution()
s=ss.commonFactors(6,12)
print(s)