from controllers.Controller import Controller

class MenuController(Controller):

    def __init__(self) -> None:
        self.menu = {
            1: ['Play game', 'game', 'show_difficulty'],
            2: ['Ranking', 'ranking', 'show_ranking'],
            3: ['Exit', 'menu', 'show_exit'],
        }

    def show_menu(self, data = {}):
        return {'view': 'MenuView', 'data': data}

    def show_exit(self, data = {}):
        return {'view': 'ExitView', 'data': data}

    def select_option(self, data):
        try:
            option = int(data['option'])
        except ValueError:
            return {'view': 'MenuView', 'data': {'error': 'Invalid Type'}}
        if option not in self.menu:
            return self.show_menu({'error': 'Invalid option'})
        return self.controllers[self.menu[option][1]].__getattribute__(self.menu[option][2])({})

    def exit(self, _):
        exit()