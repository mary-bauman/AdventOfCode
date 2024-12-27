from time import time
start = time()
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def how_many_combos(self, string):
        combos = set()
        n = len(string)
        def dfs(index):
            print(f"index = {index}, combos = {combos}")
            if index==n: return 1
            node = self.root
            

        return dfs(0)
    

trie = Trie()
towels = input().split(", ")
for towel in towels: trie.insert(towel)
input()
numLines = 402
numLines = 10
total = 0
for i in range(numLines-2):
    total += trie.how_many_combos(input())

print(total)
print("time:", round(time()-start, 6))