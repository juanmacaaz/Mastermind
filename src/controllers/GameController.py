from controllers.Controller import Controller
from controllers.Tablero import Tablero

class GameController(Controller):

    def __init__(self):
        self.tablero = Tablero()
        self.difficulty = -1

        self.color_char_map = {
            'R': 1,
            'G': 2,
            'B': 3,
            'C': 4,
            'W': 5,
            'Y': 6,
            'M': 7,
        }


    def show_difficulty(self, data = {}):
        return {'view': 'DifficultyView', 'data': data}
 
 
    def set_difficulty(self, data):
        
        if data['difficulty'] not in ['1', '2', '3']:
            return {'view': 'DifficultyView', 'data': {'error': 'Invalid difficulty'}}

        self.difficulty = int(data['difficulty'])

        # Inicializamos el tablero si la dificultad es valida

        self.tablero.set_difficulty(self.difficulty)
        self.tablero.create_tablero()
        self.tablero.generate_sequence()

        return {'view': 'GameView',
                'data': self.get_data_tablero()}


    def color_comprobation(self, combination):
        values_color = { 1: 5, 2: 6, 3: 7 }
        for i in combination:
            if i > values_color[self.difficulty] or i < 1:
                return {
                    'view': 'GameView',
                    'data': self.get_data_tablero() | {'error': 'Invalid color'}
                }
        return None


    def len_comprobation(self,combination):
        values_len = {
            1: 3,
            2: 5,
            3: 7
        }
        if values_len[self.difficulty] != len(combination):
            return {
                'view': 'GameView',
                'data': self.get_data_tablero() | {'error': 'Invalid len'}
            }
        return None
        

    def add_combination(self, data):
        
        data['combination'] = self.parse_input(data['combination'])
        if data['combination'] is None:
            return {'view': 'GameView',
                    'data': self.get_data_tablero() | {'error': 'Invalid combination'}
                    }

        valid = self.len_comprobation(data['combination'])
        if valid != None: return valid
        
        valid = self.color_comprobation(data['combination'])
        if valid != None: return valid

        self.tablero.add_combination(data['combination'])

        # Winner
        if self.tablero.check_winner():
            return {'view': 'WinnerView',
                    'data': self.get_data_tablero()}

        # Lose
        if self.tablero.get_rows() == len(self.tablero.get_tablero()):
            return {'view': 'GameOverView',
                    'data': self.get_data_tablero()}

        # Default
        return {'view': 'GameView',
                'data': self.get_data_tablero()}


    def parse_input(self, data):
        if type(data) is not str:
            return None

        data = list(data.upper())
        numbers = []
        for letter in data:
            if letter not in self.color_char_map:
                return None
            numbers.append(self.color_char_map[letter])
        return numbers if len(numbers) > 0 else None


    def get_data_tablero(self):
        tablero = self.tablero.get_tablero()
        rows = self.tablero.get_rows()
        columns = self.tablero.get_columns()
        results = self.tablero.get_results()
        colors = self.tablero.get_num_colors()
        return {
                'tablero': tablero,
                'rows': rows,
                'columns': columns, 
                'results': results,
                'colors': colors,
                }

    def get_n_intentos(self):
        return self.tablero.get_rows()

    def get_difficulty(self):
        return self.difficulty
