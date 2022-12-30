#
#made by ahmadreza alizadefard
#name : dfs
#version : 1.0
#data structure : Stack
#

import randomname

def name_generator():
  name = randomname.get_name(noun=('houses'))
  return name

id = 0  
def get_id():
  global id
  id += 1
  return id

def generate_matrix(row, column):
  matrix = []
  print("enter a matrix row by row:")
  for r in range(row):
    row = []
    print("\nenter a row:")
    for c in range(column):
      rc = input("enter a 0/1:")
      row.append(rc)
    matrix.append(row)
  return matrix

# rc(row, column) is equal to exact location(x, y) of house(node) in maze(matrix)
class Node:
  def __init__(self, rc_in_matrix, children=None, parent=None, depth=0):
    self.id = get_id()
    self.name = name_generator()
    self.rc_in_matrix = rc_in_matrix
    self.depth = depth
    self.parent = parent
    self.children = children # children are (r, c)
    
  # all attrs are const => there is no set method
  # get functions 
  def get_idd(self):
    return self.id
  def get_name(self):
    return self.name

  def get_rc_in_matrix(self):
    return self.rc_in_matrix
  
  def get_parent(self):
    return self.parent
  
  def get_children(self):
    return self.children
  
class state_space_graph:
  def __init__(self, matrix, root, goal):
    self.matrix = matrix
    self.root = root
    self.goal = goal
    self.node_base_matrix = self.node_base_matrix()
    self.root_node = self.node_base_matrix[root[0]][root[1]]
    self.goal_node = self.node_base_matrix[goal[0]][goal[1]]
    
    self.graph = self.graphdict_generator()
    
    # name functions 
  def get_name(self):
    return self.name
  
  def set_name(self, new_name):
    self.name = new_name
    
  # matrix functions
  def get_matrix(self):
    return self.matrix

  def get_node_base_matrix(self):
    return self.node_base_matrix

  def show_matrix(self):
    for r in range(len(self.matrix)):
      print(r)
  
  def set_matrix(self, new_matrix):
    self.matrix = new_matrix

  def get_node_base_matrix(self):
    return self.node_base_matrix

  def get_graph(self):
    return self.graph
  
  def node_base_matrix(self):
    nbm = list()
    # r_counter = 0
    for r in range(len(self.matrix)):
      nbm.append([])
      for c in range(len(self.matrix[r])):
        # print(self.matrix[r][c])
        if (self.matrix[r][c] == 1):
          N = Node([r, c])
          nbm[r].append(N)
        else:
          nbm[r].append(0)
    return nbm

  def get_node_children(self, node):
    children = []
    rc_node = node.rc_in_matrix  #a list: [r, c]
    r = rc_node[0]
    c = rc_node[1]
    
    up = r-1
    left = c-1
    right = c+1
    down = r+1 
       
    #down
    if down < len(self.matrix):
      if self.node_base_matrix[down][c] != 0: #down
        # self.node_base_matrix[down][c].parent = node
        children.append(self.node_base_matrix[down][c])
    #right
    if right < len(self.matrix[0]):
      if self.node_base_matrix[r][right] != 0: #right
        # self.node_base_matrix[r][right].parent = node
        children.append(self.node_base_matrix[r][right])
    #left
    if left >= 0:
      if self.node_base_matrix[r][left] != 0: #left
        # self.node_base_matrix[r][left].parent = node
        children.append(self.node_base_matrix[r][left])
    #up
    if up >= 0:
      if self.node_base_matrix[up][c] != 0: 
        # self.node_base_matrix[up][c].parent = node
        children.append(self.node_base_matrix[up][c])
    
    return(children)

# key=rc : value = Node(int(id), str(name), rc, Node(parent) [children]) 
  def graphdict_generator(self):
    graphdict = {}
    for r in self.node_base_matrix:
      for c in r:
        if(c != 0):
          graphdict[c] = self.get_node_children(c) # c is equal node == a house in maze
    return graphdict
  

class Maze:
  def __init__(self, name, matrix, start_element, target_element):
    self.name = name
    self.matrix = matrix
    self.start_element = start_element
    self.target_element = target_element
    self.state_space_graph = state_space_graph(self.matrix, self.start_element, self.target_element)

  def get_name(self):
    return self.name
  
  def get_matrix(self):
    return self.matrix

  def set_name(self, new_name):
    self.name = new_name

  def set_matrix(self, new_matrix):
    self.matrix = new_matrix
    
  def show_matrix(self):
    for r in range(len(self.matrix)):
      print(r)
      
# maze modeled by spaarse matrix:
# enter a matrix row by row (obstcles:0 houses:1)
matrix = [
  [0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,  0],
  [0,  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1,  0],
  [0,  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1,  0],
  [1,  1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1,  0],
  [0,  1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,  0],
  [0,  1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1,  0],
  [0,  1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1,  0],
  [0,  1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1,  0],
  [0,  1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1,  0],
  [0,  1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1,  0],  
  [0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0]
]
maze = Maze("my maze",  matrix, [3,0], [0,13])
state_space_graph = maze.state_space_graph
nbm = state_space_graph.node_base_matrix

graph_dict = state_space_graph.get_graph()
starter = state_space_graph.root_node
goal = state_space_graph.goal_node

def Goal_Test(node):
  return goal.id == node.id

# start of DFS ##################################################

def Visited_dfs(node):
  explored_dfs.add(node)

def Not_Explored_dfs(node):
  return node not in explored_dfs

explored_dfs = set()
fringe_dfs = list()

def DFS_goal__node(graph_dict, starter):
  
  fringe_dfs.append(starter)
  
  while(True):
    
    Visited_dfs(fringe_dfs[-1])
    neighborhood = graph_dict[fringe_dfs[-1]]
    
    if(Goal_Test(fringe_dfs[-1])):
      return fringe_dfs[-1]

    parent = fringe_dfs[-1]
    fringe_dfs.pop()  
      
    for neighbor in neighborhood:
      if(Not_Explored_dfs(neighbor)):
        neighbor.parent = parent
        fringe_dfs.append(neighbor)
        
  
goal_node_dfs = DFS_goal__node(graph_dict, starter)

track_dfs = list()

def dfs_track(last_target):

  track_dfs.append(last_target)

  while(last_target.parent):
    track_dfs.append(last_target.parent)
    last_target = last_target.parent
  else:
    return track_dfs

track_node = dfs_track(goal_node_dfs)

for node in reversed(track_node):
  print(node.id, node.rc_in_matrix, end="=>")


# end of DFS #########################################################
print("\n------------------------------------------------------")
