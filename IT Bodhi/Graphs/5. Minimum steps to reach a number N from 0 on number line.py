"""
Problem -: Minimum steps to reach a number N from 0 on number line
Mathematical Induction Proof -:
    N --> K steps
    N+1 --> K Steps - Left(K+1Steps) + Right(K+2 Steps) = K+1 Steps

                                0
                    -1                       1    --> 1 Steps
               -3        1              -1       3   --> 2 Steps
          -6       0  -2    4        -4     2  0    6  --> 3 Steps

          ................ and so on

    Logic -: BFS

    1 ==> 1
    2 ==> 3
    3 ==> 6
    4 ==> 10
    5 ==> 15
    6 ==> 21
    7 ==> 28

    Summation(N) ==> K Steps

    But if the number is between these numbers then use Left to optimize it
    K steps in Right
    i steps in Left

    Then we will land on ==> K - 2*i

    Which steps needs to be taken left  = Diff/2 :: Note : Diff should be even
    What is the Diff is odd ==>

    6                                                       7
    |                                                       |
    21      22       23       24      25      26      27    28
           7(-3)     9       7(-2)    9       7(-1)   9

22 ==> (28-22) = 6//2 = 3 :: Take the 3rd Step as left ==> 7
24 ==> (28-24) = 4//2 = 2 :: Take the 2nd Step as left ==> 7
26 ==> (28-26) = 2//2 = 1 :: Take the 1st Step as left ==> 7

23 ==> 24th Ans + 2 == 9
25 ==> 26th Ans + 2 == 9
27 ==> 28th Ans + 2 == 9


E(N) ==> We know the answer
E(N) - 2i ==> We know the answer --> Even --> Take ith step as left
E(N+1) ==> We know the answer --> Odd --> N+2
E(N+1) - OddNumber  ==> (N+1) +2 ==> N+3


-----------------------------------------------------------------------
FaceBook Friends
Users = 2 Billions
200 friends
Connect to friends
1     2     3     4
A --> T --> S --> K

Problem -: At every level the number of nodes are increasing exponentially.
Solution -: Generate the BFS from both the sides and get the intersection.
Steps:
    1. L1 : Level for A.
        Check if K is present int the Level L1.
    2. L2 : Level for K.
        Check if any element of L1 is present in L2.

"""