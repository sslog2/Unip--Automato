class DFA:
    def __init__(self, transition_function, start_state, accept_states):
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def accept(self, input_string):
        current_state = self.start_state
        if not input_string:
            return False
        first_symbol = input_string[0]
        for symbol in input_string:
            if symbol not in {"0", "1"}:
                return False
            current_state = self.transition_function[current_state][symbol]
        if (first_symbol == "0" and input_string[-1] == "0") or (
            first_symbol == "1" and input_string[-1] == "1"
        ):
            return True
        return False


states = {"q0", "q1"}
alphabet = {"0", "1"}
transition_function = {
    "q0": {"0": "q1", "1": "q1"},
    "q1": {"0": "q1", "1": "q1"},
}

start_state = "q0"
accept_states = {"q1"}

dfa = DFA(transition_function, start_state, accept_states)

test_strings = ["0", "1", "00", "11", "010", "101", "111", "100", "011", "001"]
for string in test_strings:
    print(f"String '{string}' é aceita? {dfa.accept(string)}")
