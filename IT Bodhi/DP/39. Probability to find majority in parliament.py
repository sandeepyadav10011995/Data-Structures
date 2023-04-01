"""
Problem : Probability to find majority in parliament.
Ex-:
Constituencies:         1   2   3   4   5   6
Winning Probability:   P1, P2, P3, P4, P5, P6
Losing Probability:    1-P1....

Lets say Party A wills Half of the Constituencies, then calculate the Probability of majority.
    N
    __
    ll P(i)  --> Probability To win all the Constituencies. ==> Pmax
    i=1
Majority Probability = Pmax * (1-Pj) * (1-Pk)/(Pj*Pk)

F(N, i) ==> F(10, 3) --> Out of 10 seats if you win 3 seats


F(N, i) = Win:: (F(N-1, i-1)*P(N))  +  Loss:: F(N-1, i)*(1-P(N))
Example-:

    0   1   2   3   4   5
P1
P2
P3          X   Y
P4              *
P5

* --> 3, 3
F(i, j) = Win:: X*P4      + Loss:: Y*(1-P4))

"""


class Solution:
    @staticmethod
    def majorityProbability(probability, N):
        P = len(probability)

        grid = [[0 for _ in range(N+1)] for _ in range(P)]
        # Fill the 0 seats probability
        prevLossProb = 1
        for p in range(P):
            prevLossProb *= (1 - probability[p])
            grid[p][0] = prevLossProb
        grid[0][1] = probability[0]

        for p in range(P):
            for i in range(1, N):
                grid[p][i] = grid[p-1][i-1]*probability[p] + grid[p-1][i]*(1-probability[p])
        # Majority Ans = sum(P5 --> 3, 4, 5)
        return sum(grid[-1][N//2:])


sol = Solution()
num_seats = 5
party_probs = [0.6, 0.5, 0.7, 0.4, 0.55]
print(sol.majorityProbability(probability=party_probs, N=num_seats))
