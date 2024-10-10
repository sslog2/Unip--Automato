class AFN:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def epsilon_closure(self, state):
        stack = [state]
        closure = {state}
        while stack:
            current_state = stack.pop()
            if current_state in self.transition_function and '' in self.transition_function[current_state]:
                for next_state in self.transition_function[current_state]['']:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
        return closure

    def move(self, states, symbol):
        new_states = set()
        for state in states:
            if state in self.transition_function and symbol in self.transition_function[state]:
                new_states.update(self.transition_function[state][symbol])
        return new_states

class AFD:
    def __init__(self, afn):
        self.afn = afn
        self.dfa_transition_function = {}
        self.dfa_states = []
        self.dfa_start_state = frozenset(self.afn.epsilon_closure(self.afn.start_state))
        self.dfa_accept_states = set()
        self.convert_afn_to_afd()

    def convert_afn_to_afd(self):
        queue = [self.dfa_start_state]
        visited = {self.dfa_start_state}
        
        while queue:
            current_state = queue.pop(0)
            self.dfa_states.append(current_state)
            
            for symbol in self.afn.alphabet:
                move_states = self.afn.move(current_state, symbol)
                # Corrigido para aplicar a frozenset corretamente sobre o resultado final
                next_state = frozenset(
                    state for move_state in move_states for state in self.afn.epsilon_closure(move_state)
                )
                
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append(next_state)
                
                self.dfa_transition_function[(current_state, symbol)] = next_state
                
                if any(state in self.afn.accept_states for state in next_state):
                    self.dfa_accept_states.add(next_state)

    def accept(self, input_string):
        current_state = self.dfa_start_state
        for symbol in input_string:
            current_state = self.dfa_transition_function.get((current_state, symbol), frozenset())
        return current_state in self.dfa_accept_states


states = {'q0', 'q1', 'q2'}
alphabet = {'0', '1'}
transition_function = {
    'q0': {'0': {'q0', 'q1'}, '1': {'q0'}},  
    'q1': {'1': {'q2'}},                     
    'q2': {}                                 
}
start_state = 'q0'
accept_states = {'q2'}

afn = AFN(states, alphabet, transition_function, start_state, accept_states)
afd = AFD(afn)

test_strings = [
    "01",       
    "1101",     
    "1111",    
    "010",     
    "00001",    
]

for string in test_strings:
    print(f"String '{string}' é aceita? {afd.accept(string)}")

