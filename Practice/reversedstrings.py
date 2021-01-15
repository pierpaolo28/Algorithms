# Are two strings the reverse of each other? "ABC", "CBA"

s1 = 'ABC'
s2 = 'CBA'
# s1 = 'ABCW'
# s2 = 'QCBA'


def reversed(s1, s2):
    a = ''.join(sorted(s1))
    b = ''.join(sorted(s2))
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def reversed2(s1, s2):
    for i in range(len(s1)):
        if s1[i] != s2[len(s2) - i - 1]:
            return False
    return True


print(reversed(s1, s2))
print(reversed2(s1, s2))