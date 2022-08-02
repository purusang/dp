
def ks2(wt, val, w, n):
    if n < 0 or w == 0:
        return 0
    global dp
    try:
        if dp[n][w] != -1:
            return dp[n][w]
    except:
        print("ex: ", n,w)
    if wt[n] <= w:
        dp[n][w] = max(
            val[n] + ks2(wt, val, w-wt[n], n-1 ),
            ks2(wt, val, w, n - 1)
        )
    elif wt[n] >= w:
        dp[n][w] = ks2(wt, val, w, n - 1)

    return dp[n][w]


val = [ 20, 5, 10, 40, 15, 25 ]
wt = [ 1, 2, 3, 8, 7, 4 ]
w = 10

# w = 50
# val = [60, 100, 120]
# wt = [10, 20, 30]
r, c = len(val) +1  , w +1
dp = [[-1]*c]*r
# print(dp)
print(ks2(wt, val, w, len(val)-1))