'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Solution:
 def averageValue(self, nums) -> int:
    sum=0
    c=0
    for i in nums:
        if i % 2 == 0 and i % 3 == 0:
            sum=sum+i
            c=c+1 
    avg=sum/c
    return avg

ss=Solution()
li=[1,3,6,10,12,15]
s=ss.averageValue(li)
print(s)