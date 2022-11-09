from controllers.Controller import Controller
from controllers.Tablero import Tablero

class GameController(Controller):
    '''
        This class is used to manage the game.
    '''

    def __init__(self):
        self.tablero = Tablero()
        self.difficulty = -1

        '''
            Dictionary used to map the colors to the characters.
        '''
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
        '''
            Show the difficulty view.

            Keyword arguments:
            data -- dictionary with the data to show in the view.

            Returns:
            dictionary with the view (DifficultyView) and the data to show.
        '''

        return {'view': 'DifficultyView', 'data': data}
 
 
    def set_difficulty(self, data):
        '''
            Set the difficulty of the game and initialize the tablero.
            If the difficulty is not valid, it will return the difficulty view.

            Keyword arguments:
            data['difficulty'] -- String with the difficulty of the game.

            Returns:
            dictionary with the view (GameView or DifficultyView) and the data to show.
        '''
        
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
        '''
            Check if the combination has valid colors.
            If the combination has valid colors, it will return None.

            Keyword arguments:
            combination -- list with the combination.

            Returns:
            dictionary with the view (GameView) and the data to show.
        '''


        values_color = { 1: 5, 2: 6, 3: 7 }
        for i in combination:
            if i > values_color[self.difficulty] or i < 1:
                return {
                    'view': 'GameView',
                    'data': self.get_data_tablero() | {'error': 'Invalid color'}
                }
        return None


    def len_comprobation(self,combination):
        '''
            Check if the combination has the correct length.
            If the combination has the correct length, it will return None.

            Keyword arguments:
            combination -- list with the combination.

            Returns:
            dictionary with the view (GameView) and the data to show.
        '''

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
        '''
            Add a combination to the tablero.
            If the combination is valid, it will return the game view.
            If the combination is not valid, it will return the game view with the error.
            If the player has lost, it will return the game over view.
            If the player has won, it will return the game won view.

            Keyword arguments:
            data['combination'] -- String with the combination.

            Returns:
            dictionary with the view (GameView, GameOverView or GameWonView) and the data to show.

        '''

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
        '''
            Parse the input to a list of integers.

            Keyword arguments:
            data -- String with the combination.

            Returns:
            list with the combination.
        '''

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
        '''
            Get the data of the tablero.
            This data is used to show the tablero in the view (GameView).

            Returns:
            dictionary with the data of the tablero.
        '''

        
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
