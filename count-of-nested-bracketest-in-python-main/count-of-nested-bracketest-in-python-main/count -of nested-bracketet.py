'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Solution:
    def maxDepth(self, s: str) -> int:
        c=0
        m=0
        for i in s:
            if i =='(':
               
                c=c+1
                if c > m :
                    m=c 
                
            elif i ==')':
                c=c-1
        return m
        

ss=Solution()
string1="(1+(2*3)+((8)/4))+1"
 
s=ss.maxDepth(string1)
print(s)