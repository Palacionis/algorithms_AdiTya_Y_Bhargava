# Chapter 2 - selection sort


# arrays versus linked lists:
#           arrays    linked lists
# reading     O(1)            O(n)
# insertion   O(n)            O(1)
# deletion    O(n)            O(1)

# linked lists are better if you want to insert elements in the middle

# Selection sort takes O(n*n) == O(n2) superscript time

# function that finds the smallest element in an array == min(arr)
def findSmallest(arr):
  smallest = arr[0]
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i

  return smallest_index


# selection sort

def seelectionSort(arr):
  new_arr = []
  for i in range(len(arr)):
    smallest = findSmallest(arr)
    new_arr.append(arr.pop(smallest))

  return new_arr



# arrays allow fast reads
# linked lists allow fast inserts / deletes
