'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Solution:
    def smallestEvenMultiple(self, n: int):
        
        if  n %2 ==0:
            return n
        else:
            
         return n*2

ss=Solution()
s=ss.smallestEvenMultiple(5)
print(s)