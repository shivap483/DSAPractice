class Solution:

    class Trie:
        def __init__(self,):
            self.root={}

        def insert(self,node,cur_index,freq=1):
            current_node=self.root
            for i in range(32):
                bit=node and(1<<i)
                if bit not in current_node:
                    current_node[bit]={}
                current_node=current_node[bit]
            if current_node:
                prev_freq=current_node[1][0]
                prev_index=current_node[1][1]
                freq=prev_freq+1
                cur_index+= prev_index+1
            current_node[1]=[freq,cur_index]

        def is_present(self,node,cur_index):
            current_node = self.root
            for i in range(32):
                bit = node and (1 << i)
                if bit not in current_node:
                    return False
                current_node = current_node[bit]
            return True

    # @param A : list of integers
    # @return an integer
    def solve(self, A):
