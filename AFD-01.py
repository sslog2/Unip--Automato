class DFA:
    def __init__(self, transition_function, start_state, accept_states):
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def accept(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if symbol not in {"0", "1"}:
                return False
            current_state = self.transition_function[current_state][symbol]

        return current_state in self.accept_states


states = {"q0", "q1"}
alphabet = {"0", "1"}
transition_function = {
    "q0": {"0": "q0", "1": "q1"},
    "q1": {"0": "q0", "1": "q1"},
}
start_state = "q0"
accept_states = {"q1"}

dfa = DFA(transition_function, start_state, accept_states)

test_strings = ["0", "1", "10", "101", "110", "1111"]
for string in test_strings:
    print(f"String '{string}' é aceita? {dfa.accept(string)}")
