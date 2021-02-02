import time
import random


# solve by backtracking

def isSubsetSum(set, n, sum):

    # Base Cases
    if (sum == 0):
        return True
    if (n == 0):
        return False

    # If last element is greater than
    # sum, then ignore it
    if (set[n - 1] > sum):
        return isSubsetSum(set, n - 1, sum)

    # else, check if sum can be obtained
    # by any of the following
    # (a) including the last element
    # (b) excluding the last element
    return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1])


# solve by Dynamic Programing

def isSubsetSum1(set, n, sum):

    # The value of subset[i][j] will be
    # true if there is a
    # subset of set[0..j-1] with sum equal to i
    subset = ([[False for i in range(sum + 1)]
               for i in range(n + 1)])

    # If sum is 0, then answer is true
    for i in range(n + 1):
        subset[i][0] = True

    # If sum is not 0 and set is empty,
    # then answer is false
    for i in range(1, sum + 1):
        subset[0][i] = False

    # Fill the subset table in botton up manner
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < set[i-1]:
                subset[i][j] = subset[i-1][j]
            if j >= set[i-1]:
                subset[i][j] = (subset[i-1][j] or
                                subset[i - 1][j-set[i-1]])

    # uncomment this code to return 2D DP matrix for traceback function
    # return subset
    return subset[n][sum]


def traceBack(DP, sum, n, set):
    m, b = n, sum
    subset = []
    while b > 0:
        if DP[m-1][b]:
            m -= 1
        else:
            m -= 1
            subset.append(set[m])
            b -= set[m]
    print(subset)

# uncomment if you want to try traceBack

# if __name__ == "__main__":
#     set = [300, 34, 4, 12, 47, 2]
#     n = 6
#     sum = 40
#     DP = isSubsetSum1(set, n, sum)
#     traceBack(DP, sum, n, set)


# backtracking bonus case

def backtracking(i, sums):
    if sums > sum:
        return 0
    if i == n:
        return sums
    pick = backtracking(i+1, sums + s[i])
    leave = backtracking(i+1, sums)
    return max(pick, leave)


# main for experiment

if __name__ == "__main__":
    print('n', end=',')
    print('tn')

    for n in range(20, 60):
        time1 = 0
        for x in range(1000):
            s = []
            for i in range(n):
                t = random.randint(1, 1000)
                s.append(t)
            sum = random.randint(1, 1000)
            st = time.time()
            backtracking(0, 0)
            e = time.time()
            time1 += (e-st)
        print(n, end=',')
        print(time1)
