
def ksdp(td, wt, val, n, w):

    try:
        for i in range(n):
            for j in range(w):
                if wt[i-1] <= j:
                    td[i][j] = max(
                        val[i-1] + td[i-1][j-wt[i-1]],
                        td[i - 1][j]
                    )
                elif wt[i-1] > j:
                    td[i][j] = td[i - 1][j]
    except:
        print("except: ", n,w)
    for i in range(n):
        print(td[i])
    # return td[n][w]



val = [ 20, 5, 10, 40, 15, 25 ]
wt = [ 1, 2, 3, 8, 7, 4 ]
w = 10

# w = 50
# val = [60, 100, 120]
# wt = [10, 20, 30]

n, w = len(val) + 1, w + 1
dp = [[0 for i in range(w)] for j in range(n)]

for k in range(n):
    for l in range(w):
        if k == 0 or l ==0:
            dp[k][l] = 0

for i in range(n):
    print(dp[i])
# print(n,w)
print(ksdp(dp, wt, val, n, w))


# not accurate solutions