import random

class Tablero:
    
    def __init__(self):
        self.DIFFICULTY_MODES = {
            1: {'rows': 5,  'columns': 3, 'colors': 5},
            2: {'rows': 5,  'columns': 5, 'colors': 6},
            3: {'rows': 7,  'columns': 7, 'colors': 7},
        }
        
    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def create_tablero(self):
        '''Create a tablero with the difficulty selected'''
        self.num_rows    = self.DIFFICULTY_MODES[self.difficulty]['rows']
        self.num_columns = self.DIFFICULTY_MODES[self.difficulty]['columns']
        self.num_colors  = self.DIFFICULTY_MODES[self.difficulty]['colors']

        '''creation of the tablero'''
        self.tablero = []
        self.results = []
    
    def generate_sequence(self):
        '''Generate a sequence of colors'''
        self.sequence = []
        for _ in range(self.num_columns):
            self.sequence.append(random.randint(1, self.num_colors))

    def add_combination(self, combination):
        '''Add a combination to the tablero'''
        self.tablero.append(combination)
        self.results.append(self.check_combination(combination))

    def check_combination(self, combination):
        '''Check if the combination is correct'''
        comparation = []
        for a, b in zip(self.sequence, combination):
            value = 0
            if b in self.sequence:
                value = 1
            if a == b:
                value = 2
            comparation.append(value)
        return comparation

    def check_winner(self):
        return self.sequence == self.tablero[-1]

    def get_tablero(self):
        return self.tablero

    def get_results(self):
        return self.results

    def get_rows(self):
        return self.num_rows

    def get_columns(self):
        return self.num_columns

    def get_num_colors(self):
        return self.num_colors