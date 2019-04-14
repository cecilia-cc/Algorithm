import collections
import sys


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.weights = set()

class WordFilter(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, w):
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
        for w in curr.weights:
            wordsWithPrefix.add(w)
        return wordsWithPrefix


obj = WordFilter()
words=["apple","defer","ape","ape","afee"]
for word in words:
    obj.insert(word)
print(obj.find("ap"))




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