# CSE 321 Homework 1

## Due date: 25 / 10 / 2019

1 - ) Answer in detail the questions that are shown below by using asymptotic notations, yes /
no answers and plagiarizing from the web will not be accepted.

```
a) Is the following statement scientifically sound? :“The running time of algorithm A is at
least O(n^2 )”?
b) Are the following true?
i) 2 n+1 = O(2n)?
ii) 2 2n = O(2n)?
c) Let f (n) and g(n) be asymptotically nonnegative functions. Is the equation: max(f (n),
g(n)) = Θ(f(n) + g(n)) true?
```
2 - ) In each of the following situations, indicate whether f ε O(g), or f ε Ω(g), or both (in which
case f ε Θ(g)).

f(n) g(n)

```
a) n1.01 nlog^2 n
b) n! 2 n
c) √n (log n)^3
d) n2n 3 n
e) ∑ni=1 ik nk+
f) 2 n 2 n+
g) n 1/2 5 log 2 n
h) log2n log3n
```
3 - ) List the following functions according to their order of growth and prove your assertions.

Logn, √푛+ 10 , n + 10, 10n, 100n, n^2 logn, 32logn, n^6

4 - ) Analyze the complexity in time (big -Oh notation) of the following operations at a given
binary search tree (BST) that has height n:

```
a) FindMin.
b) Searching a node.
c) Delete a leaf node.
d) Merging with another BST that has height n.
```

5 - ) Find the time complexity (big -Oh notation) of the following program.

```
void function(int n)
{
int count = 0;
for (int i = 2; i <= n; i++)
if (i % 2 == 0)
{
count++;
}
else
{
i = (i – 1) * i;
}
}
```
**Notes:**

- Your submissions will be handwritten.
- You can deliver your homework to TA M. Burak Koca until 1 6 : 45 on due date (room
    119).
- Do your homework personally, group studies will be considered as cheating.


