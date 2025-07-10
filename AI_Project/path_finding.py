from collections import deque
import heapq

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
_strategy = 'bfs'  # Default strategy

def set_strategy(new_strategy):
    global _strategy
    _strategy = new_strategy

def get_strategy():
    global _strategy
    return _strategy

def get_neighbors(node, maze):
    neighbors = []
    for d in DIRS:
        nx, ny = node[0] + d[0], node[1] + d[1]
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != '#':
            neighbors.append((nx, ny))
    return neighbors

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def bfs(start, goal, maze):
    queue = deque([start])
    visited = {start: None}
    while queue:
        current = queue.popleft()
        if current == goal:
            break
        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)
    return reconstruct_path(start, goal, visited)

def dfs(start, goal, maze):
    stack = [start]
    visited = {start: None}
    while stack:
        current = stack.pop()
        if current == goal:
            break
        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited:
                visited[neighbor] = current
                stack.append(neighbor)
    return reconstruct_path(start, goal, visited)

def hill_climbing(start, goal, maze):
    current = start
    path = [current]
    visited = set()
    while current != goal:
        visited.add(current)
        neighbors = [n for n in get_neighbors(current, maze) if n not in visited]
        if not neighbors:
            break
        current = min(neighbors, key=lambda n: heuristic(n, goal))
        path.append(current)
    return path[1:]

def a_star(start, goal, maze):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {start: None}
    g_score = {start: 0}
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            break
        for neighbor in get_neighbors(current, maze):
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))
    return reconstruct_path(start, goal, came_from)

def dfs_id(start, goal, maze, max_depth=50):
    def dls(node, goal, depth, visited):
        if node == goal:
            return [node]
        if depth == 0:
            return None
        for neighbor in get_neighbors(node, maze):
            if neighbor not in visited:
                visited.add(neighbor)
                path = dls(neighbor, goal, depth-1, visited)
                if path:
                    return [node] + path
                visited.remove(neighbor)
        return None

    for depth in range(1, max_depth+1):
        visited = set([start])
        path = dls(start, goal, depth, visited)
        if path:
            return path
    return []

def reconstruct_path(start, goal, visited):
    path = []
    node = goal
    while node != start:
        node = visited.get(node)
        if node is None:
            return []
        path.insert(0, node)
    return path

def find_path(start, goal, maze, strategy=None):
    current_strategy = strategy if strategy else _strategy
    
    if current_strategy == 'bfs':
        return bfs(start, goal, maze)
    elif current_strategy == 'dfs':
        return dfs(start, goal, maze)
    elif current_strategy == 'a_star':
        return a_star(start, goal, maze)
    elif current_strategy == 'hill_climbing':
        return hill_climbing(start, goal, maze)
    elif current_strategy == 'dfs_id':
        return dfs_id(start, goal, maze)
    else:
        return bfs(start, goal, maze)  