'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Solution:
    def defangIPaddr(self, address: str) -> str:
        a='0'
        for i in address:
            if i =='.':
                a='[.]'
            else:
                a=i
        return a

ss=Solution()
st="1.1.1.1"
s=ss.defangIPaddr(st)
print(s)