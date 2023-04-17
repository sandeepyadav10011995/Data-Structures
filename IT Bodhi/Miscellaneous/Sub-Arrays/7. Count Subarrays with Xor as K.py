"""
Count Sub-arrays with Xor as K

Approach 1: BF
            TC: O(N^3) --> O(N^2)
Approach 2: Prefix XOR
           _ _ _ _ _ _ _ _ _
XOR        -----Y---|----K--
XOR        ----------XR-----

Therefore Y^K = XR
==> Y = XR^K


Example -: [4, 2, 2, 6, 4]
K = 6
XOR = 0
XOR ^ 4 = 4
XOR ^ 2 = 6
XOR ^ 2 = 4 ==> 4^K ==> 4 ^ K = 2

count = 0-> 1
freqCount = {4: 1->2, 6: 1,

TC: O(N)
SC: O(N)

"""


class Solution:
    @staticmethod
    def countSubArrayWithXORAsK(nums: list[int], K: int) -> int:
        count = 0
        xorr = 0
        freqMap = {}
        N = len(nums)
        for i in range(N):
            xorr ^= nums[i]
            if xorr^K in freqMap:
                count += freqMap[xorr^K]
            if xorr == K:
                count += 1

            if xorr not in freqMap:
                freqMap[xorr] = 0
            freqMap[xorr] += 1

        return count
