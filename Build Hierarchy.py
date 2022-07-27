"""
Build hierarchy tree reads employee data and build a corporation hierarchy tree from the list. HashMap plays important
role to store the data when reading the input. The trick of this question is to find the root. You can get the root by
finding the employee without the manager. Starting from the root, get subordinates for each employee. This way you the
build tree recursively.

Here are the steps of build hierarchy tree :
1. Define employee Class that has id, name and subordinates.
2. Read the data line by line, store the data in the HashMap. If the employee doesn't have managerId, he is at the top
   of hierarchy (root).
3. Use recursion to find subordinates and build nary tree.
4. Use recursion to print the hierarchy.

Note -: The data structure tree and HashMap are used.

"""
from typing import List


class Employee:
    subordinates = []

    # Constructor --> Time O(1), Space O(1)
    def __init__(self, id: int, name: str, mId: int = None) -> None:
        self.id = id
        self.name = name
        self.mId = mId


class BuildHierarchyTree:
    employees = {}
    root = None

    # Read data and build map, Iteration, Time O(n), Space O(n), n is number of employees
    def readDataAndCreateMap(self, employees: List[dict]) -> None:
        for emp in employees:
            employee = Employee(id=emp.get("id"), name=emp.get("name"), mId=emp.get("mid"))
            self.employees[employee.id] = employee
            if employee.mId is None:
                self.root = employee

    # Build tree, Recursion, Time O(n), Space O(h), n is number of employees, h is levels of hierarchy tree
    def buildHierarchyTree(self, root):
        employee = root
        subs = self.getSubsById(employee._id)
        employee.subordinates = subs
        if len(subs) == 0:
            return
        for em in subs:
            self.buildHierarchyTree(em)

    # Get subordinates list by given id, Time O(n), Space O(k) ~ O(n), k is number of subordinates
    def getSubsById(self, managerId):
        subs = []
        for em in self.employees.values():
            if em.mId == managerId:
                subs.append(em)
        return subs

    # Print tree, Recursion, Time O(n), Space O(h)
    def printHierarchyTree(self, root, level):
        for i in range(1, level, 1):
            print("\t", end="")
            if i == level - 1:
                print("|__", end='')
        print(root._name)
        subs = root.subordinates
        for em in subs:
            self.printHierarchyTree(em, level + 1)


lines = [
    {"id": 1, "name": "Rob Choi", "mid": 6},
    {"id": 2, "name": "Paul Marmolejo", "mid": 5},
    {"id": 3, "name": "Lois Lemer", "mid": 6},
    {"id": 4, "name": "Christie Jacobs", "mid": 5},
    {"id": 5, "name": "Moises Medina", "mid": 6},
    {"id": 6, "name": "Joseph Grant", "mid": None},
    {"id": 7, "name": "Andy Zuckeman", "mid": 1},
    {"id": 8, "name": "Melaney Partner", "mid": 3},
    {"id": 9, "name": "Cliff Gannett", "mid": 5},
    {"id": 10, "name": "Mark O'Donnell", "mid": 1}
]

tree = BuildHierarchyTree()
tree.readDataAndCreateMap(lines)
tree.buildHierarchyTree(tree.root)
tree.printHierarchyTree(tree.root, 0)


"""
Time Complexity : O(N)
Space Complexity : O(N)
"""
