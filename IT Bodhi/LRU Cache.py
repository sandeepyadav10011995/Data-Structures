"""
========================= LRU CACHE ===============================
Cache Eviction Policies
    LIFO : Last In First Out
    FIFO: First In First Out {It reduces the CPU Efficiency}
    LRU: Least Recently Used
    OPTIMAL: We replace entry which will not be referred for maximum duration in near future.

What is Cache?
- Store the data to speed up the same future requests.
- Maybe a previous computation or a redundant copy of data.

LRU CACHE -:
    - get() --> O(1)  ==> Fast LookUp  -: Hash Tables
    - put() --> O(1)  ==> Fast Removals -: Doubly Linked List :: If we have instant access to the node we can remove it
                                                                 O(1) time complexity.


"""
from dataclasses import dataclass
from typing import Any


@dataclass
class DLL:
    key: int = 0
    val: int = 0
    prev: Any = None
    next: Any = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLL(), DLL()
        # Connect the Head and Tail nodes
        self.head.next = self.tail
        self.tail.prev = self.head

    def _addNode(self, node: DLL) -> None:
        pred = self.head
        succ = self.head.next
        pred.next = node
        node.prev = pred
        succ.prev = node
        node.next = succ

    @staticmethod
    def _removeNode(node: DLL) -> None:
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred

    def _moveToHead(self, node) -> None:
        self._removeNode(node)
        self._addNode(node)

    def _popTail(self) -> DLL:
        res = self.tail.prev
        self._removeNode(res)
        return res

    def get(self, key: int) -> int:
        node: DLL = self.cache.get(key, None)
        if not node:
            return -1

        self._moveToHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # sourcery skip: extract-method, swap-if-else-branches, use-named-expression
        node: DLL = self.cache.get(key, None)
        if not node:
            newNode = DLL()
            newNode.key = key
            newNode.val = value

            self.cache[key] = newNode
            self._addNode(newNode)
            self.size += 1

            # Check the capacity constraints
            if self.size > self.capacity:
                # pop the tail
                tail = self._popTail()
                # delete the entry from cache of the popped node
                del self.cache[tail.key]
                self.size -= 1
        else:
            # Update the value and move to head
            node.val = value
            self._moveToHead(node)
