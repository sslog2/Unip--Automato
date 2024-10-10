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
            current_state = self.transition_function[current_state][symbol]
        return current_state in self.accept_states


states = {"q0", "q1", "q2", "q3"}
alphabet = {"0", "1"}
transition_function = {
    "q0": {"0": "q1", "1": "q0"},  
    "q1": {"0": "q1", "1": "q2"},  
    "q2": {"0": "q3", "1": "q2"},
    "q3": {"0": "q3", "1": "q3"},  
}
start_state = "q0"
accept_states = {"q0", "q1", "q2"}  

afd = AFD(states, alphabet, transition_function, start_state, accept_states)

test_strings = [
    "0",        
    "00",       
    "11",       
    "010",      
    "1110",     
    "00111",    
    "001010",   
]

for string in test_strings:
    print(f"String '{string}' é aceita? {afd.accept(string)}")

