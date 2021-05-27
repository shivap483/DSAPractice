class Trie:
    def __init__(self):
        self.root_node = {}
    
    def add_word(self, word):
        current_node = self.root_node
        is_new_word = False
        
        for char in word:
            if char not in current_node:
                is_new_word = True
                current_node[char] = {}
            current_node = current_node[char]
        
        if "End of word" not in current_node:
            is_new_word = True
            current_node["End of word"] = {}
        
        return is_new_word
    
    def search_word(self, word):
        current_node = self.root_node
        for char in word:
            if char in current_node:
                current_node = current_node[char]
            else:
                return False
        if "End of word" in current_node:
            return True
        return False
