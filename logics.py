##########n=int(input())
##########a=list(map(int,input().split()))
##########s=sorted(a)
##########print(s[-3])
########
########for i in range(2):
########    a = a.remove(max(a))
########print(max(a))
########print(a)
########
######a=int(input())
######b=list(map(int,input().split()))
######i=a.index(max(a))
######a[:i+1]==sorted(a[:i+1]) and a[i: ]==sorted(a[i:] , reverse = True):
######    print(True)
######else:
######    print(False)
######    
####
####n=int(input())
####a=list(map(int,input().split()))
####o=[]
####e=[]
####for i in a:
####    if i%2==0:
####        e.append(i)
####    else:
####        o.append(i)
####for i in range(n//2):
####    print(o[i],e[i])
######if len(o)>len(e):
######    print(o)
######else:
######    print(e)
##
##
##
####import math
####
####def is_prime(x):
####    if x < 2:
####        return False
####    for i in range(2, int(math.sqrt(x))+1):
####        if x % i == 0:
####            return False
####    return True
####
####def distinct_primes(n):
####    max_distinct = 0
####    for i in range(1, n+1):
####        count = 0
####        for j in range(2, i+1):
####            if i % j == 0 and is_prime(j):
####                count += 1
####        max_distinct = max(max_distinct, count)
####    return max_distinct
####
####q = int(input())
####for i in range(q):
####    n = int(input())
####    print(distinct_primes(n))
##from queue import Queue
##
##def is_prime(n):
##    if n < 2:
##        return False
##    for i in range(2, int(n ** 0.5) + 1):
##        if n % i == 0:
##            return False
##    return True
######
######def find_shortest_path(Num1, Num2):
######    queue = Queue()
######    queue.put((Num1, 0))
######    visited = set([Num1])
######    while not queue.empty():
######        num, dist = queue.get()
######        if num == Num2:
######            return dist
######        for i in range(4):
######            for j in range(10):
######                if j == 0 and i == 0:
######                    continue
######                new_num = int(str(num)[:i] + str(j) + str(num)[i+1:])
######                if is_prime(new_num) and new_num not in visited:
######                    visited.add(new_num)
######                    queue.put((new_num, dist + 1))
######    return -1
######
######if __name__ == '__main__':
######    Num1 = int(input().strip())
######    Num2 = int(input().strip())
######    print(find_shortest_path(Num1, Num2))
##
##
##
##def numRollsToTarget(n, k, target):
##    memo = {}
##    def dp(i, t):
##        if i == 0 and t == 0:
##            return 1
##        if i == 0 or t < 0:
##            return 0
##        if (i, t) in memo:
##            return memo[(i, t)]
##        res = 0
##        for j in range(1, k+1):
##            res += dp(i-1, t-j)
##        memo[(i, t)] = res
##        return memo[(i, t)]
##    return dp(n, target)
##
### Testing the function with sample inputs
##print(numRollsToTarget(1, 6, 3))  # Output: 1
##print(numRollsToTarget(2, 6, 7))  # Output: 6
##print(numRollsToTarget(30, 30, 500))  # Output: 222616187



def numRollsToTarget(n, k, target):
    MOD = 10**9 + 7
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for t in range(j, target + 1):
                dp[i][t] = (dp[i][t] + dp[i-1][t-j]) % MOD
    return dp[n][target]

# Taking input from user
n, k, target = map(int, input().split())

# Calling the function with user input
result = numRollsToTarget(n, k, target)

# Displaying the result
print(result)
