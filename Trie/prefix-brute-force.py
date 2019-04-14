import collections
class WordFilter:

    def __init__(self, words):
        self.map=collections.defaultdict(set)
        for i in range(len(words)):
            word=words[i]
            for x in range(len(word)+1):
                prefix=word[:x]
                self.map[prefix].add(word)

    def f(self, prefix) -> int:
        #print(self.map)
        return self.map.get(prefix,-1)


# Your WordFilter object will be instantiated and called as such:
words=["apple","defer","ape","ape","afee"]
obj = WordFilter(words)
print(obj.f("ap"))