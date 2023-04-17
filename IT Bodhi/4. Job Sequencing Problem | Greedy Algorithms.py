"""
Job Sequencing Problem | Greedy Algorithms
Approach : Sort the Jobs according to profit first
           Perform the job at the latest deadline -> The latter, the better
           DP array size = max deadline value assigned as -1
           Iterate over the jobs and perform them


        TC: NlogN -> sorting + O(N*M) M -: Last Deadline value
        SC: O(M)

"""
from dataclasses import dataclass


@dataclass
class Job:
    id: int = None
    deadline: int = None
    profit : int = None


class Solution:
    @staticmethod
    def maxJobSequencingProfit(jobs: list) -> (int, int):
        N = len(jobs)
        modifiedJobs = [Job(id=job[0], deadline=job[1], profit=job[2]) for job in jobs]

        modifiedJobs.sort(key=lambda x:x.profit, reverse=True)
        maxDeadline = 0
        for i in range(N):
            if modifiedJobs[i].deadline > maxDeadline:
                maxDeadline = modifiedJobs[i].deadline

        deadlineArr = [-1 for _ in range(maxDeadline)]

        maxJobProfit = 0
        countJobs = 0

        for i in range(N):
            for j in range(maxDeadline-1, -1, -1):
                if deadlineArr[j] == -1:  # Free Slot
                    deadlineArr[j] = i
                    countJobs += 1
                    maxJobProfit += modifiedJobs[i].profit
                    break

        return countJobs, maxJobProfit


j = [(1, 4, 20), (2, 5, 60), (3, 6, 70), (4, 6, 65), (5, 4, 25), (6, 2, 80), (7, 2, 10), (8, 2, 22)]
sol = Solution()
print(sol.maxJobSequencingProfit(jobs=j))
