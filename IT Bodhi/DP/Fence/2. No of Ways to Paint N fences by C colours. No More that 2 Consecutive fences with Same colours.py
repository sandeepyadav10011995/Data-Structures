"""
Problem : No of ways to paint N fences by C colours. No more that 2 consecutive fences with same colours.
Colors -: R, G, B
Fences -: N

Case 1: No Rules
F(N) = C^N

Case 2: No Consecutive with Same Color
F(N) = C*(C-1)^(N-1)

Case 3: Not more than two Consecutive
F(N) = Last two colors are different(F(N-1)*(X-1)) + Last two colors are same(F(N-2)*(X-1))

F(N) = F(N-1)*(X-1) + F(N-2)*(X-1)
F(N) = (X-1) * (F(N-1)+F(N-2))

Therefore F(N) = (C-1) * (F(N-1)+F(n-2))

Case 3: Not more than 3 Consecutive
F(N) = Last 1 Same + Last 2 Same + Last 3 Same


Case 4: Not more than K Consecutive
F(N) = (C-1) * Summation(N-K) (low=i=1, high=k)
TC: O(N*K) --> Soltuion
SC: O(N)
"""

