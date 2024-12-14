import math


# Define a tree node class
class Node:
    def __init__(self, state, parent=None):
        # The state of the node
        self.state = state
        # Parent and children pointers
        self.parent = parent
        self.children = []
        # Visit count and value (Q) for UCB
        self.visit_count = 0
        self.value = 0
        # List of unexplored actions for expansion
        self.unexplored_actions = get_legal_actions(state)

# Selection: use UCB to select the best child node
def ucb_score(child, parent, exploration_constant=math.sqrt(2)):
    if child.visit_count == 0:
        return float('inf')  # Encourage exploration
    return child.value / child.visit_count + exploration_constant * math.sqrt(
        math.log(parent.visit_count) / child.visit_count
    )

def select_node(node):
    return max(node.children, key=lambda child: ucb_score(child, node))

# Expansion: add a child node for an untried action
def expand_node(node):
    action = node.unexplored_actions.pop()
    new_state = apply_action(node.state, action)
    child_node = Node(new_state, parent=node)
    node.children.append(child_node)
    return child_node

# Simulation: play out a random game or use a heuristic until a terminal state
def simulate(state):
    while not is_terminal(state):
        action = random.choice(get_legal_actions(state))
        state = apply_action(state, action)
    return get_reward(state)

# Backpropagation: update statistics of nodes up to the root
def backpropagate(node, reward):
    while node is not None:
        node.visit_count += 1
        node.value += reward
        node = node.parent

# MCTS Loop: combine all steps
def monte_carlo_tree_search(root, iterations):
    for _ in range(iterations):
        # 1. Selection
        node = root
        while node.children and not node.unexplored_actions:
            node = select_node(node)
        
        # 2. Expansion
        if node.unexplored_actions:
            node = expand_node(node)
        
        # 3. Simulation
        reward = simulate(node.state)
        
        # 4. Backpropagation
        backpropagate(node, reward)
    
    # Return the best action from the root
    return max(root.children, key=lambda child: child.visit_count)











