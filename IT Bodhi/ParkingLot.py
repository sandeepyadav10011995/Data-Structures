"""
Parking Lot

class Interval:
    start: int
    end: int
    slotNo: int

    override the __lt__ to support minHeap

class ParkingLot
    __init__(N: int) -> None
        - N: minHeap Fixed Size
        - size: int To monitor the cur size of minHeap
        - freeSlot: [0, 0, 0] of N size -> To keep the track whether slot is free or not?
        - slotFreq: {i: 0 for i in range(N)}
        -
    _getMinSlotNo() -> int
        -
    allocateSpace(start: int, duration: int) -> msg "Allocated"/"Please wait for x units"
        - deallocateSpace(start)
        - Create an Interval and assign the min SlotNo from the pool of FreeSlot
        - Update the size
        - Update SlotFreq
    deallocateSpace(now: int) -> None
        - Free the slots if the time has already passed
        - Add the slotNo to the pool of freeSlot
        - Update the size
    getMostUsedSSlot() -> int


"""
from dataclasses import dataclass
from heapq import *


@dataclass
class Interval:
    start: int = None
    end: int = None
    slotNo: int =  None

    def __lt__(self, other):
        return self.end < other.end


class ParkingLot:
    def __init__(self, N: int) -> None:
        self.N = N
        self.size = 0
        self.minHeap = []
        self.freeSlot = [0 for _ in range(N)]
        self.freqSlot = {i: 0 for i in range(N)}
        self.mostUsedSpace = 0

    def _getMinSlot(self) -> int | None:
        for i in range(self.N):
            if self.freeSlot[i] == 0:
                return i
        return None

    def _updateMostAccessedSpace(self, slotNo: int) -> None:
        if self.freeSlot[self.mostUsedSpace] < self.freqSlot[slotNo]:
            self.mostUsedSpace = slotNo

    def allocateSpace(self, start: int, duration: int) -> str:
        self.deAllocateSpace(start)
        if self.size < self.N:
            newInterval = Interval(start=start,
                                   end=start+duration,
                                   slotNo=self._getMinSlot())
            heappush(self.minHeap, newInterval)
            self.size += 1
            self.freqSlot[newInterval.slotNo] += 1
            self._updateMostAccessedSpace(newInterval.slotNo)
            return "Allocated with Slot No as {newInterval.slotNo}"
        else:
            waitingDuration = start - self.minHeap[0].end
            return f"Please wait for {waitingDuration} units"

    def deAllocateSpace(self, now: int) -> None:
        while self.size > 0 and self.minHeap[0].end < now:
            deletedInterval = heappop(self.minHeap)
            self.freeSlot[deletedInterval.slotNo] = 0
            self.size -= 1

    def getMostUsedSpace(self) -> int:
        return self.mostUsedSpace
