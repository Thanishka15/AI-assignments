import heapq
import random
import matplotlib.pyplot as plt

# ------------------ DIJKSTRA ------------------

def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    parent = {node: None for node in graph}

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        if current_cost > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            cost = current_cost + weight

            if cost < distances[neighbor]:
                distances[neighbor] = cost
                parent[neighbor] = current_node
                heapq.heappush(pq, (cost, neighbor))

    return distances, parent


def get_path(parent, goal):
    path = []
    while goal:
        path.append(goal)
        goal = parent[goal]
    return path[::-1]

graph = {
    "Bangalore": [("Chennai", 350), ("Hyderabad", 570), ("Mysore", 150)],
    "Chennai": [("Bangalore", 350), ("Hyderabad", 630), ("Madurai", 460)],
    "Hyderabad": [("Bangalore", 570), ("Chennai", 630), ("Vijayawada", 275)],
    "Vijayawada": [("Hyderabad", 275), ("Visakhapatnam", 350), ("Chennai", 450)],
    "Visakhapatnam": [("Vijayawada", 350)],
    "Mysore": [("Bangalore", 150), ("Coimbatore", 200)],
    "Coimbatore": [("Mysore", 200), ("Madurai", 215), ("Kochi", 190)],
    "Madurai": [("Chennai", 460), ("Coimbatore", 215), ("Trichy", 135)],
    "Trichy": [("Madurai", 135), ("Chennai", 330)],
    "Kochi": [("Coimbatore", 190), ("Thiruvananthapuram", 210)],
    "Thiruvananthapuram": [("Kochi", 210)]
}

print("\n--- DIJKSTRA (Southern Cities) ---")
distances, parent = dijkstra(graph, "Bangalore")

print("Shortest distances from Bangalore:")
for city, dist in distances.items():
    print(f"{city}: {dist} km")

print("\nShortest path to Thiruvananthapuram:")
print(get_path(parent, "Thiruvananthapuram"))