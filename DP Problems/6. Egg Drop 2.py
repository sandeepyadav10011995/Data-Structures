class Solution:
    def superEggDrop(self, K, N):
        memo = {}
        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    lo, hi = 1, n
                    # keep a gap of 2 X values to manually check later
                    while lo + 1 < hi:
                        x = int((lo + hi) / 2)
                        t1 = dp(k-1, x-1)
                        t2 = dp(k, n-x)

                        if t1 < t2:
                            lo = x
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x

                    ans = 1 + min(max(dp(k-1, x-1), dp(k, n-x))
                                  for x in range(lo, hi))

                memo[k, n] = ans
            return memo[k, n]
        return dp(K, N)
# class Solution:
#     def __init__(self):
#         self.memo = {}
#
#     def _eggDrop(self, total_eggs, total_floors):
#         """
#             If we have 0 floors we need 0 trials, no matter the egg amount given
#             If we have 1 floor we need 1 trial, no matter the egg amount given
#         """
#         if (total_eggs, total_floors) not in self.memo:
#             ans = 0
#             if total_floors == 0:
#                 ans = 0
#             elif total_eggs == 1:
#                 ans = total_floors
#             else:
#                 low, high = 1, total_floors
#                 """
#                     If we have 1 egg...no matter what floors we get, our approach will
#                     be to do 'floorAmount' drops...this is because we want to start from
#                     floor 1, drop...then go to floor 2, drop...and so on until we get to
#                     in the worst case 'floorAmount'
#                     Remember, we want to know the minimum amount of drops that will always
#                     work. So we want to MINIMIZE...to the absolute LEAST...worst...amount
#                     of drops so that our drop count ALWAYS works
#                     Any worse then the MINIMIZED WORST will be suboptimal
#                 """
#                 while low < high:
#                     mid = (low + high) / 2
#                     t1 = self._eggDrop(total_eggs-1, mid-1)
#                     t2 = self._eggDrop(total_eggs, total_floors-mid)
#                     if t1 < t2:
#                         low = mid
#                     elif t1 > t2:
#                         high = mid
#                     else:
#                         low = high = mid
#                 ans += 1 + min(max(self._eggDrop(total_eggs-1, x-1), self._eggDrop(total_eggs, total_floors-x)) for x in (low, high))
#             self.memo[total_eggs, total_floors] = ans
#         return self.memo[total_eggs, total_floors]
#         """
#             We want to know the cost of the 2 outcomes:
#             1.) We drop an egg and it breaks.
#             We move 1 floor down. We have 1 less egg.
#             2.) We drop an egg and it doesn't break.
#             We have this many floors left: the difference between the total floors and our current
#             floor. We have the same number of eggs.
#             After we get the cost of the WORST outcome we add 1 to that worst outcome
#             to simulate the fact that we are going to do a test from THIS sub-problem.
#             The answer to this problem is 1 PLUS the cost of the WORST SITUATION that
#             happens after our action at this sub-problem.
#         """

sol = Solution()
print(sol.superEggDrop(3, 14))
