def dfs_water_jug(capA, capB, goal):
    stack = [(0,0,[])]
    visited = set()

    while stack:
        a,b,path = stack.pop()

        if (a,b) in visited:
            continue

        visited.add((a,b))

        path = path+ [(a,b)]

        if a == goal or b == goal:
            print("DFS sol path: ")
            for state in path:
                print(state)
            return 
        
        next_states = [
            (capA,b),
            (a,capB),
            (0,b),
            (a,0),
            (a - min(a, capB-b), b + min(a, capB-b)),
            (a + min(b, capA-a), b - min(b, capA-a))
        ]

        for state in next_states:
            if state not in visited:
                stack.append((state[0], state[1], path))

dfs_water_jug(4,3,2)