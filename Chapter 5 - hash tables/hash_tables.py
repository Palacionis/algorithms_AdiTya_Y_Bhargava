# Chapter 5 - hash tables

# hash tables have O(1) time complexity
# dictionaries == hash tables in Python 

# an example of good dictionaries usage is cache

# when you visit site like facebook, many pages are stored in the hash table, like terms and conditions,
# home page and more. This way often visited sites load faster for the end user

cache = {}

def get_page(url):
  if cache.get(url):
    return cache[url]
  else:
    data = get_data_from_server(url) # pseudo function to store web data
    cache[url] = data
    return data


# to avoid hash colisions, the simple trick is: if multiple keys map to the same slot, start a linked list
# hash tables uses an array for storage
# resizing a hash table is smart when your load factor ( used slots / all slots ) is greater than 0.7

# array + hash function == hash table