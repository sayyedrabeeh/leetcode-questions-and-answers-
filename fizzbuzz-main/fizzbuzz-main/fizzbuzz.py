'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Solution:
    def fizzBuzz(self, n: int):
      li=[]
      for i in range (1,n+1):
       
        if i % 3==0 and i % 5 ==0:
            li.append( 'fizzBuzz')
        elif i % 3==0 :
            li.append('Fizz')
        elif i % 5==0:
            li.append('Buzz')
        else:
            li.append(str(i))
      return  li 
    
ss= Solution()
s=ss.fizzBuzz(5)
print(s)