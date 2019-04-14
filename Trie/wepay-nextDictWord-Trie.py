# Trie树实现字符串数组字典排序
# O(n)

class Node(object):
    def __init__(self, c=None, word=None):
        self.c = c    # 节点存储的单个字符
        self.word = word # 节点存储的词
        self.childs = []   # 此节点的子节点

class Trie(object):
    def __init__(self):
        self.root  = Node()

    def setWords(self, words):
        for word in words:
            self.add(word)

    def find(self, node, c):
        '''查找字符插入的位置'''
        childs = node.childs
        length = len(childs)
        if length == 0:
            return -1
        for i in range(length):
            if childs[i].c == c:
                return i
        return -1

    def add(self, word):
        '''添加字符串'''
        node = self.root
        for c in word:
            pos = self.find(node, c)
            if pos < 0:
                node.childs.append(Node(c))
                """
                为了图简单，这里直接使用Python内置的sorted来排序
                pos有问题，因为sort之后的pos会变掉,所以需要再次find来获取真实的pos
                自定义单字符数组的排序方式可以实现任意规则的字符串数组的排序
                """
                node.childs = sorted(node.childs, key=lambda child: child.c)
                pos = self.find(node, c)
            node = node.childs[pos]
        node.word = word

    def preOrder(self, node):
        '''先序输出'''
        results = []
        if node.word:
            results.append(node.word)
        for child in node.childs:
            results.extend(self.preOrder(child))
        return results



if __name__ == '__main__':
    words = ['python', 'function', 'php', 'food', 'kiss', 'perl', 'goal', 'go', 'golang', 'easy']
    trie = Trie()
    trie.setWords(words)
    result = trie.preOrder(trie.root)
    print('原始字符串数组:     %s' % words)
    print('Trie树排序后:       %s' % result)
    print('Python的sort排序后: %s' % sorted(words))