from collections import deque

class DFAState:
    def __init__(self, states, is_accepting=False):
        self.states = states 
        self.is_accepting = is_accepting
        self.transitions = {}

class DFA:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.states = set()

def epsilon_closure(nfa_state, visited=None):
    if visited is None:
        visited = set()
    if nfa_state in visited:
        return visited
    visited.add(nfa_state)
    if nfa_state.edge1 and nfa_state.label is None:
        epsilon_closure(nfa_state.edge1, visited)
    if nfa_state.edge2 and nfa_state.label is None:
        epsilon_closure(nfa_state.edge2, visited)
    return visited

def move(states, symbol):
    result = set()
    for state in states:
        if state.label == symbol:
            result.add(state.edge1)
    return result

def nfa_to_dfa(nfa):
   
    initial_nfa_states = epsilon_closure(nfa.initial)
    initial_dfa_state = DFAState(initial_nfa_states, nfa.accept in initial_nfa_states)
    
    dfa = DFA(initial_dfa_state)
    dfa.states.add(initial_dfa_state)
    
    
    queue = deque([initial_dfa_state])
    
    
    while queue:
        current_dfa_state = queue.popleft()
        
        
        symbols = set()
        for nfa_state in current_dfa_state.states:
            if nfa_state.label and nfa_state.label != 'ε':
                symbols.add(nfa_state.label)
        
        
        for symbol in symbols:
            
            next_nfa_states = move(current_dfa_state.states, symbol)
            
            
            next_nfa_states_closure = set()
            for state in next_nfa_states:
                next_nfa_states_closure.update(epsilon_closure(state))
            
            
            existing_state = None
            for dfa_state in dfa.states:
                if dfa_state.states == next_nfa_states_closure:
                    existing_state = dfa_state
                    break
            
            if existing_state is None:
                
                new_dfa_state = DFAState(
                    next_nfa_states_closure,
                    nfa.accept in next_nfa_states_closure
                )
                dfa.states.add(new_dfa_state)
                queue.append(new_dfa_state)
                current_dfa_state.transitions[symbol] = new_dfa_state
            else:
                current_dfa_state.transitions[symbol] = existing_state
    
    return dfa 