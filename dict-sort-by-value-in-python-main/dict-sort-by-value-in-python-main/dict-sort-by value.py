'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
test_dict = {"Gfg" : 5, "is" : 7, "Best" : 2, "for" : 9, "geeks" : 8}
res={key:val  for key, val in sorted(test_dict.items(),key=lambda 
i: i[1])}

print(str(res))