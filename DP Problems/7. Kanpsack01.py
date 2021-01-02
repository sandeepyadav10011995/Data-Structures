class Solution:
    def _knapsack_recursive_bottom_up(self, values, weights, max_weight_constraint, cache):
        for total_items in range(1, len(values)+1):
            for max_weight in range(1, max_weight_constraint+1):
                # if total_items == 0 or max_weight == 0:
                #     cache[total_items][max_weight] = 0
                if max_weight >= weights[total_items - 1]:
                    cache[total_items][max_weight] = cache[total_items-1][max_weight]
                else:
                    with_item = values[total_items - 1] + cache[total_items-1][max_weight-weights[total_items - 1]]
                    without_item = cache[total_items-1][max_weight]
                    cache[total_items][max_weight] = max(with_item, without_item)
        return cache[len(values)][max_weight_constraint]

    def _knapsack_recursive_top_down(self, values, weights, max_weight, total_items, cache):
        # Base Cases
        if total_items == 0 or max_weight == 0:
            return 0

        if cache[total_items][max_weight] != 0:
            return cache[total_items][max_weight]

        cur_index = total_items - 1
        if weights[cur_index] > max_weight:
            cache[total_items][max_weight] = self._knapsack_recursive_top_down(values, weights, max_weight, total_items - 1, cache)
            return cache[total_items][max_weight]
        with_item = values[cur_index] + self._knapsack_recursive_top_down(values, weights, max_weight - weights[cur_index], total_items - 1, cache)
        without_item = self._knapsack_recursive_top_down(values, weights, max_weight, total_items - 1, cache)
        cache[total_items][max_weight] = max(with_item, without_item)
        return cache[total_items][max_weight]

    def _knapsack_dynamic(self, values, weights, max_weight, total_items, cache):
        for i in range(1, total_items+1):
            for j in range(1, max_weight+1):
                if j >= weights[i-1]:
                    cache[i][j] = max(cache[i-1][j], cache[i-1][j - weights[i-1]] + values[i-1])
                else:
                    cache[i][j] = cache[i-1][j]
        return cache[-1][-1]

    def knapsack(self, values, weights, max_weight):
        total_items = len(values)
        cache = [[0] * (max_weight+1) for _ in range(total_items+1)]
        # Recursive Solution --> Top Down
        # return self._knapsack_recursive_top_down(values, weights, max_weight, total_items, cache)
        # Recursive Solution --> Bottom Up
        # return self._knapsack_recursive_bottom_up(values, weights, max_weight, cache)
        # Dynamic Solution
        return self._knapsack_dynamic(values, weights, max_weight, total_items, cache)

values = [60, 50, 70, 30]
weights = [5, 3, 4, 2]
max_weight = 5
sol = Solution()
print(sol.knapsack(values, weights, max_weight))\
