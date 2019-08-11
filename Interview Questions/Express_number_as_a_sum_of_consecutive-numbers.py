# How many ways there are to express a natural number N as a sum of two or more consecutive
# natural numbers?
# eg. 10 = 1+2+3+4
# eg. 100 = 9+10+11+12+13+14+15+16
#     100 = 18+19+20+21+22

# In order to solve this problem we need to consider consecutive series.
# a = first number in the consecutive series
# n = number of numbers in the consecutive series

# Sum of an aritmethic progression = (first number + last number)*n/2
#                                N = (a +a +n -1)*n/2
# Let's start first by finding a, a = (2N + n - n**2)/2n

def solution(N):
    count = 0 # count of the number of n solutions
    n = 2 # our arithmetic series has to be composed by at least 2 numbers

    while 2*N + n - n**2 > 0:
        a = (2*N + n -n**2) / (2*n)
        if a - int(a) == 0:
            print(a, n)
            count += 1
        n+=1

    return count

nat_num = 20
print("There are n number of possible ways to reach", nat_num, ": ", solution(nat_num))
nat_num = 100
print("There are n number of possible ways to reach", nat_num, ": ", solution(nat_num))
nat_num = 900
print("There are n number of possible ways to reach", nat_num, ": ", solution(nat_num))