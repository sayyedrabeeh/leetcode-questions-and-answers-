'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_num = sorted(nums)
        dict_map = {}
        for i ,num in enumerate(sorted_num):
            if num not in dict_map:
                dict_map[num] = i
        return [dict_map[num] for num in nums]
ss=Solution()
s1=[8,1,2,2,3]
s2=ss.smallerNumbersThanCurrent(s1)
print(s2)
        