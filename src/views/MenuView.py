class MenuView():

    def __init__(self):
        self.menu = {
            '1': ['Play game', 'game', 'show_difficulty'],
            '2': ['Ranking', 'ranking', 'show_ranking'],
            '3': ['Exit', 'menu', 'show_exit'],
        }

    def show(self, data):
        print('\033[91m Menu \033[0m')
        for key, value in self.menu.items():
            print(f'{key} - {value[0]}')
        if 'error' in data:
            print(f'\033[91m Error: {data["error"]} \033[0m')
    
    def input(self):
        value = input("Input value (1, 2, 3): ")
        return {'controller': 'menu',
                'action': 'select_option',
                'data': {'option': value}}