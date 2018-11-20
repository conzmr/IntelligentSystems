import timeit
from collections import deque

class Node:
    def __init__(self, state, parent, move, depth, cost):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

        if self.state:
            self.map = ''.join(str(e) for e in self.state)

    def __eq__(self, other):
        return self.map == other.map

    def __lt__(self, other):
        return self.map < other.map


cells_number = 0
grid_size = 0
initial_state = list()
goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
goal_node = Node
expanded_nodes = 0
max_search_depth = 0
movements_sequence = list()
costs = set()

def setInitialState(initial_config):
    global cells_number, grid_size
    tiles = initial_config.split(" ")
    for tile in tiles:
        initial_state.append(int(tile))
    cells_number = len(initial_state)
    grid_size = int(cells_number ** 0.5)


def bfs(initial_state):
    global goal_node, max_search_depth
    explored, queue = set(), deque([Node(initial_state,
    None, None, 0, 0)])
    while queue:
        node = queue.popleft()
        explored.add(node.map)
        if node.state == goal_state:
            goal_node = node
            return queue
        neighbors = getNeighbors(node)
        for neighbor in neighbors:
            if neighbor.map not in explored:
                queue.append(neighbor)
                explored.add(neighbor.map)
                if neighbor.depth > max_search_depth:
                    max_search_depth += 1



def getNeighbors(node):
    global expanded_nodes
    expanded_nodes += 1
    neighbors = list()
    neighbors.append(Node(move(node.state, 'Up'), node,
    'Up', node.depth + 1, node.cost + 1))
    neighbors.append(Node(move(node.state, 'Down'), node,
    'Down', node.depth + 1, node.cost + 1))
    neighbors.append(Node(move(node.state, 'Left'), node,
    'Left', node.depth + 1, node.cost + 1))
    neighbors.append(Node(move(node.state, 'Right'), node,
    'Right', node.depth + 1, node.cost + 1))
    nodes = [neighbor for neighbor in neighbors if neighbor.state]
    return nodes


def move(state, position):
    new_state = state[:]
    index = new_state.index(0)

    if position == 'Up':
        if index not in range(0, grid_size):
            temp = new_state[index - grid_size]
            new_state[index - grid_size] = new_state[index]
            new_state[index] = temp
            return new_state
        else:
            return None

    if position == 'Down':
        if index not in range(cells_number - grid_size, cells_number):
            temp = new_state[index + grid_size]
            new_state[index + grid_size] = new_state[index]
            new_state[index] = temp
            return new_state
        else:
            return None

    if position == 'Left':
        if index not in range(0, cells_number, grid_size):
            temp = new_state[index - 1]
            new_state[index - 1] = new_state[index]
            new_state[index] = temp
            return new_state
        else:
            return None

    if position == 'Right':
        if index not in range(grid_size - 1, cells_number, grid_size):
            temp = new_state[index + 1]
            new_state[index + 1] = new_state[index]
            new_state[index] = temp
            return new_state
        else:
            return None



def getPath():
    current_node = goal_node
    while initial_state != current_node.state:
        movements_sequence.insert(0, current_node.move)
        current_node = current_node.parent
    return movements_sequence


def setOutput(time):
    global movements_sequence
    node_size = 72
    movements_sequence = getPath()
    used_memory = node_size*max_search_depth
    print("path_to_goal: " + str(movements_sequence))
    print("path_cost: " + str(goal_node.depth))
    print("expanded_nodes: " + str(expanded_nodes))
    print("running_time: " + format(time, '.2f'))
    print("used_memory: " + str(used_memory))


def main():
    file = open('initial_state.txt', 'r')
    initial_config = file.read().rstrip()
    setInitialState(initial_config)
    start = timeit.default_timer()
    frontier = bfs(initial_state)
    stop = timeit.default_timer()
    setOutput(stop-start)


if __name__ == "__main__":
    main()
