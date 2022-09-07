# Python program for the above approach
from queue import PriorityQueue

def kthLargest(k, arr, n):
	ans = [0]*n

	# Creating a min-heap using priority queue
	pq = PriorityQueue()

	# Iterating through each element
	for i in range(n):
		# If size of priority
		# queue is less than k
		if (pq.qsize() < k):
			pq.put(arr[i])
		else:
			if (arr[i] > pq.queue[0]):
				pq.get()
				pq.put(arr[i])

	# If size is less than k
		if (pq.qsize() < k):
			ans[i] = -1
		else:
			ans[i] = pq.queue[0]

	return ans


# Driver Code
n = 6
arr = [1, 2, 3, 4, 5, 6]
k = 4

# Function call
v = kthLargest(k, arr, n)
print(*v)

# This code is contributed by Lovely Jain
