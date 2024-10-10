class AFN:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def accept(self, input_string):
        current_states = {self.start_state}
        for symbol in input_string:
            next_states = set()
            for state in current_states:
                if symbol in self.transition_function.get(state, {}):
                    next_states.update(self.transition_function[state][symbol])
            current_states = next_states
        return bool(current_states.intersection(self.accept_states))


states = {"q0", "q1", "q2", "q3", "q4", "q5"}
alphabet = {"0", "1"}
transition_function = {
    "q0": {"0": {"q0"}, "1": {"q0", "q1", "q3"}},
    "q1": {"0": {"q2"}},
    "q2": {"1": {"q5"}},
    "q3": {"1": {"q4"}},
    "q4": {"0": {"q5"}},
    "q5": {"0": {"q5"}, "1": {"q5"}}
}
start_state = "q0"
accept_states = {"q5"}

afn = AFN(states, alphabet, transition_function, start_state, accept_states)

test_strings = [
    "101",
    "110",
    "1001",
    "0110",
    "11101",
    "001",
    "0101",
]

for string in test_strings:
    print(f"String '{string}' é aceita? {afn.accept(string)}")

