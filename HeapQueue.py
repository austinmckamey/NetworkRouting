import math

from MyQueue import MyQueue


class HeapQueue(MyQueue):

    def __init__(self, nodes, srcIndex):
        self.pointerList = []
        self.listOfNodes = []
        for i in range(len(nodes)):
            self.listOfNodes.append(i)
            self.pointerList.append(i)
        self.bubbleUp(srcIndex, nodes)
        self.currentSize = len(nodes)

    def bubbleUp(self, i, distances):
        while i != 0:
            f = math.floor((i-1)/2)
            if distances[self.listOfNodes[i]] < distances[self.listOfNodes[f]]:
                temp = self.listOfNodes[f]
                self.listOfNodes[f] = self.listOfNodes[i]
                self.listOfNodes[i] = temp
                self.pointerList[self.listOfNodes[f]] = f
                self.pointerList[self.listOfNodes[i]] = i
                i = f
            else:
                return

    def siftDown(self, i, distances):
        while (i*2 + 1) < self.currentSize:
            smallestChild = self.minChild(i, distances)
            if distances[self.listOfNodes[i]] > distances[self.listOfNodes[smallestChild]]:
                temp = self.listOfNodes[i]
                self.listOfNodes[i] = self.listOfNodes[smallestChild]
                self.listOfNodes[smallestChild] = temp
                self.pointerList[self.listOfNodes[i]] = i
                self.pointerList[self.listOfNodes[smallestChild]] = smallestChild
                i = smallestChild
            else:
                return

    def minChild(self, i, distances):
        first = i*2 + 1
        last = i*2 + 2
        if last > self.currentSize - 1:
            return first
        else:
            if distances[self.listOfNodes[first]] < distances[self.listOfNodes[last]]:
                return first
            else:
                return last

    def insert(self, node, distances):
        self.listOfNodes.append(node)
        self.pointerList.append(node)
        self.currentSize += 1
        self.bubbleUp(self.currentSize - 1, distances)

    def makeQueue(self, nodes):
        for i in range(len(nodes)):
            self.insert(i, nodes)
        return self

    def deleteMin(self, distances):
        toReturn = self.listOfNodes[0]
        self.listOfNodes[0] = self.listOfNodes[self.currentSize - 1]
        self.pointerList[self.listOfNodes[0]] = 0
        self.pointerList[toReturn] = -1
        del self.listOfNodes[self.currentSize - 1]
        self.currentSize -= 1
        self.siftDown(0, distances)
        return toReturn

    def decreaseKey(self, node, distances):
        index = self.pointerList[node]
        self.bubbleUp(index, distances)
