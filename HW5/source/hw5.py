def optimal_cost(n, M, ny, sf):
    min_cost = [[0] * n, [0] * n]
    min_cost[0][0] = ny[0]
    min_cost[1][0] = sf[0]

    for i in range(1, n):
        min_cost[0][i] = min(min_cost[0][i - 1] + ny[i], min_cost[1][i - 1] + sf[i] + M)
        min_cost[1][i] = min(min_cost[0][i - 1] + ny[i] + M, min_cost[1][i - 1] + sf[i])

    return min(min_cost[0][n - 1], min_cost[1][n - 1])


def optimal_list_schedule(S):
    S = sorted(S, key=lambda x: x[1], reverse=False)
    optimal = []
    joined = -1
    for s in S:
        if joined == -1 or optimal[joined][1] <= s[0]:
            optimal.append(s)
            joined += 1
    return optimal


def align_score(A, B):
    # scores are hardcoded, could be changed.
    match, miss, gap = 2, -2, -1

    n = len(A) + 1
    m = len(B) + 1
    F = ([[0 for i in range(n)] for i in range(m)])

    for i in range(m):
        F[i][0] = gap * i
    for i in range(n):
        F[0][i] = gap * i

    for i in range(1, m):
        for j in range(1, n):
            score = miss
            if B[i - 1] == A[j - 1]:
                score = match
            no_gap_score = F[i - 1][j - 1] + score
            F[i][j] = max(no_gap_score, F[i - 1][j] + gap, F[i][j - 1] + gap)
    return max(*[F[i][n - 1] for i in range(m)], *[F[m - 1][i] for i in range(n)])


def ancient_sum(arr):
    op = 0
    n = len(arr)
    while n > 1:
        for i in range(0, n, 2):
            arr[i] += arr[i + 1]
            op += arr[i]
        arr = [arr[i] for i in range(n) if i % 2 == 0]
        n = len(arr)
    print(op, "number of operation.")
    return arr[0]


def driver_optimal_cost():
    ny = [1, 3, 20, 30]
    sf = [50, 20, 2, 4]
    m = 10
    n = 4
    print(optimal_cost(n, m, ny, sf))


def driver_align_score():
    seq1 = 'alignment'
    seq2 = 'slime'
    print(align_score(seq1, seq2))


def driver_ancient_sum():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(ancient_sum(arr))


def driver_optimal_list_schedule():
    schedule = [[1, 3], [11, 1], [12, 3], [12, 2], [1, 4]]
    print(schedule)
    print(optimal_list_schedule(schedule))


def drivers():
    driver_align_score()
    driver_optimal_cost()
    driver_optimal_list_schedule()
    driver_ancient_sum()


drivers()