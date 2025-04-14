import graphviz
from collections import deque

def draw_dfa(dfa, filename='dfa_graph'):
    dot = graphviz.Digraph('DFA')
    dot.attr(rankdir='LR')
    
    
    state_names = {}
    visited = set()
    queue = deque()
    counter = 0
    
    
    queue.append(dfa.initial_state)
    visited.add(dfa.initial_state)
    state_names[dfa.initial_state] = f'q{counter}'
    counter += 1
    
    
    while queue:
        current_state = queue.popleft()
        
        for symbol in sorted(current_state.transitions.keys()):
            next_state = current_state.transitions[symbol]
            if next_state not in visited:
                visited.add(next_state)
                state_names[next_state] = f'q{counter}'
                counter += 1
                queue.append(next_state)
    
    
    for state in dfa.states:
        if state.is_accepting:
            dot.node(state_names[state], shape='doublecircle', label=state_names[state])
        else:
            dot.node(state_names[state], shape='circle', label=state_names[state])
    
    
    for state in dfa.states:
        for symbol, next_state in state.transitions.items():
            dot.edge(state_names[state], state_names[next_state], label=symbol)
    
    
    dot.node('start', shape='point')
    dot.edge('start', state_names[dfa.initial_state])
    
    
    with open('dfa_graph', 'w') as f:
        f.write(dot.source)
    print("DFA graph saved as 'dfa_graph'")
    
    
    dot.render(filename, format='png', view=True, cleanup=True) 