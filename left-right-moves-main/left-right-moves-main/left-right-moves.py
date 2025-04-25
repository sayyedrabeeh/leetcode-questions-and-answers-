'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Solution:
    def furthestDistanceFromOrigin(self, moves):
        x=0
        y=x
        l=0
        for i in moves:
            if i =='R':
                x=x+1
            elif i =='L':
                y=y+1
            
            elif i =='_':
                l=l+1
        return max(x+l,y+l)-min(x,y)

ss=Solution()
s="_R__LL_"
s1=ss.furthestDistanceFromOrigin(s)
print(s1)