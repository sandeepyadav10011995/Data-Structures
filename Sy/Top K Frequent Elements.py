# Python3 implementation to find k
# numbers with most occurrences in
# the given array
import heapq
 
# Function to print the k numbers with
# most occurrences
def print_N_mostFrequentNumber(arr, n, k):
     
    mp = dict()
     
    # Put count of all the distinct elements
    # in dictionary with element as the
    # key & count as the value.
    for i in range(0, n):
        if arr[i] not in mp:
            mp[arr[i]] = 0
        else:
            mp[arr[i]] += 1
             
    # Using heapq data structure
    heap = [(value, key) for key,
             value in mp.items()]
              
    # Get the top k elements
    largest = heapq.nlargest(k, heap)
 
    # Insert the data from the map to
    # the priority queue
    print(k, " numbers with most "
             "occurrences are:", sep = "")
              
    # Print the top k elements
    for i in range(k):
        print(largest[i][1], end =" ")
 
# Driver code
if __name__=="__main__":
     
    arr = [ 3, 1, 4, 4, 5, 2, 6, 1 ]
    n = len(arr)
    k = 2
     
    print_N_mostFrequentNumber(arr, n, k)
