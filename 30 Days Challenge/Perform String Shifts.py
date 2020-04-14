"""
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:
direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.

A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.

Example:
Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"

Constraints:
1 <= s.length <= 100
s only contains lower case English letters.
1 <= shift.length <= 100
shift[i].length == 2
0 <= shift[i][0] <= 1
0 <= shift[i][1] <= 100

"""
# Optimized Solution
class Solution:
    def helper(self, s: str, count: int, flag: int) -> str:
        # Base Case --> If the shift value i.e. count > length of the string i.e. s
        count = count % len(s)
        if flag == 0:
            return s[count:] + s[:count]
        else:
            return s[-count:] + s[:-count]
        
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        ls = 0
        rs = 0
        for i in shift:
            if i[0] == 0:
                ls += i[1]
            else:
                rs += i[1]
                
        if ls > rs:
            ls -= rs
            rs = 0
        elif rs > ls:
            rs -= ls
            ls = 0
        else:
            return s
        
        if ls != 0:
            return self.helper(s, ls, flag=0)
        else:
            return self.helper(s, rs, flag=1)
        

