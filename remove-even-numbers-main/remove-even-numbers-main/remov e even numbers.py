'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d={}
for i in dict1:
    if dict1[i]%2 != 0:
        d[i]=dict1[i]
print(d)