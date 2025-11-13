from collections import deque

# Check if state is safe
def Is_safe(state):
    f, w, g, c = state

    # Wolf eats Goat if farmer is not there
    if w == g and f != w:
        return False

    # Goat eats Cabbage if farmer is not there
    if g == c and f != g:
        return False

    return True


# Return all possible next moves
def successor(state):
    f, w, g, c = state
    moves = []

    # function to change side
    def opposite(x):
        return 'R' if x == 'L' else 'L'

    # Farmer goes alone
    new = (opposite(f), w, g, c)
    if Is_safe(new):
        moves.append(new)

    # Farmer takes Wolf
    if f == w:
        new = (opposite(f), opposite(w), g, c)
        if Is_safe(new):
            moves.append(new)

    # Farmer takes Goat
    if f == g:
        new = (opposite(f), w, opposite(g), c)
        if Is_safe(new):
            moves.append(new)

    # Farmer takes Cabbage
    if f == c:
        new = (opposite(f), w, g, opposite(c))
        if Is_safe(new):
            moves.append(new)

    return moves


# Breadth First Search to find shortest solution path
def bfs(start, goal):
    queue = deque([start])
    parent = {start: None}
    visited = set([start])

    while queue:
        current = queue.popleft()

        if current == goal:  # Found solution
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return list(reversed(path))

        for nxt in successor(current):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = current
                queue.append(nxt)

    return None  # No solution


# Starting state: all on left side
start_state = ('L', 'L', 'L', 'L')
goal_state  = ('R', 'R', 'R', 'R')

solution = bfs(start_state, goal_state)

# Print solution path
if solution:
    print("\nSolution Found:\n")
    for step, s in enumerate(solution):
        print(f"Step {step}: Farmer={s[0]}, Wolf={s[1]}, Goat={s[2]}, Cabbage={s[3]}")
else:
    print("No solution exists.")
