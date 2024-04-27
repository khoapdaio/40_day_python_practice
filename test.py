import collections
from collections import deque
from typing import List


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    adj = [[] for _ in range(n)]
    output = [float('inf') for _ in range(n)]
    output[src] = 0

    for start, end, price in flights:
        adj[start].append((end, price))

    graph = deque()
    graph.append((src, -1, 0))
    while graph:
        start, stop, cost = graph.popleft()
        if stop >= k:
            continue
        for end, price in adj[start]:
            if cost + price < output[end]:
                output[end] = cost + price
                graph.append((end, stop + 1, cost + price))
    if output[dst] == float('inf'):
        return -1
    else:
        return int(output[dst])


def findCheapestPrice2(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    prices = [float('inf') for _ in range(n)]
    prices[src] = 0

    for i in range(k + 1):
        tempPrices = prices.copy()
        for start, end, price in flights:
            if prices[start] == float('inf'):
                continue
            if prices[start] + price < tempPrices[end]:
                tempPrices[end] = prices[start] + price
        prices = tempPrices
    return -1 if prices[dst] == float('inf') else int(prices[dst])


# print(findCheapestPrice2(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1))


def findAllPeople(n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
    meetings.sort(key=lambda x: x[2])
    meeting_dict = collections.defaultdict(list)
    for person1, person2, time in meetings:
        meeting_dict[time].append([person1, person2])

    has_secret = {0, firstPerson}
    for time, meetings in meeting_dict.items():
        graph = collections.defaultdict(list)
        seen = set()
        for person1, person2 in meetings:
            graph[person1].append(person2)
            graph[person2].append(person1)

            if person1 in has_secret:
                seen.add(person1)
            if person2 in has_secret:
                seen.add(person2)
        queue = collections.deque(seen)
        while queue:
            person = queue.popleft()
            for neighbor in graph[person]:
                if neighbor not in has_secret:
                    has_secret.add(neighbor)
                    queue.append(neighbor)
    return has_secret;


# print(findAllPeople(6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1))


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.count = n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])

        print(f"par[x] = {self.par[x]}")
        return self.par[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.size[px] < self.size[py]:
            self.par[px] = py
            self.size[py] += self.size[px]
        else:
            self.par[py] = px
            self.size[px] += self.size[py]
        self.count -= 1


def canTraverseAllPairs(nums: List[int]) -> bool:
    uf = UnionFind(len(nums))
    factor_index = {}
    for i, n in enumerate(nums):
        f = 2
        while f * f <= n:
            if n % f == 0:
                if f in factor_index:
                    print(uf.union(i, factor_index[f]))
                else:
                    factor_index[f] = i
                while n % f == 0:
                    n = n // f
            f += 1
        if n > 1:
            if n in factor_index:
                print(f"uf.union ={uf.union(i, factor_index[n])}")
            else:
                factor_index[n] = i
        print(f"factor_index = {factor_index}")
        print(f"uf.count={uf.count}")
    return uf.count == 1


print(canTraverseAllPairs([2, 3, 6]))
