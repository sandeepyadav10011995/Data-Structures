"""
N meetings In One Room | Greedy Algorithm

Approach 1: Sort the meeting according to finish time
            Then put them in the queue

            TC: O(N)--> Meeting entry + O(NlogN) -> sorting + O(N) --> iterating queue ~ O(NlogN)
            SC: O(N)

"""
from dataclasses import dataclass


@dataclass
class Meeting:
    start: int = None
    end: int = None
    pos: int = None


class Solution:
    @staticmethod
    def maxMeeting(start: list[int], end: list[int]) -> list[int]:
        N = len(start)
        meetings: list[Meeting] = []
        for i in range(N):
            meetings.append(Meeting(start=start[i], end=end[i], pos=i+1))

        # Sort the meetings w.r.t end time
        meetings.sort(key=lambda x: x.end)

        answer: list[int] = [meetings[0].pos]
        limit = meetings[0].end
        for i in range(1, N):
            if meetings[i].start > limit:
                limit = meetings[i].end
                answer.append(meetings[i].pos)

        return answer


sol = Solution()
print(sol.maxMeeting(start=[1, 0, 3, 8, 5, 8], end=[2, 6, 4, 9, 7, 9]))