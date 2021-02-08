class LSystem:
    def __init__(self, initial_state, possible_states, productions):
        self.initial_instance = initial_state
        self.possible_states = possible_states
        self.productions = productions
        self.current_instance = self.initial_instance
        self.all_instances = [self.initial_instance]

    def replace_state(self, state):
        return self.productions[state]

    def replace_instance(self, instance):
        new_instance = ''

        for state in instance:
            if state in self.possible_states:
                new_instance = new_instance + self.replace_state(state)
            else:
                new_instance = new_instance + state

        self.update_instance(new_instance)

    def update_instance(self, new_instance):
        self.current_instance = new_instance
        self.all_instances.append(new_instance)

    def next_instance(self):
        self.replace_instance(self.current_instance)

    def run_steps(self, number_of_steps):
        for i in range(number_of_steps):
            self.next_instance()