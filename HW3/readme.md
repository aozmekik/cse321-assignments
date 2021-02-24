
1 - ) There are 2n boxes standing in a row; the first n of them are black and the remaining n
boxes are white. Design a decrease-and-conquer algorithm that makes the boxes alternate in
a black-white-black-white pattern using minimum number of moves. Remember that
interchanging any two boxes is considered to be one move. Analyze the worst-case, best-case
and average-case complexities of your algorithm. Explain your algorithm in the report file.

2 - ) Fake coin problem is a famous problem and there are many versions of it in the literature.
In our version, there are n coins which look exactly the same but one of them is fake. You can
use a weighbridge which has two scales to find the fake coins. Design a decrease-and-conquer
algorithm which finds the fake coin. Analyze the worst-case, best-case and average-case
complexities of your algorithm. Explain your algorithm in the report file.

3 - ) Implement the quick sort and insertion sort algorithms and count the number of swap
operations to compare these two algorithms. Analyze the average-case complexity of the
algorithms. Compare the operations count in your report file to decide which algorithm is
better and support your analysis by using the theoretical average-case analysis of your
algorithms. Make a comparative evaluation of your experimental analysis with the theoretical
analysis. Discuss the results.

4 - ) Design a decrease and conquer algorithm that finds the median of an unsorted array.
Implement your algorithm and analyze the worst-case complexity of your algorithm.

5 - ) Suppose that there is an array A which consists of n integer values. Design a recursive
exhaustive search algorithm that finds the optimal sub-array B such that:

```
푆U푀(퐵)≤(푚푎푥(퐴)+푚in(A)) x
```
## 푛

## 4

The optimality criterion is to have the minimum number of multiplication of items in the sub-
array. For example:

Let’s A = [2, 4, 7, 5, 22, 11], and the sub-arrays that satisfy the condition:

```
푆U푀(퐵)≤ 36
```
[22, 11, 4] [22, 11, 2, 5, 7] [22, 7, 5, 2]

[22, 11, 5] [22, 11, 2, 4, 5, 7] [22, 7, 5, 4]

[22, 11, 7] [22, 7, 5, 4, 2] [22, 11, 5, 7]

[22, 11, 4, 2] [22, 11, 4, 2, 7] [22, 11, 4, 5, 7]

[22, 11, 4, 5] [22, 11, 4, 2, 5] [22, 11, 4, 7]

The optimal sub-array is [22, 11, 4].


Implement your proposed algorithm using Python. Analyze the worst-case complexity of the
algorithm. Explain your algorithm in the report file.

**Note:**

* All implementations must be done using Python programming language (Python 3.6). Write
a driver function to test your implementations. All parts must be in one .py file.

* Try not to use external python libraries unless you have to.

* Write a driver function that includes at least one test for all your implementations.

* Prepare a report for your code explainations, complexity analysis etc. in pdf format. You can
attach the scanned handwritten work you have, if you have any, and put them in the pdf file.

* Zip your report and .py file into a .zip file before submitting it.

* Submit your assignment via Moodle.

* Late submissions will not be accepted, so do not wait until the last minute.

* Do your homework on your own; group studies will be considered as cheating.


