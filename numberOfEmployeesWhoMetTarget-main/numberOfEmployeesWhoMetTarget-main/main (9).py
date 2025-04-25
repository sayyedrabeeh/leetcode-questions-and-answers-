'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        c=0
        for i in hours:
            if target <= i:
                c=c+1
        return c
ss=Solution()
s1=[0,2,1,5,3,4]
s2=ss.numberOfEmployeesWhoMetTarget(s1,3)
print(s2)