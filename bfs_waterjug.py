from collections import deque

def bfs_water_jug(capA, capB, goal):
    
    visited = set()
    queue = deque()

    queue.append((0,0,[]))

    while queue:
        a,b,path = queue.popleft()

        if (a,b) in visited:
            continue 

        visited.add((a,b))
        path = path +[(a,b)]

        if a == goal or b == goal:
            print("Bfs sol path: ")
            for state in path:
                print(state)
            return 
        
        next_states = [
            (capA, b),
            (a, capB),
            (a,0), (0,b),
            (a- min(a, capB-b), b+min(a, capB-b)),
            (a+min(b, capA-a), b - min(b, capA-a))
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

bfs_water_jug(4,3,2)          
          
