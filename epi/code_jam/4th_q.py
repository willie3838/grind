'''
- dfs until leaf node and then calculate the maximum fun factor
- we use a heap to ensure that we always go on the minimum path first


'''
import heapq
from sys import stdin, stdout
from collections import defaultdict

T = int(input())

for test in range(1, T+1):
    N = int(input())
    F = [0] + [int(x) for x in stdin.readline().split()]
    P = [0] + [int(x) for x in stdin.readline().split()]

    tree = defaultdict(list)
    for i in range(1, N+1):
        tree[P[i]].append(i)
    
    print(F,P,tree)
    totalFun = 0
    
    visited = [False for i in range(N+1)]
    visited[0] = True
    
    heap = [(0,0)]
    heapq.heapify(heap)
    while heap:
        currFun, currNode = heapq.heappop(heap)
        children = tree[currNode]

        if len(children) == 0:
            currMax = 0
            while not visited[currNode]:
                currMax = max(currMax, F[currNode])
                visited[currNode] = True
                currNode = P[currNode]
            totalFun += currMax
            continue

        for child in children:
            heapq.heappush(heap, (F[child], child))

    print("Case #%d: %d" %(test, totalFun))