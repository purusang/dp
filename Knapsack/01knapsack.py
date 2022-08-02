import  math
max_val = -math.inf

def knapsack(arr, sack, capacity, weight_key):
    # base conditions
    if sack['wt'] + weight_key > capacity:
        return sack['val']
    if len(arr)==0:
        return sack['val'] + arr[weight_key]

    # add element to sack
    sack['wt'] += weight_key
    sack['val'] += arr[weight_key]

    # remove item from array
    # temp = arr[weight_key]
    arr.pop(weight_key)

    # now recursively call knapsack for each remaining child
    global max_val
    for item in list(arr):
        # print(item , val)
        val = knapsack(arr, sack, capacity, item)
        if val > max_val:
            max_val = val

    # backtracking: reinserting the popped element for going upward in the tree.
    # arr[weight_key] = temp
    # if reached deadend => means len(arr) > 0 but none child be adjusted
    # in this case we simply return the value of sack
    return sack['val']


def ks1(arr, sack, c, w):
    temp = None
    if w is not None:
        if sack['wt'] + w > c:
            return sack['val']
        if len(arr)==0:
            return sack['val'] + arr[w]
        sack['wt'] += w
        sack['val'] += arr[w]

        temp = arr[w]

        arr.pop(w)
    global max_val
    print(list(arr))
    for wt in list(arr):
        val = ks1(arr, sack, c, wt)
        print(val)
        if val > max_val:
            max_val = val
        if temp is not None:
            arr[w] = temp
    return max_val

# sack = {'wt':0, 'val':0 }
#
# # weight_value = {1: 1, 3: 4, 4: 5, 5:7}
# # sack_capacity = 7
#
# # weight_value = {
# #     95:55, 4:10, 60:47, 32:5, 23:4, 72:50, 80:8, 62:61, 65:85, 46:87
# # }
# # sack_capacity = 269
#
# weight_value = {
#     4:1, 5:2, 1:3
# }
# sack_capacity = 4
# # for item in list(weight_value):
# #     val = ks1(weight_value, sack, sack_capacity, item)
# #     if val > max_val:
# #         max_val = val
# print('\nOutput: ',ks1(weight_value, sack, sack_capacity, None))

def ks2(wt, val, w, n):
    if n == 0 or w == 0:
        return 0

    if wt[n] <= w:
        return max(
            val[n] + ks2(wt, val, w-wt[n], n-1 ),
            ks2(wt, val, w - wt[n], n - 1)
        )
    elif wt[n] >= w:
        return ks2(wt, val, w - wt[n], n - 1)


val = [60, 100, 120]
wt = [10, 20, 30]

print(ks2(wt, val, 50, len(val)-1))