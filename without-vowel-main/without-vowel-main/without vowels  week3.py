'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
mystring = "hello wrld"
vowels = "aeiouAEIOU"
newstr = ""
num = 0
for x in mystring:
    if x not in vowels:
        newstr += x
    else:
        num += 1
print(newstr) 
print(num)