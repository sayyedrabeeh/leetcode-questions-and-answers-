'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        a=max(candies)
        b=0
        l=[]
        for i in candies:
           b=i+extraCandies
           if b >=a:
             l.append(True)
           else:
             l.append(False)
        return l      
ss=Solution()
s1=[0,2,1,5,3,4]
s2=ss.kidsWithCandies(s1,3)
print(s2)