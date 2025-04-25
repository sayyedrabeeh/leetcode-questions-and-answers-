'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

dict1= {'a': 100, 'b': 300, 'c': 250}
k=0
v=0
for i in dict1:
    if v ==0 or dict1[i]>v:
        v=dict1[i]
        k=i
         
print(k)
print(v)


    