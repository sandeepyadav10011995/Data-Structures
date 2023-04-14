"""
Problem : Paint N fences with X colours
        Variant 1-: No two fences with same colour.
        Variant 2-: No more than two fences with same colour.


Variant 1-: No two fences with same colour.
F(N) = X * (X-1)^(N-1)

Variant 2-: No more than two fences with same colour.
X = R, B, Y
For N = 2 --> X*X = X^2 = 3^2 = 9
For N = 3 --> X(X^2 - 1) = 3^2 - 3 = 6
For N = 4 --> But this above will not work for N > 3

F(N) = Last two colors are same(F(N-2)*(X-1)) + Last two colors are different(F(N-1)*(X-1))

F(N) = F(N-2) * (X-1) + F(N-1) * (X-1)
F(N) = (X-1) * (F(N-2) + F(N-1))

"""


class Solution:
    def fillXColorsOnNPositionsVariantB(self, N, X):
        # Base Case
        if N <= 0:
            return 0
        if N == 1:
            return X
        if N == 2:
            return X * X

        return (X - 1) * (
                    self.fillXColorsOnNPositionsVariantB(N - 2, X) + self.fillXColorsOnNPositionsVariantB(N - 1, X))

    def fillXColorsOnNPositionsVariantBMemo(self, N, X, memo):
        # Base Case
        if N <= 0:
            return 0
        if N == 1:
            return X
        if N == 2:
            return X * X

        if memo[N] < 0:
            memo[N] = (X - 1) * \
                      (self.fillXColorsOnNPositionsVariantBMemo(N - 2, X, memo) +
                       self.fillXColorsOnNPositionsVariantBMemo(N - 1, X, memo))
        return memo[N]


sol = Solution()
print(sol.fillXColorsOnNPositionsVariantB(N=1, X=3))
print(sol.fillXColorsOnNPositionsVariantB(N=2, X=3))
print(sol.fillXColorsOnNPositionsVariantB(N=3, X=3))
print(sol.fillXColorsOnNPositionsVariantB(N=4, X=3))
print(sol.fillXColorsOnNPositionsVariantB(N=5, X=3))
print()
print("*"*50+"DP Solution"+"*"*50)
print()
print(sol.fillXColorsOnNPositionsVariantBMemo(N=1, X=3, memo=[-1 for _ in range(2)]))
print(sol.fillXColorsOnNPositionsVariantBMemo(N=2, X=3, memo=[-1 for _ in range(3)]))
print(sol.fillXColorsOnNPositionsVariantBMemo(N=3, X=3, memo=[-1 for _ in range(4)]))
print(sol.fillXColorsOnNPositionsVariantBMemo(N=4, X=3, memo=[-1 for _ in range(5)]))
print(sol.fillXColorsOnNPositionsVariantBMemo(N=5, X=3, memo=[-1 for _ in range(6)]))
