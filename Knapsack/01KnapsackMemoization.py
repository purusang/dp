
def ks2(wt, val, w, n):
    if n == 0 or w == 0:
        return 0
    global dp
    try:
        if dp[n][w] != -1:
            return dp[n][w]
    except:
        print("ex: ", n,w)
    if wt[n-1] <= w:
        dp[n][w] = max(
            val[n-1] + ks2(wt, val, w-wt[n-1], n-1 ),
            ks2(wt, val, w, n - 1)
        )
    elif wt[n-1] > w:
        dp[n][w] = ks2(wt, val, w, n - 1)

    return dp[n][w]


# val = [ 20, 5, 10, 40, 15, 25 ]
# wt = [ 1, 2, 3, 8, 7, 4 ]
# w = 10

w = 50
val = [60, 100, 120]
wt = [10, 20, 30]
n, w = len(val), w
dp = [[-1 for _ in range(w+1)] for _ in range(n+1)]
# print(dp)

print(ks2(wt, val, w, n))

print(dp)