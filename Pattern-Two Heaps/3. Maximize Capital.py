"""
In many problems, where we are given a set of elements such that we can divide them into two parts. We are interested
in knowing the smallest element in one part and the biggest element in the other part. The Two Heaps pattern is an
efficient approach to solve such problems.As the name suggests, this pattern uses two Heaps;
    Min Heap ---> smallest element
    Max Heap ---> biggest element

Problem Statement:  Given a set of investment projects with their respective profits, we need to find the most
                    profitable projects. We are given an initial capital and are allowed to invest only in a fixed
                    number of projects. Our goal is to choose projects that give us the maximum profit. Write a
                    function that returns the maximum total capital after selecting the most profitable projects.

    We can start an investment project only when we have the required capital. Once a project is selected, we can assume
    that its profit has become our capital.

Algo:
    While selecting projects we have two constraints:
        a.  We can select a project only when we have the required capital.
        b.  There is a maximum limit on how many projects we can select.

    Since we don’t have any constraint on time, we should choose a project, among the projects for which we have enough
    capital, which gives us a maximum profit. Following this greedy approach will give us the best solution.

    While selecting a project, we will do two things:
        a.  Find all the projects that we can choose with the available capital.
        b.  From the list of projects in the 1st step, choose the project that gives us a maximum profit.

    We can follow the Two Heaps approach similar to Find the Median of a Number Stream. Here are the steps of our
    algorithm:
        a.  Add all project capitals to a min-heap, so that we can select a project with the smallest capital
            requirement.
        b.  Go through the top projects of the min-heap and filter the projects that can be completed within our
            available capital. Insert the profits of all these projects into a max-heap, so that we can choose a
            project with the maximum profit.
        c.  Finally, select the top project of the max-heap for investment.
        d.  Repeat the 2nd and 3rd steps for the required number of projects.

Example 1:
    Input: Project Capitals=[0,1,2], Project Profits=[1,2,3], Initial Capital=1, Number of Projects=2
    Output: 6
    Explanation:
        a.  With initial capital of ‘1’, we will start the second project which will give us profit of ‘2’. Once we
            selected our first project, our total capital will become 3 (profit + initial capital).
        b.  With ‘3’ capital, we will select the third project, which will give us ‘3’ profit.
        c.  After the completion of the two projects, our total capital will be 6 (1+2+3).

Example 2:
    Input: Project Capitals=[0,1,2,3], Project Profits=[1,2,3,5], Initial Capital=0, Number of Projects=3
    Output: 8
    Explanation:
        a.  With ‘0’ capital, we can only select the first project, bringing out capital to 1.
        b.  Next, we will select the second project, which will bring our capital to 3.
        c.  Next, we will select the fourth project, giving us a profit of 5.
        d.  After selecting the three projects, our total capital will be 8 (1+2+5).

"""

from heapq import *


class MaximizeProfit:
    @staticmethod
    def find_maximum_capital(capitals: list[int], profits: list[int], no_of_projects: int, initial_capital: int):
        min_capital_heap = []
        max_profit_heap = []

        # insert all project capitals to a min-heap
        for i in range(0, len(profits)):
            heappush(min_capital_heap, (capitals[i], i))

        # let's try to find a total of 'numberOfProjects' best projects
        available_capital = initial_capital
        for _ in range(no_of_projects):
            # find all projects that can be selected within the available capital and insert them in a max-heap
            while min_capital_heap and min_capital_heap[0][0] <= available_capital:
                capital, i = heappop(min_capital_heap)
                heappush(max_profit_heap, (-profits[i], i))

            # terminate if we are not able to find any project that can be completed within the available capital
            if not max_profit_heap:
                break

            # select the project with the maximum profit
            available_capital += -heappop(max_profit_heap)[0]

        return available_capital


def main():
    mc = MaximizeProfit()
    print("Maximum capital: " + str(mc.find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " + str(mc.find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()

"""
Time Complexity: O(NlogN + KlogN) ==> N : No of Projects and K: No of projects to be selected 
Space Complexity: O(N)
"""
