class NFA:
    def __init__(
        self, states, alphabet, transition_function, start_state, accept_states
    ):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def _move(self, states, symbol):
        new_states = set()
        for state in states:
            if (
                state in self.transition_function
                and symbol in self.transition_function[state]
            ):
                new_states.update(self.transition_function[state][symbol])
        return new_states

    def accept(self, input_string):
        current_states = {self.start_state}
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            current_states = self._move(current_states, symbol)

        return bool(current_states & self.accept_states)


states = {"q0", "q1", "q2", "q3", "q4"}
alphabet = {"0", "1"}
transition_function = {
    "q0": {"0": {"q1"}},
    "q1": {"1": {"q2"}},
    "q2": {"0": {"q2"}, "1": {"q2", "q3"}},
    "q3": {"0": {"q4"}},
    "q4": {},
}
start_state = "q0"
accept_states = {"q4"}

nfa = NFA(states, alphabet, transition_function, start_state, accept_states)

test_strings = [
    "01",
    "010",
    "0110",
    "01010",
    "110",
    "0101",
    "011010",
    "0100",
    "0001",
    "011011",
]

for string in test_strings:
    print(f"String '{string}' é aceita? {nfa.accept(string)}")
