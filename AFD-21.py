class AFD:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def accept(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False 
            current_state = self.transition_function[current_state].get(symbol, "q2")
        return current_state in self.accept_states


states = {"q0", "q1", "q2"}
alphabet = {"a", "b"}
transition_function = {
    "q0": {"a": "q0", "b": "q1"},
    "q1": {"a": "q0"},           
    "q2": {"a": "q2", "b": "q2"} 
}

start_state = "q0"
accept_states = {"q0"}  

afd = AFD(states, alphabet, transition_function, start_state, accept_states)

test_strings = [
    "a",        
    "b",        
    "ab",      
    "ba",     
    "bba",     
    "baa",     
    "aab",     
    "aaba",    
    "babab",   
    "bababa",   
    "",         
]

for string in test_strings:
    print(f"String '{string}' é aceita? {afd.accept(string)}")

