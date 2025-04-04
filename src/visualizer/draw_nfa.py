# Digraph is used to create a directed graph
from graphviz import Digraph

def draw_nfa(nfa, filename='nfa_graph'):
    # the object dot shayel el visualization bta3 el graph and the format of the file zy mna 3ayza 
    dot = Digraph(format='png')
    dot.attr(rankdir='LR')  # graph layout direction from left-to-right

    state_id_map = {}     # 3shan akeep track of unique IDs for each state in the NFA 
    state_counter = [0]

#-----------------------------------------------------
# assigns a unique ID (like "S0", "S1") to each state.
# lw el state already leha id 3ndi baraga3o lw la b3mlha wa7d w araga3o
    def get_id(state):
        if state not in state_id_map:
            state_id_map[state] = f"S{state_counter[0]}"
            state_counter[0] += 1
        return state_id_map[state]
#-----------------------------------------------------

# DFs mn 3nd el initial bta3 el nfa states
    visited = set()
    stack = [nfa.initial]

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)

# bgeb el id bta3 el current wl id bta3 el target w a3ml edge benhom a7ot 3leh el label
        curr_id = get_id(current)
        for label, target in [(current.label if current.label else 'ε', current.edge1), ('ε', current.edge2)]:
            if target:
                target_id = get_id(target)
                dot.edge(curr_id, target_id, label=label)
                stack.append(target)

    # Draw nodes
    for state, sid in state_id_map.items():
        if state == nfa.accept:
            dot.node(sid, shape='doublecircle')  # Accept state
        else:
            dot.node(sid, shape='circle')

    # Mark the start state
    dot.node('start', shape='point')
    dot.edge('start', get_id(nfa.initial), label='start')

    # Show diagram
    dot.render(filename, view=True)  # Will open the image