'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
p='my name is sayyed rabeeh'
vowels='aeiou'
l={i:0 for i in vowels}
for i in p :
    if i in l:
        l[i]=l[i]+1
print(l)