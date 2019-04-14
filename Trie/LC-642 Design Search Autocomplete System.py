import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.sentence = set()

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.weight = collections.defaultdict(int)
        self.root = TrieNode()
        self.trie = self.root
        self.cache = ""
        for i in range(len(sentences)):
            self.weight[sentences[i]] = times[i]
            self.insert(sentences[i])

    def insert(self, s):
        cur = self.root
        for w in s:
            cur = cur.children[w]
            cur.sentence.add(s)

    def input(self, c):
        ans = []
        if c != '#':
            self.cache += c
            if self.trie:
                self.trie = self.trie.children.get(c)
            if self.trie:
                ans = sorted(self.trie.sentence, key=lambda x: (-self.weight[x], x))[:3]

        else:
            self.weight[self.cache] += 1
            self.insert(self.cache)
            self.cache = ""
            self.trie = self.root
        return ans

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)