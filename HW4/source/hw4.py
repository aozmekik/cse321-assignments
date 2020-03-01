def largest_sub(lst, i, j):
    return (i, j - 1) if sum(lst[i:j - 1]) > sum(lst[i + 1: j]) else (i + 1, j)


def find_largest_cont_sub(lst, i, j):
    """Given an list, finds the contiguous subset having the
    largest sum within list."""
    if i == j:
        return lst

    k, l = largest_sub(lst, i, j)
    sub = find_largest_cont_sub(lst, k, l)
    return lst[i:j] if sum(lst[i:j]) > sum(sub) else sub


def best_goods_day(C, P, i, j):
    if i + 1 == j:
        return i

    # first half of arrays.
    m = (i + j) // 2
    day1 = best_goods_day(C, P, i, m)
    day2 = best_goods_day(C, P, m, j)
    return day1 if P[day1] - C[day1] > P[day2] - C[day2] else day2


def kth_element(A, B, m, n, k):
    if m > n:  # switch arrays to make m <= n
        return kth_element(B, A, n, m, k)
    if m == 0:
        return B[k - 1]
    if k == 1:
        return min(A[0], B[0])

    i = min(m, k // 2)
    j = min(n, k // 2)
    if A[i - 1] > B[j - 1]:
        return kth_element(A, B[j:], m, n - j, k - j)
    else:
        return kth_element(A[i:], B, m - i, n, k - i)


# G is adjacency list. n is len(G). color = [].
def bipartite(G, n, color):
    unvisited = False
    if not color:
        color = [-1] * len(G)
    if n < len(G):
        if color[n] == -1:
            unvisited = True
            for v in G[n]:
                if color[v] != -1:
                    unvisited = False
                    if color[n] == color[v]:
                        return False
                    else:
                        color[n] = 1 if color[v] == -1 else -1
        if unvisited:
            color[n] = -1
        return bipartite(G, n + 1, color)
    else:
        return True


def leftmost_min(lst, leftmost, row, column, k):
    if row == 1:
        leftmost[0] = lst[0].index(min(lst[0][0:column]))
    else:
        mid = int(ceil(row, 2.0))
        leftmost_min(lst, leftmost, mid, column, 2 * k)
        for i in range(1, row - 1, 2):
            idx = k * i
            end = leftmost[idx + k] + 1
            leftmost[idx] = lst[idx].index(min(lst[idx][leftmost[idx - k]:end]))
        if row % 2 == 0:
            idx = k * (row - 1)
            leftmost[idx] = lst[idx].index(min(lst[idx][leftmost[idx - k]:column]))


def ceil(a, b):
    if a % b == 0:
        return a / b
    else:
        return a // b + 1


def driver_find_largest_cont_sub():
    lst = [5, -6, 6, 7, -6, 7, -4, 3]
    sub = find_largest_cont_sub(lst, 0, 9)
    print(sub)


def driver_best_goods_day():
    C = [5, 11, 2, 21, 5, 7, 8, 12, 13]
    P = [7, 9, 5, 21, 7, 13, 10, 14, 20]
    print(best_goods_day(C, P, 0, 9))


def driver_kth_element():
    A = [5, 9, 14, 15, 16]
    B = [1, 2, 11, 20, 23, 24]
    print(A + B)
    el = kth_element(A, B, 5, 5, 5)
    print(el)


def driver_bipartite():
    G = [[1, 3], [1, 2], [1], [1, 2]]
    print(bipartite(G, 4, []))


def driver_leftmost_min():
    A = [[10, 17, 13, 28, 23],
         [17, 22, 16, 29, 23],
         [24, 28, 22, 34, 24],
         [11, 13, 6, 17, 7],
         [45, 44, 32, 37, 23],
         [36, 33, 19, 21, 6],
         [75, 66, 51, 53, 34]]
    rows = 7
    columns = 5
    mins = [0] * rows
    leftmost_min(A, mins, rows, columns, 1)
    print(mins)


def drivers():
    driver_leftmost_min()
    driver_bipartite()
    driver_kth_element()
    driver_best_goods_day()
    driver_find_largest_cont_sub()


drivers()
