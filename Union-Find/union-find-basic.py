class QuickFind(object):
    id = []
    count = 0

    def __init__(self, n):
        self.count = n
        i = 0
        while i < n:
            self.id.append(i)
            i += 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        return self.id[p]

    def union(self, p, q):
        idp = self.find(p)
        if not self.connected(p, q):
            for i in range(len(self.id)):
                if self.id[i] == idp:  # 将p所在组内的所有节点的id都设为q的当前id
                    self.id[i] = self.id[q]
            self.count -= 1


qf = QuickFind(10)

print("initial id list is %s" % (",").join(str(x) for x in qf.id))

list = [(4, 3),(3, 8),(6, 5),(9, 4),(2, 1),(8, 9),
    (5, 0),(7, 2),(6, 1),(1, 0),(6, 7)]

for k in list:
    p = k[0]
    q = k[1]
    qf.union(p, q)
    print("%d and %d is connected? %s" % (p, q, str(qf.connected(p, q))))

print("final id list is %s" % (",").join(str(x) for x in qf.id))
print("count of components is: %d" % qf.count)



########################
class QuickUnion(object):
    # tree
    id = []
    count = 0

    def __init__(self, n):
        self.count = n
        i = 0
        while i < n:
            self.id.append(i)
            i += 1

    def connected(self, p, q):
        if self.find(p) == self.find(q):
            return True
        else:
            return False

    def find(self, p):
        while (p != self.id[p]):
            p = self.id[p]
        return p

    def union(self, p, q):
        idq = self.find(q)
        idp = self.find(p)
        if not self.connected(p, q):
            self.id[idp] = idq
            self.count -= 1

qf = QuickUnion(10)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("initial id list is %s" % (",").join(str(x) for x in qf.id))

list = [(4, 3),(3, 8),(6, 5),(9, 4),(2, 1),(8, 9),
    (5, 0),(7, 2),(6, 1),(1, 0),(6, 7)]

for k in list:
    p = k[0]
    q = k[1]
    qf.union(p, q)
    print("%d and %d is connected? %s" % (p, q, str(qf.connected(p, q))))

print("final id list is %s" % (",").join(str(x) for x in qf.id))
print("count of components is: %d" % qf.count)



##################################################

class WeightedQuickUnion(object):
    id = []
    count = 0
    sz = []

    def __init__(self, n):
        self.count = n
        i = 0
        while i < n:
            self.id.append(i)
            self.sz.append(1)  # inital size of each tree is 1
            i += 1

    def connected(self, p, q):
        if self.find(p) == self.find(q):
            return True
        else:
            return False

    def find(self, p):
        while (p != self.id[p]):
            p = self.id[p]
        return p

    def union(self, p, q):
        idp = self.find(p)
        idq = self.find(q)
        if not self.connected(p, q):
            if (self.sz[idp] < self.sz[idq]):
                self.id[idp] = idq
                self.sz[idq] += self.sz[idp]
            else:
                self.id[idq] = idp
                self.sz[idp] += self.sz[idq]
            self.count -= 1

qf = WeightedQuickUnion(10)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("initial id list is %s" % (",").join(str(x) for x in qf.id))

list = [(4, 3),(3, 8),(6, 5),(9, 4),(2, 1),(8, 9),
    (5, 0),(7, 2),(6, 1),(1, 0),(6, 7)]

for k in list:
    p = k[0]
    q = k[1]
    qf.union(p, q)
    print("%d and %d is connected? %s" % (p, q, str(qf.connected(p, q))))

print("final id list is %s" % (",").join(str(x) for x in qf.id))
print("count of components is: %d" % qf.count)

