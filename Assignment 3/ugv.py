# ------------------ A* STATIC ------------------
import random
import heapq

GRID_SIZE = 70

def generate_grid(density):
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if random.random() < density:
                grid[i][j] = 1  # obstacle

    return grid


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    pq = [(0, start)]
    came_from = {}
    g_cost = {start: 0}
    explored = 0

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while pq:
        _, current = heapq.heappop(pq)
        explored += 1

        if current == goal:
            return came_from, explored

        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy

            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                if grid[nx][ny] == 1:
                    continue

                new_cost = g_cost[current] + 1

                if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_cost
                    priority = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(pq, (priority, (nx, ny)))
                    came_from[(nx, ny)] = current

    return None, explored


def reconstruct_path(came_from, start, goal):
    if came_from is None:
        return None

    path = []
    node = goal

    while node != start:
        path.append(node)
        node = came_from.get(node)
        if node is None:
            return None

    path.append(start)
    return path[::-1]


print("\n--- UGV STATIC (A*) ---")
grid = generate_grid(0.2)  # density: 0.1 low, 0.2 medium, 0.3 high
start = (0, 0)
goal = (69, 69)

came_from, explored = astar(grid, start, goal)
path = reconstruct_path(came_from, start, goal)

print("Path length:", len(path) if path else "No path")
print("Nodes explored:", explored)

def calculate_moe(path, explored):
    if path is None:
        return "No valid path"

    return {
        "Path Length": len(path),
        "Nodes Explored": explored,
        "Efficiency": round(len(path)/explored, 4)
    }
print("MOE:", calculate_moe(path, explored))