from collections import deque

def Is_safe(state): #state is like array index from 0to3 containing state of a thing currently
    F=state[0]
    G=state[1]
    W=state[2]
    C=state[3]
    if G==C and F!=G:
        return False
    elif W==G and F!=W :
        return False
    else:
        return True

def opposite(f):
    if f == "R":
        return "L"
    else:
        return "R"


def Safe_move(state):
    F=state[0]
    G=state[1]
    W=state[2]
    C=state[3]
    
    safe=[]

    new_state=[opposite(F),G,W,C]
    if (Is_safe(new_state)):
        safe.append(new_state)
    if F==G:
        new_state=[opposite(F),opposite(G),W,C]
        if (Is_safe(new_state)):
                safe.append(new_state)
    if F==W:
        new_state=[opposite(F),G,opposite(W),C]
        if (Is_safe(new_state)):
            safe.append(new_state)
    if F==C:
        new_state=[opposite(F),G,W,opposite(C)]
        if (Is_safe(new_state)):
            safe.append(new_state)
    
    return safe

def solving(initial_state):
    goal_state = ['R', 'R', 'R', 'R']
    queue = deque([ [initial_state] ])
    visited = { tuple(initial_state) }
    while queue:
        current_path = queue.popleft()
        current_state = current_path[-1]
        if current_state == goal_state:
            print(" Solution found!")
            return current_path  
        for next_state in Safe_move(current_state):
            if tuple(next_state) not in visited:
                visited.add(tuple(next_state))
                new_path = current_path + [next_state]
                queue.append(new_path)

  
    print("No solution found.")
    return None


def print_solution(path):
    if path is None:
        return
    
    print("\n--- (Farmer, Goat, Wolf, Cabbage) ---")
    for i, step in enumerate(path):
        print(f"Step {i}: {step}")


state = ['L', 'L', 'L', 'L']
solution_path = solving(state)
print_solution(solution_path)