"""
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. 
The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. 
Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning 
and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6

Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

"""

class Solution:
    def getNeighbors(self, key: str) -> List[str]:
        neighbors = []
        for i in range(4):
            for j in [1, -1]:
                if int(key[i]) == 0 and j == -1:
                    dig = 9
                else:
                    dig = (int(key[i]) + j) % 10
                neighbors.append(key[:i]+str(dig)+key[i+1:])
        return neighbors
        
        
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = []
        if not "0000" in deadends:
            queue.append(('0000', 0))
            visited = {'0000'}
        while queue:
            key, count = queue.pop(0)
            if key == target:
                return count
            for nkey in self.getNeighbors(key):
                if nkey in deadends:
                    continue
                if nkey not in visited:
                    queue.append((nkey, count+1))
                    visited.add(nkey)
        return -1
