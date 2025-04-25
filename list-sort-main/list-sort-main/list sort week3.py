'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
li=[12,32,34,45,3,56,67]
n=len(li)
for i in range(n):
    for j in range (0,n-i-1):
        if li[j]<li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
print(li)