class NFA: #НКА
    def __init__(self):
        self.num_states = 0 #кол-во сост.
        self.states = []
        self.symbols = []#алфавит
        self.num_accepting_states = 0
        self.accepting_states = [] #конечные сост.
        self.start_state = 0 #нач. сост
        self.transition_functions = []


    def init_states(self):
        self.states = list(range(self.num_states))

    def print_nfa(self):#вывод
        print(self.num_states)
        print("".join(self.symbols))
        print(str(self.num_accepting_states) + " " + " ".join(str(accepting_state) for accepting_state
                                                              in self.accepting_states))
        print(self.start_state)

        for transition in sorted(self.transition_functions):
            print(" ".join(str(value) for value in transition))


    def construct_nfa_from_lines(self, lines): #построить по строкам
        self.num_states = int(lines[0]) #кол-во сост
        self.init_states()
        self.symbols = list(lines[1].strip()) #алфавит

        accepting_states_line = lines[2].split(" ") #конечные сост.
        for index in range(len(accepting_states_line)):
            if index == 0:
                self.num_accepting_states = int(accepting_states_line[index])
            else:
                self.accepting_states.append(int(accepting_states_line[index]))
        
        self.startState = int(lines[3]) #нач. сост.
        
        
        for index in range(4, len(lines)): #добавляем ребра
            transition_func_line = lines[index].split(" ")
            
            starting_state = int(transition_func_line[0])
            transition_symbol = transition_func_line[1]
            ending_state = int(transition_func_line[2])
            
            transition_function = (starting_state, transition_symbol, ending_state);
            self.transition_functions.append(transition_function)        


class DFA: #ДКА
    def __init__(self):
        self.num_states = 0
        self.symbols = []
        self.num_accepting_states = 0
        self.accepting_states = []
        self.start_state = 0
        self.transition_functions = []
        self.q = []
    
    #перевод из нка
    def convert_from_nfa(self, nfa):
        self.symbols = nfa.symbols
        self.start_state = nfa.start_state

        nfa_transition_dict = {}
        dfa_transition_dict = {}
        
        # комбинируем переходы НКА (удаляем лямбда-пер.)
        for transition in nfa.transition_functions: #проходим по всем функциям перехода
            starting_state = transition[0]
            transition_symbol = transition[1]
            ending_state = transition[2]
            
            if (starting_state, transition_symbol) in nfa_transition_dict: #ребро уже есть
                nfa_transition_dict[(starting_state, transition_symbol)].append(ending_state)#добавим состояние в переход
            else:
                nfa_transition_dict[(starting_state, transition_symbol)] = [ending_state]

        self.q.append((0,))
        
        # переводим переходы НКА в ДКА
        for dfa_state in self.q:#для каждого состояния- мн-ва
            for symbol in nfa.symbols:#для каждого символа
                if len(dfa_state) == 1 and (dfa_state[0], symbol) in nfa_transition_dict:
                    dfa_transition_dict[(dfa_state, symbol)] = nfa_transition_dict[(dfa_state[0], symbol)]#копируем переход
                    
                    if tuple(dfa_transition_dict[(dfa_state, symbol)]) not in self.q:#если состояние отсутствует
                        self.q.append(tuple(dfa_transition_dict[(dfa_state, symbol)]))#добавим его
                else:
                    destinations = []#окончания переходов
                    final_destination = []#итог. сост.(U delta(q,a))
                    
                    for nfa_state in dfa_state: #для каждого состояние в мн-ве
                        if (nfa_state, symbol) in nfa_transition_dict \
                                and nfa_transition_dict[(nfa_state, symbol)] not in destinations:
                            destinations.append(nfa_transition_dict[(nfa_state, symbol)])
                    
                    if not destinations:#нет окончаний
                        final_destination.append(None)
                    else:  
                        for destination in destinations:
                            for value in destination:
                                if value not in final_destination:
                                    final_destination.append(value)
                        
                    dfa_transition_dict[(dfa_state, symbol)] = final_destination
                        
                    if tuple(final_destination) not in self.q:
                        self.q.append(tuple(final_destination))

        # переводим состояния НКА в состояния ДКА
        for key in dfa_transition_dict:
            self.transition_functions.append((self.q.index(tuple(key[0])), key[1],
                                              self.q.index(tuple(dfa_transition_dict[key]))))

        #сохранение мн-ва F
        for q_state in self.q:
            for nfa_accepting_state in nfa.accepting_states:
                if nfa_accepting_state in q_state:
                    self.accepting_states.append(self.q.index(q_state))
                    self.num_accepting_states += 1


    def print_dfa(self):#вывод
        print(len(self.q))
        print("".join(self.symbols))
        print(str(self.num_accepting_states) + " " + " ".join(str(accepting_state) for accepting_state
                                                              in self.accepting_states))
        print(str(self.start_state) + "'")
        
        for transition in sorted(self.transition_functions):
            result = str(transition[0]) + "' " + str(transition[1]) + " " + str(transition[2]) + "'"
            print(result)
