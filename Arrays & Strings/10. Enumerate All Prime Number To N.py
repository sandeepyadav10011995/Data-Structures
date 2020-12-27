class Solution:
    def enumeratePrimes1(self, n): # Time Complexity ==> O(N^1.5)
        if n <= 1:
            return []

        output = []
        i = 2
        while i < n:
            j = 2
            is_prime = True
            while j < i:
                if i % j == 0:
                    is_prime = False
                j += 1

            if is_prime:
                output.append(i)
            i += 1

        return output

    def enumeratePrimes2(self, n): # Time Complexity ==> O(N*Log(Log(N)))
        if n <= 1:
            return []

        is_prime = [True for _ in range(n)]
        is_prime[0], is_prime[1] = False, False

        for i in range(n):
            if is_prime[i]:
                for j in range(i+i, n, i):
                    is_prime[j] = False

        output = [i for i in range(n) if is_prime[i]]
        return  output

sol = Solution()
print(sol.enumeratePrimes1(10))
print(sol.enumeratePrimes2(10))
