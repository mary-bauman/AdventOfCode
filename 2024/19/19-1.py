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

    def can_form(self, string):
        memo = {}
        def dfs(index):
            # If we've reached the end of the string, return True
            if index == len(string): return True
            if index in memo: return memo[index]
            # Traverse the trie from the current index
            node = self.root
            for i in range(index, len(string)):
                char = string[i]
                if char not in node.children:
                    memo[index] = False
                    return False
                node = node.children[char]
                if node.is_end_of_word:  # Found a valid substring
                    # Continue to check if the remaining string can be formed
                    if dfs(i + 1):
                        memo[index] = True
                        return True
            memo[index] = False
            return False
        return dfs(0)
    

trie = Trie()
towels = input().split(", ")
for towel in towels: trie.insert(towel)
input()
numLines = 402
total = 0
for i in range(numLines-2): total += int(trie.can_form(input()))
print(total)
