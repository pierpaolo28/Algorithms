def kDifference(a, k):
    res = 0
    # Slow runtime solution
    # for i in range(len(a)):
    #     for j in range(i+1, len(a)):
    #         if (a[i] - a[j]) == k or (a[j] - a[i]) == k:
    #             res += 1
    # return res
    a.sort()
    right = 0
    left = 0
    while right < len(a):
        if a[right] - a[left] == k:
            res += 1
            left += 1
            right += 1
        elif a[right] - a[left] > k:
            left += 1
        elif a[right] - a[left] < k:
            right += 1
    return res