class SegmentTree:

    def __init__(self, list):
        self.tree = [0 for _ in range(3 * len(list))]
        self.list = list
        self.buildTree(0, 0, len(list) - 1)

    def buildTree(self, index, start, end):
        if start == end:
            self.tree[index] = self.list[start]
        else:
            lc = 2 * index + 1
            rc = 2 * index + 2
            mid = start + (end - start) // 2
            self.buildTree(lc, start, mid)
            self.buildTree(rc, mid + 1, end)
            self.tree[index] = self.tree[lc] + self.tree[rc]

    def update(self, type, id, index, start, end):
        if id < start or id > end:
            return
        if start == end:
            if type == 1:
                self.tree[index] += 1
            elif type == 2:
                self.tree[index] = max(self.tree[index] - 1, 0)
            return
        lc = 2 * index + 1
        rc = 2 * index + 2
        mid = start + (end - start) // 2
        self.update(type, id, lc, start, mid)
        self.update(type, id, rc, mid + 1, end)
        self.tree[index] = self.tree[lc] + self.tree[rc]

    def query(self, l, r, index, start, end):
        if l <= start and end <= r:
            return self.tree[index]
        if r < start or end < l:
            return 0
        lc = 2 * index + 1
        rc = 2 * index + 2
        mid = start + (end - start) // 2
        return self.query(l, r, lc, start, mid) + self.query(l, r, rc, mid + 1, end)


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        list = [0 for _ in range(A)]
        ans = []
        segment_tree = SegmentTree(list)
        index = start = 0
        end = A - 1
        for query in B:
            if query[0] == 1 or query[0] == 2:
                segment_tree.update(query[0], query[1] - 1, index, start, end)
            else:
                ans.append(segment_tree.query(query[1] - 1, query[2] - 1, index, start, end))
        return ans
