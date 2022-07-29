from collections import deque


def find_subarrays(arr, target):
  result = []
  product = 1
  left = 0
  for right in range(len(arr)):
    product *= arr[right]
    while (product >= target and left <= right):
      product /= arr[left]
      left += 1
    # since the product of all numbers from left to right is less than the target therefore,
    # all subarrays from left to right will have a product less than the target too; to avoid
    # duplicates, we will start with a subarray containing only arr[right] and then extend it
    temp_list = deque()
    for i in range(right, left-1, -1):
      temp_list.appendleft(arr[i])
      result.append(list(temp_list))
  return result


def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print(find_subarrays([8, 2, 6, 5], 50))


main()



Time complexity#
The main for-loop managing the sliding window takes O(N)
O(N)
 but creating subarrays can take up to O(N^2)
O(N 
2
 )
 in the worst case. Therefore overall, our algorithm will take O(N^3)
O(N 
3
 )
.

Space complexity#
Ignoring the space required for the output list, the algorithm runs in O(N)
O(N)
 space which is used for the temp list.

Can you try estimating how much space will be required for the output list?
