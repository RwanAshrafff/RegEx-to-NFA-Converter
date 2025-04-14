class state:
    def __init__(self):
        self.label = None
        self.edge1 = None
        self.edge2 = None

class nfa:
    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept


def compile(postfix):
    nfaStack = []

    for c in postfix.split():
        if c == '*':
            nfa1 = nfaStack.pop()
            initial, accept = state(), state()
            initial.edge1, initial.edge2 = nfa1.initial, accept
            nfa1.accept.edge1, nfa1.accept.edge2 = nfa1.initial, accept
            nfaStack.append(nfa(initial, accept))

        elif c == '.':
            nfa2, nfa1 = nfaStack.pop(), nfaStack.pop()
            nfa1.accept.edge1 = nfa2.initial
            nfaStack.append(nfa(nfa1.initial, nfa2.accept))

        elif c == '|':
            nfa2, nfa1 = nfaStack.pop(), nfaStack.pop()
            initial = state()
            initial.edge1, initial.edge2 = nfa1.initial, nfa2.initial
            accept = state()
            nfa1.accept.edge1 = accept
            nfa2.accept.edge1 = accept
            nfaStack.append(nfa(initial, accept))

        elif c == '+':
            nfa1 = nfaStack.pop()
            accept, initial = state(), state()
            initial.edge1 = nfa1.initial
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            nfaStack.append(nfa(initial, accept))

        elif c == '?':
            nfa1 = nfaStack.pop()
            accept, initial = state(), state()
            initial.edge1, initial.edge2 = nfa1.initial, accept
            nfa1.accept.edge1 = accept
            nfaStack.append(nfa(initial, accept))

        else:
            accept, initial = state(), state()
            initial.label = c
            initial.edge1 = accept
            nfaStack.append(nfa(initial, accept))

    return nfaStack.pop()
