class Solution:
    # @param A : string
    # @return an integer
    def seats(self, A):
        positions = []
        for i, c in enumerate(A):
            if c == "x": positions.append(i)
        size = len(positions)
        mid = size // 2
        left = mid - 1
        right = mid + 1
        k = 1
        res = 0
        while left >= 0:
            res += positions[mid] - positions[left] - k
            left -= 1
            k += 1
        k = 1
        while right < size:
            res += positions[right] - positions[mid] - k
            right += 1
            k += 1
        return res
