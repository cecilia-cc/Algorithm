# 参考261
import collections

class Solution:
    def graphHasCircle(self, n, edges):
        if len(edges)!= n-1:
            return False

        visited = collections.defaultdict(bool)
        graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            visited[x]=False
            visited[y]=False

        print(visited)
        print(graph)
        travese = []
        p = collections.deque()
        first=edges[0][0]
        p.append(first)
        visited[first] = True
        while p:
            cur = p.popleft()
            travese.append(cur)
            for c in graph[cur]:
                if not visited[c]:
                    visited[c] = True
                    p.append(c)
        print(travese)
        return len(travese) == n

s=Solution()
print(s.graphHasCircle(5, [[7,1], [7,2], [7,3], [1,4]]))
print(s.graphHasCircle(7, [[23,92], [23,68], [92,68], [92,68],[36,4],[68,17],[6,17]]))