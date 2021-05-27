class LPS:
    def lps(self, str):
        n = len(str)
        i = 0
        lps = [0 for _ in range(n)]
        j = 1
        while j < n:
            if str[i] == str[j]:
                i += 1
                lps[j] = i
                j += 1
            else:
                if i != 0:
                    i = lps[i - 1]
                else:
                    lps[j] = 0
                    j += 1
        return lps
