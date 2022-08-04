def ksdp(td, wt, val, n, w):
    try:
        for i in range(1, n + 1):
            for j in range(1, w + 1):
                if wt[i-1] <= j:
                    td[i][j] = max(
                        val[i-1] + td[i-1][j-wt[i-1]],
                        td[i - 1][j]
                    )
                elif wt[i-1] > j:
                    td[i][j] = td[i - 1][j]
    except:
        print("except: ", n,w)
    for i in range(n+1):
        print(td[i])
    return td[n][w]


val = [ 20, 5, 10, 40, 15, 25 ]
wt = [ 1, 2, 3, 8, 7, 4 ]
w = 10

w = 50
val = [60, 100, 120]
wt = [10, 20, 30]

n, w = len(val), w
dp = [[0 for i in range(w+1)] for j in range(n+1)]

print(n,w)
print(ksdp(dp, wt, val, n, w))
