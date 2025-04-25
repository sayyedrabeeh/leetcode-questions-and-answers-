'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
li=[1,2,3,4,5,6]
print(li)
lis=li[::-1]
print(lis)




print(li)
l=len(li)
i=0
while i < l//2:
  li[i],li[l-i-1]=li[l-i-1],li[i]
  i=i+1
print(li)