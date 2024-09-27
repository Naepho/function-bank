Welcome to the documentation for this function bank !  

# Table of contents
- [Table of contents](#table-of-contents)
- [Python](#python)
  - [Data structures](#data-structures)
  - [Search algorithms](#search-algorithms)


# Python

## Data structures
**Priority queue** : a queue sorted according to priority. The lowest priority is the first out. Support for automatic priority computation is available.

## Search algorithms
**A\*** : search algorithm based on a cost function. This function should be the sum of two contributions : $f(n) = c(n) + h(n)$. $c(n)$ is the cost that it took to get to the node $n$. $h(n)$ is the expected cost to get to the goal. This last function should satisfy the condition $h(n) \le c(n, a, n') + h(n')$ where $n'$ is a successor node and $a$ is the action taken to get from $n$ to $n'$.
