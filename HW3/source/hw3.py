"""
CSE 321 Homework #3 Algorithm Implementations.
author: Ahmed Semih Ozmekik
Driver functions defined below for all implementations.
"""

import random  # for pivot selection


def find_sum(A):
    return (max(A) + min(A)) * (len(A) / 4)


def find_mult(A):
    mult = 1
    for el in A:
        mult *= el
    return mult


def find_optimal_sub(lst, index, sub_lst, opt_sub):
    if index == len(lst):
        if len(sub_lst) != 0:
            if sum(sub_lst) >= find_sum(lst):
                if len(opt_sub) == 0 or find_mult(sub_lst) < find_mult(opt_sub):
                    opt_sub = sub_lst
    else:
        opt_sub = find_optimal_sub(lst, index + 1, sub_lst, opt_sub)
        opt_sub = find_optimal_sub(lst, index + 1, sub_lst + [lst[index]], opt_sub)
    return opt_sub


def arrange_box(lst, first_idx, last_idx):
    """
    :param lst = ["black", "black", ..., "white", "white", ...]
    2n <- len(lst), lst including n black boxes, n white boxes.
    """
    if first_idx >= last_idx:
        return

    swap(lst, first_idx, last_idx)  # swap first and last item of given list/sub-list
    arrange_box(lst, first_idx + 2, last_idx - 2)


# Correspond to one move in box arrangement.
# Swaps items in given indices.
def swap(lst, idx1, idx2):
    temp = lst[idx1]
    lst[idx1] = lst[idx2]
    lst[idx2] = temp


def different(A, B, C):
    if type(A) == list:
        if sum(A) == sum(B):
            return C
        elif sum(A) == sum(C):
            return B
        else:
            return A
    else:
        if A == B:
            return C
        elif A == C:
            return B
        else:
            return A


# Implementation didn't specified as required for this hw.
# Nonetheless, for to test whether the algorithm is working properly
# I have implemented the algorithm given in report.
# In this implementation; when it finds the coin it just shows that it's found.
# It's not given any indexes or etc. for the sake of user.
def find_fake_coin(lst):
    if len(lst) == 3:
        return different(lst[0], lst[1], lst[2])
    A = lst[0: len(lst) // 3]
    B = lst[len(lst) // 3:(2 * len(lst)) // 3]
    C = lst[(2 * len(lst)) // 3:len(lst)]
    return find_fake_coin(different(A, B, C))


def find_median(lst):
    if len(lst) % 2 == 1:  # odd number of items
        return quick_select(lst, len(lst) / 2)
    else:
        return (quick_select(lst, len(lst) / 2 - 1) + quick_select(lst, len(lst) / 2)) / 2


def quick_select(lst, k):
    if len(lst) == 1:
        return lst[0]

    pivot = random.choice(lst)  # picks a pivot among the items
    smallers = [item for item in lst if item < pivot]
    highers = [item for item in lst if item > pivot]
    pivots = [item for item in lst if item == pivot]

    if k < len(smallers):
        return quick_select(smallers, k)
    elif k < len(smallers) + len(pivots):
        return pivots[0]
    else:
        return quick_select(highers, k - len(smallers) - len(pivots))


def insertion_sort(lst):
    for i in range(1, len(lst)):
        item = lst[i]
        sorted_idx = i - 1
        while sorted_idx >= 0 and lst[sorted_idx] > item:
            lst[sorted_idx + 1] = lst[sorted_idx]  # swap operation performed
            sorted_idx -= 1
        lst[sorted_idx + 1] = item


def quick_sort(lst, low_idx, high_idx):
    if low_idx < high_idx:
        partition_idx = partition(lst, low_idx, high_idx)
        quick_sort(lst, low_idx, partition_idx - 1)
        quick_sort(lst, partition_idx + 1, high_idx)


def partition(lst, low_idx, high_idx):
    smaller_idx = low_idx - 1
    pivot = lst[high_idx]
    for j in range(low_idx, high_idx):
        if lst[j] < pivot:
            smaller_idx = smaller_idx + 1
            swap(lst, smaller_idx, j)
    swap(lst, smaller_idx + 1, high_idx)
    return smaller_idx + 1


def driver_arrange_box():
    black_box = ["black" for i in range(5)]
    white_box = ["white" for i in range(5)]
    box = black_box + white_box
    print("Not arranged", box)
    arrange_box(box, 0, 9)
    print("Rearranged", box)


def driver_find_fake_coin():
    coins = [0, 0, 1, 0, 0, 0, 0, 0, ]  # len = 3^2 = 9 (satisfies 3^m)
    print("Coins: ", coins)
    print("coin is fake: ", find_fake_coin(coins))


def driver_find_median():
    lst = [2.7, 3.5, 5.1, 8.3]
    print("Searching median in list: ", lst)
    print("Median: ", find_median(lst))


def driver_insertion_sort():
    lst = [random.randint(i, i + 10) for i in range(10)]
    print("Unsorted list: ", lst)
    insertion_sort(lst)
    print("Sorted list (via Insertion Sort): ", lst)


def driver_quick_sort():
    lst = [random.randint(i, i + 10) for i in range(10)]
    print("Unsorted list: ", lst)
    quick_sort(lst, 0, len(lst) - 1)
    print("Sorted list (via Quick Sort): ", lst)


driver_arrange_box()
driver_find_fake_coin()
driver_find_median()
driver_insertion_sort()
driver_quick_sort()
