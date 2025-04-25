'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Solution:
    def convertTemperature(self, celsius: float):
      li=[]
      kelvin=celsius+273.15
      fahrenheit=celsius*1.80+32.00
      li.append(kelvin)
      li.append(fahrenheit)
      return li
ss=Solution()
s=ss.convertTemperature(36.50)
print(s)