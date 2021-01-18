# Chapter 3 - recursion

# recursive function to calculate factorial

def factorial(n):
  print(n)
  if n == 1:
    return 1
  return factorial(n-1) * n


# recursion functions have 2 cases: the base case and the recursive case
# a stack has two operations: push and pop, those are used during recursion
# all function calls go to one stack