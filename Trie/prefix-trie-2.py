import collections
import sys


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.weights = set()

class WordFilter(object):
    def __init__(self, words):
        self.words = words
        self.root = TrieNode()
        for word in words:
            self.add(word)

    def add(self, w):
        curr = self.root
        for c in w:
            curr = curr.children[c]
            curr.weights.add(w)

    def find(self, prefix):
        wordsWithPrefix = set()
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return -1
            curr = curr.children[c]
        if prefix:
            for w in curr.weights:
                wordsWithPrefix.add(w)
        else:
            wordsWithPrefix = set(self.words)
        return wordsWithPrefix


words=["apple","defer","ape","ape","afee"]
obj = WordFilter(words)
print(obj.find("ap"))
print(obj.find(""))



"""
# file input
f=open('/Users/cecilia/Desktop/test', 'r')
s=f.read()
print(s)
slist=s.split()
print(slist)
"""

"""
# keyboard input
input = sys.stdin.readline().strip("\n")
while input != "":
    print(obj.search(input))
    input = sys.stdin.readline().strip("\n")
"""