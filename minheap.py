class minHeap:
    def __init__(self):
        self.heap = []

    def _leftIndex(index):
        return 2 * index + 1

    def _rightIndex(index):
        return 2 * index + 2

    def _parentIndex(index):
        return (index-1)//2

    def printHeap(self):
        i = 1
        j = 1
        for item in self.heap:
            print(item,end=" ")
            i -= 1
            if not i:
                i = 2 ** j
                j += 1
                print()
        print()
        return

    def printVerifyHeap(self):
        end = len(self.heap)
        children = []
        for index, value in enumerate(self.heap):
            left = minHeap._leftIndex(index)
            right = minHeap._rightIndex(index)
            if left < end:
                children.append(self.heap[left])
            if right < end:
                children.append(self.heap[right])
            print("Value/Min: {}/{} Children: {}".format(value, min(children+[value]), children))
            children = []
        return

    def isHeap(self):
        end = len(self.heap)
        children = []
        for index, value in enumerate(self.heap):
            left = minHeap._leftIndex(index)
            right = minHeap._rightIndex(index)
            if left < end:
                children.append(self.heap[left])
            if right < end:
                children.append(self.heap[right])
            if value == min(children + [value]):
                children = []
                continue
            else:
                return False
        return True

    def insert(self, value):
        index = len(self.heap)
        self.heap.append(value)
        parent = minHeap._parentIndex(index)
        while self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            if index == 0:
                break
            parent = minHeap._parentIndex(index)
        return

    def getChildren(self,index) -> [('index','value'),('index','value')]:
        end = len(self.heap)
        if index >= end or index < 0:
            raise IndexError("Index {} outside heap size {}".format(index, end))
        returnList = []
        leftIndex = minHeap._leftIndex(index)
        rightIndex = minHeap._rightIndex(index)
        for i in (leftIndex, rightIndex):
            if i < end:
                returnList.append((i, self.heap[i]))
        return returnList

    def swapWithChildren(self, index):
        #swaps node with its smallest child, returns 0 if no swap occurs, otherwise returns
        #new index of given value
        children = self.getChildren(index)
        children.sort(key=lambda x: x[1])
        values = [child[1] for child in children]
        if self.heap[index] == min(values+[self.heap[index]]):
            return 0
        else:
            new_index = children[0][0]
            self.heap[index], self.heap[new_index] = self.heap[new_index], self.heap[index]
            return new_index

    def extract(self):
        if len(self.heap) == 0:
            raise IndexError("Cannot extract from empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()
        returnValue = self.heap[0]
        self.heap[0] = self.heap.pop()
        index = 0
        while True:
            index = self.swapWithChildren(index)
            if index == 0:
                break
        return returnValue





H = minHeap()
for item in [6,5,8,9,2,5,7,4,4,5,7,9,3,4,5,6,5,7]:
    H.insert(item)

H.printHeap()
H.printVerifyHeap()
print(H.isHeap())
print(H.extract())
print()
H.printHeap()
H.printVerifyHeap()
print(H.isHeap())