# Input is a string but represents a number, compare the two number and return True is the first one is larger than the second one.

s1, s2 = "3456", "123"
s1, s2 = "34", "147"
s1, s2 = "232", "233"


def largerthan(s1, s2):
    if int(s1) > int(s2):
        return True
    else:
        return False


def largerthan2(s1, s2):
    if len(s1) > len(s2):
        return True
    elif len(s1) == len(s2):
        for i, j in zip(s1, s2):
            if i > j:
                return True
        return False
    else:
        return False


print(largerthan(s1, s2))
print(largerthan2(s1, s2))