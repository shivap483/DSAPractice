import time
start=time.time()
def solve(N,K):
    count=0
    map= [None]*int(N)
    for num in range(int(N)):
        map,sum=sum_of_digits(map,num)
        if sum%K==0:
            count+=1
    print(map)
    return count
def sum_of_digits(map,num):
    sum=0
    temp=num
    while(num!=0):
        if map[num]:
            sum+=map[num]
            map[temp] = sum
            return map,sum
        else:
            sum+=num%10
            num=num//10
    map[temp] = sum
    return map,sum

def ranges(n):
    sum=0
    list=[]
    count=0
    for i in range(n):
        if count>=n:
            break
        x=i
        for _ in range(10) :
            if count >= n:
                break
            list.append(x+_)
            count+=1
    print(list)

# print(solve("10000",2))
# print(time.time()-start)

print(ranges(100000))
print(time.time()-start)