
1 - ) An m × n array A of real numbers is called a **_special_** array if for all i, j , k, and l such that 1
≤ i < k ≤ m and 1 ≤ j < l ≤ n, we have:

```
A[i,j ] + A[k,l] ≤ A[i,l] + A[k,j ]
```
For example, the following array is a **_special_** array:

```
10 17 13 28 23
```
```
17 22 16 29 23
```
```
24 28 22 34 24
```
```
11 13 6 17 7
```
```
45 44 32 37 23
```
```
36 33 19 21 6
```
```
75 66 51 53 34
```
```
a) Prove that an array is special if and only if for all i = 1, 2, ..., m − 1 and j = 1, 2, ..., n − 1,
we have:
A[i,j ] + A[i + 1 ,j + 1 ] ≤ A[i,j + 1 ] + A[i + 1 ,j ]
b) Give an algorithm (not necessarily divide-and-conquer) that converts a 2D array into
the special array only if it can be done with changing one single element in the array.
Write pseudo code, implement and explain your algorithm.
c) Give a divide-and-conquer algorithm that finds the leftmost minimum element in each
row. Implement your algorithm and explain it in the report file.
d) Write the recurrence relation for the running time of your algorithm in option c)
```
2 - ) Given two sorted arrays A and B, design a divide-and-conquer algorithm that finds the kth
element of the merged array of these two sorted arrays. Do not try to merge the array at first
and find the kth element later! Implement your algorithm and analyze its worst-case running
time. You can assume that the arrays A and B have m and n items, respectively. Explain your
algorithm in your report file.


3 - ) Given an array of integers A[1; ... ;n], propose a divide-and-conquer algorithm that finds a
contiguous subset having the largest sum within A. For example, let A = [5, -6, 6, 7, -6, 7, -4,
3]. The contiguous subset with the largest sum is [6, 7 , - 6, 7] whose sum is 14. Implement your
algorithm and analyze its worst-case running time. Explain your algorithm in your report file.

4 - ) A bipartite graph is a graph whose vertices can be divided into two disjoint and
independent sets U and V such that every edge connects a vertex in U to one in V. Design a
decrease and conquer algorithm that checks whether a given graph is a bipartite graph or not.
Implement your algorithm and analyze its worst-case running time. Explain your algorithm in
report file.

5 - ) Suppose that you manage a warehouse: buy some goods, store the goods for one day and
sell them the next day. The cost of storing the goods changes daily depending on the
occupancy ratio in the warehouse. On the other hand, the selling price of the goods varies
according to markets. You want to buy and sell 500 goods and make as much money as
possible from these sales. Design a divide-and-conquer algorithm that finds the best day to
buy the goods. Consider the following example to understand the problem:

Suppose that you have ten days to buy and sell the goods.

The array of storage costs for the goods is:

```
C = [ 5 , 11 , 2 , 21 , 5 , 7 , 8 , 12 , 13 ,−]
```
The array of prices for the goods in markets is:

```
P=[−, 7 , 9 , 5 , 21 , 7 , 13 , 10 , 14 , 20 ]
```
```
Day 1 2 3 4 5 6 7 8 9 10
```
```
Cost 5 11 2 21 5 7 8 12 13 -
```
```
Price - 7 9 5 21 7 13 10 14 20
```
```
Gain 2 - 2 3 0 2 6 2 2 7
```
The best day to buy goods is the 9 th day because if you buy the goods on the 9 th day and sell
them on the 10th day, you can make 7 units of money, which is the maximum possible gain in
the schedule.


Your algorithm must report if there is no day to make money. Implement your algorithm and
analyze its worst-case running time. Explain your algorithm in the report file.

**Note:**

* All implementations must be done using Python programming language (Python 3.6). All
parts must be in one .py file.

* Try not to use external python libraries unless you have to.

* Write a driver function that includes at least one test for all your implementations.

* Prepare a report for your code explanations, complexity analysis etc. in pdf format. You can
attach the scanned handwritten work you have, if you have any, and put them in the pdf file.

* Zip your report and .py file into a .zip file before submitting it.

* Submit your assignment via Moodle.

* Late submissions will not be accepted, so do not wait until the last minute.

*** Do your homework on your own; group studies will be considered as cheating.**


