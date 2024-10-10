class AFD:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.transition_function = {state: {symbol: next_state for symbol, next_state in 
transitions.items()} for state, transitions in transition_function.items()}
        self.start_state = start_state
        self.accept_states = set(accept_states)

    def accept(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            current_state = self.transition_function[current_state][symbol]
        return current_state in self.accept_states


states = {"q0", "q1", "q2", "q3"}
alphabet = {"a", "b"}
transition_function = {
    "q0": {"a": "q1", "b": "q0"},  
    "q1": {"a": "q1", "b": "q2"},  
    "q2": {"a": "q3", "b": "q3"},  
    "q3": {"a": "q3", "b": "q3"}  
}
start_state = "q0"
accept_states = {"q2"}  

afd = AFD(states, alphabet, transition_function, start_state, accept_states)

test_strings = [
    "ab",        
    "aabb",      
    "abab",      
    "baba",      
    "aaabbb",    
    "ababab",    
    "a",         
    "abx",       
    "abc",       
    "abaaa",    
    "aaab",     
    "aaa",      
]

for string in test_strings:
    print(f"String '{string}' é aceita? {afd.accept(string)}")
