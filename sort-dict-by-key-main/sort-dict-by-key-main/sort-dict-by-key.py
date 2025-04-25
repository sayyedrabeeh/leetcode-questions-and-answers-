'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
dict1={'a':10,'c':8,'b':15,'d':5}
dict2={key:val  for key,val in sorted(dict1.items(),key=lambda i:i[0])}
print(dict2)
res = {key: val for key, val in sorted(dict1.items(), key = lambda ele: ele[0])}
print(res)