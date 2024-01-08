class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
        
    def insertKey(self, item):
        self.heap.append(item)
        self.size += 1
        
        currentIndex = self.size - 1
        
        while currentIndex > 0:
            parentIndex = (currentIndex - 1) // 2
            if self.heap[parentIndex] > self.heap[currentIndex]:
                print(f"Swapping {parentIndex} and {currentIndex} ie values {self.heap[parentIndex]} and {self.heap[currentIndex]}")
                self.heap[parentIndex], self.heap[currentIndex] = self.heap[currentIndex], self.heap[parentIndex]
                currentIndex = parentIndex
            else:
                break
        print(f"Heap => {self.heap}")

    def getMin(self):
        return self.heap[0]
    
    def removeTop(self):
        topValue = self.heap[0]
        self.size -= 1
        heap = self.heap

        index = 0

        while index < self.size // 2:
            print(heap)
            nextIndex = index * 2 + 1 if heap[index * 2 + 1] < heap[index * 2 + 2] else index * 2 + 2
            print(index, nextIndex)
            heap[index] = heap[nextIndex]
            index = nextIndex
        self.heap = heap[:-1]
        



        
    def printHeap(self):
        print(self.heap)
                



heapObj = MinHeap()
heapObj.insertKey(15)
heapObj.insertKey(5)
heapObj.insertKey(3)
heapObj.insertKey(2)
heapObj.insertKey(4)
heapObj.printHeap()
heapObj.removeTop()
heapObj.removeTop()
heapObj.removeTop()
heapObj.printHeap()