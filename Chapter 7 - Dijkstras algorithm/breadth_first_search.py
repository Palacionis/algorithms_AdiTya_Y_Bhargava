# Chapter 6 - breadth-first search

# breadth-first search is O(V+E) - vertices + edges == people + their connections to others

# an algorithm to solve a shortest-path problem is called breadth-first search

from collections import deque


graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


search_queue  = deque()
search_queue += graph['you']

def person_is_seller(name):
  return name[-1] == 'm' # thom is the mango seller

while search_queue:
  print(search_queue)
  person = search_queue.popleft() # grab the first person of the queue
  if person_is_seller(person): 
    print(f'person {person} is a mango seller')
    break

  else:
    search_queue += graph[person]

# this approach can loop infinitely because we check neighbors twice, peggy is a friend of bob and alice, we
# do not want to do extra work if we already checked if peggy is a mango seller

# deque(['alice', 'bob', 'claire'])
# deque(['bob', 'claire', 'peggy'])
# deque(['claire', 'peggy', 'anuj', 'peggy'])
# deque(['peggy', 'anuj', 'peggy', 'thom', 'jonny'])
# deque(['anuj', 'peggy', 'thom', 'jonny'])
# deque(['peggy', 'thom', 'jonny'])
# deque(['thom', 'jonny'])
# person thom is a mango seller


def search(name):
  search_queue = deque()
  search_queue += graph[name]
  searched = set()

  while search_queue:
    # print(search_queue)
    person = search_queue.popleft()
    if person not in searched:
      # print(f'Searching {person}')
      if person_is_seller(person):
        return f'{person} is a mango seller'
      else:
        search_queue += graph[person]
        searched.add(person)
  return f'Noone is a mango seller'

search('you')

# notice how we only check if peggy is a mango seller only once

# deque(['alice', 'bob', 'claire'])
# Searching alice
# deque(['bob', 'claire', 'peggy'])
# Searching bob
# deque(['claire', 'peggy', 'anuj', 'peggy'])
# Searching claire
# deque(['peggy', 'anuj', 'peggy', 'thom', 'jonny'])
# Searching peggy
# deque(['anuj', 'peggy', 'thom', 'jonny'])
# Searching anuj
# deque(['peggy', 'thom', 'jonny'])
# deque(['thom', 'jonny'])
# Searching thom
# 'thom is a mango seller'