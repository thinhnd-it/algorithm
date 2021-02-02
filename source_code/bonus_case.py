# bonus case
def backtracking(i, sum):
    if sum > k:
        return 0
    if i == n:
        return sum
    pick = backtracking(i+1, sum + set[i])
    leave = backtracking(i+1, sum)
    return max(pick, leave)


if __name__ == '__main__':
    set = [300, 34, 4, 12, 47, 2]
    k = 100
    n = len(set)
    print(backtracking(i=0, sum=0))
