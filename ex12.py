import sys
from fa import NFA, DFA

filename = "test2.txt"

file = open(filename, 'r')
lines = file.readlines()

file.close()

nfa = NFA()
dfa = DFA()

nfa.construct_nfa_from_lines(lines)

nfa.print_nfa()
print()

dfa.convert_from_nfa(nfa)

dfa.print_dfa()
