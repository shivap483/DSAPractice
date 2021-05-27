def sum_of_digits(num):
    sum = 0
    while (num != 0):
        sum += num % 10
        num = num // 10
    return sum

def ranges(k):
    map={}
    for k in range(int(k)):
        for i in range(sum_of_digits(k)):
            if i in map:
                map[i]+=1
            else:
                map[i]=1
    return map

print(ranges(10000))
