# Task 1: print list of elements in tabular format

def splitting(A, K):
    for i in range(0, len(A), K):
        yield A[i:i+K]

def solution(A, K):
    # write your code in Python 3.6
    spacenum = len(str(max(A)))
    res = list(splitting(A, K))
    p = '-'*(spacenum) + '+'
    print('+' + p*len(res[0]))
    for j in res:
        r = ''.join([' '*(spacenum -len(str(i))) + str(i) + '|' for i in j])
        h =  r.replace(" |", "")
        print('|' + h)
        print('+' + p*len(j))

# Task 2: Return number of soldiers who can report to some superior (n+1)

def solution(ranks):
    # write your code in Python 3.6
    report = 0
    for j in range(len(ranks)):
        count = 0
        for h, i in enumerate(ranks):
            if ranks[j] == i - 1:
                report += 1
                if count == 0 or h == i:
                    report -= 1
                count += 1
    if report != 0:
        report += 1

    return report

# Task 3: Return starting index of the maximum sequence of ascending elements in an array

def solution(A):
    # write your code in Python 3.6
    maxn = 0
    dicts = {}
    for i in range(len(A) - 1):
        if A[i] < A[i + 1]:
            maxn += 1
        else:
            dicts[i - maxn] = maxn
            maxn = 0

    return max(dicts, key=dicts.get)