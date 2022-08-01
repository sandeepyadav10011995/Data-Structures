from heapq import *


def schedule_tasks(tasks, k):
  intervalCount = 0
  taskFrequencyMap = {}
  for char in tasks:
    taskFrequencyMap[char] = taskFrequencyMap.get(char, 0) + 1

  maxHeap = []
  # add all tasks to the max heap
  for char, frequency in taskFrequencyMap.items():
    heappush(maxHeap, (-frequency, char))

  while maxHeap:
    waitList = []
    n = k + 1  # try to execute as many as 'k+1' tasks from the max-heap
    while n > 0 and maxHeap:
      intervalCount += 1
      frequency, char = heappop(maxHeap)
      if -frequency > 1:
        # decrement the frequency and add to the waitList
        waitList.append((frequency+1, char))
      n -= 1

    # put all the waiting list back on the heap
    for frequency, char in waitList:
      heappush(maxHeap, (frequency, char))

    if maxHeap:
      intervalCount += n  # we'll be having 'n' idle intervals for the next iteration

  return intervalCount


def main():
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'b', 'a'], 3)))


main()







