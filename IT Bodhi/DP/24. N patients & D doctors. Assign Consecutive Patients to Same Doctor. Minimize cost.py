"""
Problem : N patients & D doctors. Assign consecutive patients to same doctor. Minimize cost.

    P1  P2  P3  P4
D1  1   2   15   3
D2  4   1   6   10
D3  8   21  3   1


    P1  P2  P3  P4
D1  1   3   18  21
D2  1   2   8   18
D3  1   2   5   6

D1-->D2-->D3-->D4
P1   P2   P3   P4
D3-->D3-->D2-->D1

MC(i, j, N) = min(for (k= 0->j-i+1)
                cost(N, j-k+1, j)
                + MC(i, j-k, N-1))

MC(i, N) = min(for (k= 0->i+1)
                cost(N, i-k+1, j)
                + MC(i, i-k, N-1))



TC: (N*M) * N
N : patients
M : doctors

"""

