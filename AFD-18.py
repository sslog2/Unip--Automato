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


states = {"q00", "q01", "q10", "q11"} 
alphabet = {"0", "1"}
transition_function = {
    "q00": {"0": "q10", "1": "q01"},  
    "q01": {"0": "q11", "1": "q00"},  
    "q10": {"0": "q00", "1": "q11"},  
    "q11": {"0": "q01", "1": "q10"},  
}
start_state = "q00"
accept_states = {"q11"}  

afd = AFD(states, alphabet, transition_function, start_state, accept_states)

test_strings = [
    "01",      
    "10",      
    "0011",   
    "1100",   
    "000",     
    "111",     
    "000111",  
    "101010",  
]

for string in test_strings:
    print(f"String '{string}' é aceita? {afd.accept(string)}")

