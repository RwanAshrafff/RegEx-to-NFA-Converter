import graphviz
from collections import deque

def draw_dfa(dfa, filename='dfa_graph'):
    dot = graphviz.Digraph('DFA')
    dot.attr(rankdir='LR')
    
    # Create a mapping from state objects to sequential names using BFS order
    state_names = {}
    visited = set()
    queue = deque()
    counter = 0
    
    # Start with initial state
    queue.append(dfa.initial_state)
    visited.add(dfa.initial_state)
    state_names[dfa.initial_state] = f'q{counter}'
    counter += 1
    
    # BFS to assign state names
    while queue:
        current_state = queue.popleft()
        # Process transitions in sorted order for consistent numbering
        for symbol in sorted(current_state.transitions.keys()):
            next_state = current_state.transitions[symbol]
            if next_state not in visited:
                visited.add(next_state)
                state_names[next_state] = f'q{counter}'
                counter += 1
                queue.append(next_state)
    
    # Add states with sequential names
    for state in dfa.states:
        if state.is_accepting:
            dot.node(state_names[state], shape='doublecircle', label=state_names[state])
        else:
            dot.node(state_names[state], shape='circle', label=state_names[state])
    
    # Add transitions using sequential names
    for state in dfa.states:
        for symbol, next_state in state.transitions.items():
            dot.edge(state_names[state], state_names[next_state], label=symbol)
    
    # Add initial state arrow
    dot.node('start', shape='point')
    dot.edge('start', state_names[dfa.initial_state])
    
    # Save the DOT file
    with open('dfa_graph', 'w') as f:
        f.write(dot.source)
    print("DFA graph saved as 'dfa_graph'")
    
    # Also render as PNG for visualization
    dot.render(filename, format='png', view=True, cleanup=True)  # Will open the image