def finalPrice(prices):
    l = []
    res = 0
    no_disc = []
    for ind, i in enumerate(prices):
        if(l):
            if i > l[-1]:
                l.append(i)
                no_disc.append(ind)
            else:
                while(l and i <= l[-1]):
                    res += l[-1] -i
                    l.pop(-1)
                    no_disc.pop(-1)
                l.append(i)
                no_disc.append(ind)
        else:
            l.append(i)
            no_disc.append(ind)
    print(res + sum(l))
    print(*no_disc)