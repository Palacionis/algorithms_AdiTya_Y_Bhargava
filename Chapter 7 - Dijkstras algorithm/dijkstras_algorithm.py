# Chapter 7 - dijkstra's algorithm

# Dijkstra's algorithm has 4 steps
  # find the cheapest node
  # checking if there is a cheaper path to the neigbors of this node, if so, update the costs
  # repeat until you have done this for every node in the graph
  # calculate the final path

# graph table
graph = {}

graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['end'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 5

graph['end'] = {}

# costs table
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['end'] = infinity

# parents table

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['end'] = None


processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]

        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node



node = find_lowest_cost_node(costs)

while node is not None:
  cost = costs[node]
  neighbors = graph[node]
  for n in neighbors.keys():
      new_cost = cost + neighbors[n]
      if n in costs:
          if costs[n] > new_cost:
              costs[n] = new_cost
              parents[n] = node
      else:
          costs[n] = new_cost
          parents[n] = node
  processed.append(node)
  node = find_lowest_cost_node(costs)


def find_path(parents, finish):
  path = []
  node = finish
  while node:
      path.insert(0, node)
      if parents.__contains__(node):
          node = parents[node]
      else:
          node = None
  return path


path = find_path(parents, 'end')
distance = costs['end']

print(f'Path is: {path}')
print(f'Distance from start to finish is: {distance}')

# Path is: ['start', 'b', 'a', 'end']
# Distance from start to finish is: 6

# graph table

graph = {}
graph['start'] = {}
graph['start']['a'] = 5
graph['start']['b'] = 2
 
graph['a'] = {}
graph['a']['c'] = 4
graph['a']['d'] = 2
 
graph['b'] = {}
graph['b']['a'] = 8
graph['b']['d'] = 7
 
graph['c'] = {}
graph['c']['d'] = 6
graph['c']['finish'] = 3
 
graph['d'] = {}
graph['d']['finish'] = 1
graph['finish'] = {}
 
infinity = float('inf')
 
costs = {}
costs['start'] = 0
 
parents = {}
 
processed = []
 
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
 
    for node in costs:
        cost = costs[node]
 
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
 
 
 
node = find_lowest_cost_node(costs)
 
while node is not None:
  cost = costs[node]
  neighbors = graph[node]
  for n in neighbors.keys():
      new_cost = cost + neighbors[n]
      if n in costs:
          if costs[n] > new_cost:
              costs[n] = new_cost
              parents[n] = node
      else:
          costs[n] = new_cost
          parents[n] = node
  processed.append(node)
  node = find_lowest_cost_node(costs)
 
 
def find_path(parents, finish):
  path = []
  node = finish
  while node:
      path.insert(0, node)
      if parents.__contains__(node):
          node = parents[node]
      else:
          node = None
  return path
 
 
path = find_path(parents, 'finish')
distance = costs['finish']
 
print(f'Path is: {path}')
print(f'Distance from start to finish is: {distance}')



# Path is: ['start', 'a', 'd', 'finish']
# Distance from start to finish is: 8