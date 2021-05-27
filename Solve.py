class Solution:
    # @param A : list of integers
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        trie = Trie()
        result = []
        for i in range(len(A)):
            if A[i] == 0:
                trie.insert(B[i])
            if A[i] == 1:
                result.append(trie.get_frequency(B[i]))
        return result


class TrieNode:
    
    def __init__(self):
        self.frequency = 0
        self.children = {}
        # self.value = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
            current.frequency += 1
        current.isWord = True
    
    def search(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.isWord
    
    def get_frequency(self, prefix):
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.frequency
    
    def starts_with(self, prefix):
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True
