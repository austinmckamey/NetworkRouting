import math

from MyQueue import MyQueue


class ArrayQueue(MyQueue):

    def __init__(self, nodes):
        self.listOfNodes = []
        for i in range(len(nodes)):
            self.listOfNodes.append(i)

    def insert(self, node, distances):
        self.listOfNodes.append(node)

    def makeQueue(self, nodes):
        for i in range(len(nodes)):
            self.insert(i, nodes)
        return self

    def deleteMin(self, distances):
        minimum = math.inf
        toReturn = None
        toRemove = None
        for i in range(len(self.listOfNodes)):
            if distances[self.listOfNodes[i]] <= minimum:
                minimum = distances[self.listOfNodes[i]]
                toReturn = self.listOfNodes[i]
                toRemove = i
        del self.listOfNodes[toRemove]
        return toReturn

    def decreaseKey(self, node, distances):
        pass
