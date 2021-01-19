# Chapter 4 - quicksort

# a quicksort function

def quicksort(arr):
  print(arr)
  if len(arr) < 2: # the base case
    return arr # arrays with 1 or 0 elements are already 'sorted'

  pivot = arr[0]
  less = [x for x in arr[1:] if x <= pivot]
  more = [x for x in arr[1:] if x > pivot]


  return quicksort(less) + [pivot] + quicksort(more)


print(quicksort([5, 10, 3, 2]))
# [2, 3, 5, 10]

# by selecting the pivot to be a random element, the average runtime of quicksort is O(nlogn)
