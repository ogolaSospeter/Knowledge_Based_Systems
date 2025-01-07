# Define capacities
jug1_capacity = 3
jug2_capacity = 4
initial_state = (0, 0)  # (amount in jug1, amount in jug2)

def possible_actions(state):
    actions = []
    jug1, jug2 = state

    # Fill Jug 1
    actions.append((jug1_capacity, jug2))
    # Fill Jug 2
    actions.append((jug1, jug2_capacity))
    # Empty Jug 1
    actions.append((0, jug2))
    # Empty Jug 2
    actions.append((jug1, 0))
    # Pour from Jug 1 to Jug 2
    transfer_to_jug2 = min(jug1, jug2_capacity - jug2)
    actions.append((jug1 - transfer_to_jug2, jug2 + transfer_to_jug2))
    # Pour from Jug 2 to Jug 1
    transfer_to_jug1 = min(jug2, jug1_capacity - jug1)
    actions.append((jug1 + transfer_to_jug1, jug2 - transfer_to_jug1))

    return actions

def dfs(state, target, visited, path):
    if state in visited:
        return None
    visited.add(state)
    path.append(state)

    # Check if we reached the target in either jug
    if state[0] == target or state[1] == target:
        return path

    # Explore all possible actions from the current state
    for next_state in possible_actions(state):
        result = dfs(next_state, target, visited, path)
        if result:
            return result

    path.pop()  # Backtrack if no solution is found from this state
    return None

# Initialize variables for DFS
visited = set()
path = []
target_volume = 2

# Start DFS from initial state

solution_path = dfs(initial_state, target_volume, visited, path)
if solution_path:
    for state in solution_path:
        print(state)