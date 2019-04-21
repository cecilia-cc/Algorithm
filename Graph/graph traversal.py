import collections

class Graph:
    # 有向图
    def __init__(self):
        self.graph = collections.defaultdict(list)
        self.visited = collections.defaultdict(bool)
        self.nodes = set()

    def add_nodes(self,node_list):
        for node in node_list:
            self.graph[node] = []
            self.visited[node] = False
            self.nodes.add(node)

    def add_edge(self,edge):
        u,v = edge
        if v not in self.graph[u]:
            self.graph[u].append(v)

    def DFS(self,root):
        order=[]
        def dfs(node):
            self.visited[node] = True
            order.append(node)
            for n in self.graph[node]:
                if not self.visited[n]:
                    dfs(n)
        if root:
            dfs(root)
        # 未联通的节点
        for node in self.nodes:
            if not self.visited[node]:
                dfs(node)
        return order


    def BFS(self,root):
        order = []
        q = collections.deque()

        def bfs():
            while q:
                cur = q.popleft()
                self.visited[cur] = True
                for n in self.graph[cur]:
                    if (not self.visited[n]) and (not n in q):
                        q.append(n)
                        order.append(n)
        if root:
            q.append(root)
            order.append(root)
            bfs()

        # 未联通的节点
        for node in self.nodes:
            if not self.visited[node]:
                q.append(node)
                order.append(node)
                bfs()
        return order

    def circle_path(self,):
        stack = []
        path = []

        def dfs_circle(node,stack):
            self.visited[node] = True
            stack.append(node)
            if node in self.graph:
                for n in self.graph[node]:
                    if n not in stack:
                        if not self.visited[n]:
                            dfs_circle(n,stack)
                    else:
                        index = stack.index(n)
                        temp = []
                        for i in stack[index:]:
                            temp.append(i)
                        temp.append(n)
                        path.append(temp)
            stack.pop(-1)

        for node in self.nodes:
            if not self.visited[node]:
                dfs_circle(node, stack)
        return path

if __name__ == '__main__':
    g = Graph()
    g.add_nodes(['a','b','c','d','e','t','f'])
    g.add_edge(('a', 'b'))
    g.add_edge(('a', 'c'))
    g.add_edge(('b', 'e'))
    g.add_edge(('e', 'b'))
    g.add_edge(('c', 'd'))
    g.add_edge(('d', 'a'))
    g.add_edge(('d', 'p'))
    g.add_edge(('t', 'f'))
    print("DFS:")
    #print(g.DFS('a'))
    print("BFS:")
    #print(g.BFS('a'))
    print("Circle:")
    print(g.circle_path())
