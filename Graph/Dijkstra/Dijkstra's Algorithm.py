"""
Implement Dijkstra's shortest path algorithm.

Given a weighted, directed graph, and a starting vertex, return the shortest distance from the starting vertex to every vertex in the graph.

Input:

n - the number of vertices in the graph, where (2 <= n <= 100). Each vertex is labeled from 0 to n - 1.
edges - a list of tuples, each representing a directed edge in the form (u, v, w), where u is the source vertex, v is the destination vertex, and w is the weight of the edge, where (1 <= w <= 10).
src - the source vertex from which to start the algorithm, where (0 <= src < n).
Note: If a vertex is unreachable from the source vertex, the shortest path distance for the unreachable vertex should be -1.

Example 1:

Dijkstra's Algorithm

Input:
n = 5
edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]
src = 0

Output:
{{0:0}, {1:7}, {2:3}, {3:9}, {4:5}}
"""


import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        dis = {u :float('inf') for u in range(n)}
        adj = {u: [] for u in range(n)}

        for u, v, w in edges:
            adj[u].append((v, w))
        
        heap = [(0, src)] #distance, src --> min heap
        dis[src] = 0

        while heap:
            d, u = heapq.heappop(heap)
            for v, w in adj[u]:
                if (d + w) < dis[v]:
                    dis[v] = d + w
                    heap.append((dis[v], v))
        
        for u, wt in dis.items():
            if wt == float('inf'):
                dis[u] = -1
        return dis
     
        

        

        
