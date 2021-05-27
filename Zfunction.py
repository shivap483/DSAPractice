def z_func(A):
    n = len(A)
    z = [0 for i in range(n)]
    l = 0
    r = 0
    for i in range(1, n):
        if i > r:
            l = r = i
            while r < n and A[r - l] == A[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            if z[i - l] < r - i + 1:
                z[i] = z[i - l]
            else:
                l = i
                while r < n and A[r - l] == A[r]:
                    r += 1
                z[i] = r - l
                r -= 1
    return z
