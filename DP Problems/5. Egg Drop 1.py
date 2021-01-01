class Solution:
    def _eggDrop(self, total_eggs, total_floors, memo):
        """
            If we have 0 floors we need 0 trials, no matter the egg amount given
            If we have 1 floor we need 1 trial, no matter the egg amount given
        """
        for egg in range(1, total_eggs+1):
            memo[egg][0] = 0
            memo[egg][1] = 1
        """
            If we have 1 egg...no matter what floors we get, our approach will
            be to do 'floorAmount' drops...this is because we want to start from
            floor 1, drop...then go to floor 2, drop...and so on until we get to
            in the worst case 'floorAmount'
            Remember, we want to know the minimum amount of drops that will always
            work. So we want to MINIMIZE...to the absolute LEAST...worst...amount
            of drops so that our drop count ALWAYS works
            Any worse then the MINIMIZED WORST will be suboptimal
        """
        for floor in range(1, total_floors+1):
            memo[1][floor] = floor

        for egg in range(2, total_eggs+1):
            for floor in range(2, total_floors+1):
                for attempt_floor in range(1, floor):
                    """
                        We want to know the cost of the 2 outcomes:
                        1.) We drop an egg and it breaks.
                        We move 1 floor down. We have 1 less egg.
                        2.) We drop an egg and it doesn't break.
                        We have this many floors left: the difference between the total floors and our current
                        floor. We have the same number of eggs.
                    """
                    cost_of_worst_outcome = max(memo[egg-1][attempt_floor-1], memo[egg][floor-attempt_floor])
                    """
                        After we get the cost of the WORST outcome we add 1 to that worst outcome
                        to simulate the fact that we are going to do a test from THIS sub-problem.
                        The answer to this problem is 1 PLUS the cost of the WORST SITUATION that
                        happens after our action at this sub-problem.
                    """
                    accounting_to_sub_problem = 1 + cost_of_worst_outcome
                    memo[egg][floor] = min(memo[egg][floor], accounting_to_sub_problem)
        return memo[-1][-1]

    def eggDrop(self, total_eggs, total_floors):
        memo = [[float('inf') for floors in range(total_floors + 1)] for eggs in range(total_eggs + 1)]
        return self._eggDrop(total_eggs, total_floors, memo)

sol = Solution()
print(sol.eggDrop(3, 14))
