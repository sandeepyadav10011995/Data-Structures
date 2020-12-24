class Solution:
    def _canPartition(self, start, arr, visited, k, running_bucket_sum, target_bucket_sum):
        if k == 1:
            return True
        if running_bucket_sum == target_bucket_sum:
            return self._canPartition(0, arr, visited, k - 1, 0, target_bucket_sum)
        for i in range(start, len(arr)):
            if not visited[i] and running_bucket_sum+arr[i] <= target_bucket_sum:
                visited[i] = True
                if self._canPartition(i+1, arr, visited, k, running_bucket_sum + arr[i], target_bucket_sum):
                    return True
                visited[i] = False
        return False

    def partitionKSubsets(self, arr, k):
        arr_sum = sum(arr)
        if k == 0 or arr_sum % k != 0:
            return False
        visited = [False] * len(arr)
        return self._canPartition(0, arr, visited, k, 0, arr_sum%k)


sol = Solution()
print(sol.partitionKSubsets(arr=[4, 3, 2, 3, 5, 2, 1], k=4))
