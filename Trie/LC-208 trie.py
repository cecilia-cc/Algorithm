import collections
class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isWord = False


class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root
        for w in word:
            cur = cur.children[w]
        cur.isWord = True

    def search(self, word):
        cur = self.root
        for w in word:
            cur = cur.children.get(w)
            if cur == None:
                return False
        return cur.isWord

    def startsWith(self, prefix):
        cur = self.root
        for w in prefix:
            cur = cur.children.get(w)
            if cur == None:
                return False
        return True

    def delete(self, word):
        node = self.root
        queue = []
        for letter in word:
            queue.append((letter, node))
            child = node.children.get(letter)
            if child is None:
                return False
            node = child
        if not node.isWord:
            return False
        if len(node.children):
            node.isWord = False
        else:
            for letter, node in reversed(queue):
                del node.children[letter]
                if len(node.children) or node.isWord:
                    break
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
obj.insert("app")
obj.insert("liuly")
print(obj.search("app"))
print(obj.search("a"))
print(obj.startsWith("ap"))
obj.delete("app")
print(obj.search("app"))
