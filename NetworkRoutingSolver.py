#!/usr/bin/python3
from ArrayQueue import ArrayQueue
from CS312Graph import *
import time
import math

from HeapQueue import HeapQueue
from MyQueue import MyQueue


class NetworkRoutingSolver:
    def __init__(self):
        self.source = None
        self.dest = None
        self.network = None
        self.queue = None
        self.previous = None

    #  Initializes member variable network to the graph made by the GUI
    def initializeNetwork(self, network):
        assert(type(network) == CS312Graph)
        self.network = network
        self.source = None
        self.dest = None
        self.queue = None
        self.previous = None

    #  Called after computeShortestPaths, using the previous array computed there to
    #  return shortest path and cost
    def getShortestPath(self, destIndex):
        self.dest = destIndex
        edges = []
        total_length = 0
        #  Iterates backwards from destination node until it reaches the source node
        while self.source != destIndex:
            prevIndex = self.previous[destIndex]
            if prevIndex is None:
                #  Shortest path is not found, meaning the destination node is unreachable
                return {'cost': float('inf'), 'path': edges}
            prev_node = self.network.nodes[prevIndex]
            edge = None
            for i in range(len(prev_node.neighbors)):
                if prev_node.neighbors[i].dest.node_id == destIndex:
                    edge = prev_node.neighbors[i]
            edges.append((edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)))
            total_length += edge.length
            destIndex = prevIndex
        return {'cost': total_length, 'path': edges}

    #  Computes the shortest path from the source node to every node in the graph using
    #  Dijkstra's algorithm, and creates previous array to trace that path
    def computeShortestPaths(self, srcIndex, use_heap=False):
        self.source = srcIndex
        t1 = time.time()
        dist = []
        prev = []
        #  Dijkstra's
        for i in range(len(self.network.nodes)):
            dist.append(math.inf)
            prev.append(None)
        dist[srcIndex] = 0
        #  Defines which implementation of priority queue to use, based off flags set
        if not use_heap:
            self.queue = ArrayQueue(dist)
        else:
            self.queue = HeapQueue(dist, srcIndex)
        H = self.queue
        while len(H.listOfNodes) > 0:
            u = H.deleteMin(dist)
            nodeU = self.network.nodes[u]
            for i in range(len(nodeU.neighbors)):
                v = nodeU.neighbors[i].dest.node_id
                if dist[v] > dist[u] + nodeU.neighbors[i].length:
                    dist[v] = dist[u] + nodeU.neighbors[i].length
                    prev[v] = u
                    H.decreaseKey(v, dist)
        self.previous = prev
        t2 = time.time()
        return t2 - t1
