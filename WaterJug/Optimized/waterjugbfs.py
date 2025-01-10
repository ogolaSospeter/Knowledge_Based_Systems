from collections import deque

def waterJugSolverBFS(jug1, jug2, targetCapacity):
    #The algorithm uses a queue (deque from the collections module) to store the states of the jugs. 
    # Initially, both jugs are empty, so the state is (0, 0).
    queue = deque([(0, 0)])
    visited = set([(0, 0)])
    parents = {}  # stores the previous state for each state,
    #which helps in tracing back the solution path once the goal is found.

    while queue:
        current_state = queue.popleft()
        amt1, amt2 = current_state

        """
        If either jug contains the desired amount of water (amt1 == aim or amt2 == aim), the algorithm reconstructs the sequence of steps leading to the solution.
It traces back from the goal state to the initial state (0, 0) using the parents dictionary and then reverses the steps to return them in the correct order.
        """
        if amt1 == targetCapacity or amt2 == targetCapacity:
            steps = []
            while current_state != (0, 0):
                steps.append(current_state)
                current_state = parents[current_state]
            steps.append((0, 0))
            steps.reverse()
            return steps

        next_states = [
            (jug1, amt2),  
            (amt1, jug2),  
            (0, amt2),     
            (amt1, 0),     
            (min(jug1, amt1 + amt2), max(0, amt1 + amt2 - jug1)),  
            (max(0, amt1 + amt2 - jug2), min(jug2, amt1 + amt2))   
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)
                parents[state] = current_state

    return None

# Example usage:
jug1_capacity = 5
jug2_capacity = 3
desired_quantity = 4

solution = waterJugSolverBFS(jug1_capacity, jug2_capacity, desired_quantity)
if solution:
    for step in solution:
        print(step)
else:
    print("No solution found.")