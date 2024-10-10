class DFA:
    def __init__(
        self, states, alphabet, transition_function, start_state, accept_states
    ):
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


states = {"q0", "q1"}
alphabet = {"a", "b"}
transition_function = {
    "q0": {"a": "q1", "b": "q0"},
    "q1": {"a": "q0", "b": "q1"},
}
start_state = "q0"
accept_states = {"q1"}

dfa = DFA(states, alphabet, transition_function, start_state, accept_states)

test_strings = [
    "a",
    "b",
    "aa",
    "ab",
    "ba",
    "aaa",
    "aab",
    "abb",
    "abab",
    "aabab",
    "bbbb",
    "aabba",
]

for string in test_strings:
    print(f"String '{string}' é aceita? {dfa.accept(string)}")
