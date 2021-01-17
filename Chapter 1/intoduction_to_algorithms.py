# Chapter 1 - introduction to algorithms

# For any list of n, binary search will take log2n steps to run the worst case. 2 is subscript
# whereas simple search will take n

# binary search only works when the list is sorted

def binary_search(list, item):
  low = 0
  high = len(list)-1

  while low <= high:
    mid = (low + high) // 2
    guess = list[mid]

    if guess == item:
      return mid

    if guess > item:
      high = mid - 1
    
    else:
      low = mid + 1

  return None


# some bigO notations from fastest to slowest:

# O(logn) - log time: example - binary search
# O(n) - linear time: example - simple search
# O(n * logn) example - quicksort
# O(n2) - 2 is superscript - a slow sorting algorithm, example: selection sort
# O(n!) - a really slow algorithm: example - traveling salesperson

# algorithm times are measured in terms of growth of an algorithm
