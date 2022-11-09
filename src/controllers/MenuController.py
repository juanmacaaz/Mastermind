from controllers.Controller import Controller

class MenuController(Controller):

    def __init__(self) -> None:

        # Menu options [name, controller, method]
        self.menu = {
            1: ['Play game', 'game', 'show_difficulty'],
            2: ['Ranking', 'ranking', 'show_ranking'],
            3: ['Exit', 'menu', 'show_exit'],
        }

    def show_menu(self, data = {}):
        '''
            This method is used to show the menu.

            Keyword arguments:
            data -- Not used

            Returns:
            dict -- The view to show and the data to show
        '''

        return {'view': 'MenuView', 'data': data}

    def show_exit(self, data = {}):
        '''
            This method is used to show the exit message.

            Keyword arguments:
            data -- Not used

            Returns:
            dict -- The view to show and the data to show
        '''

        return {'view': 'ExitView', 'data': data}

    def select_option(self, data):
        '''
            This method is called when the user select an option from the menu.
            It calls the method of the controller selected.
            If the option is not valid, it returns the menu view.

            Keyword arguments:
            data['option'] -- The option selected by the user (int)

            Returns:
            dict -- The view to show and the data to show
        '''

        try:
            option = int(data['option'])
        except ValueError:
            return {'view': 'MenuView', 'data': {'error': 'Invalid Type'}}
        if option not in self.menu:
            return self.show_menu({'error': 'Invalid option'})
        return self.controllers[self.menu[option][1]].__getattribute__(self.menu[option][2])({})

    def exit(self, _):
        '''
            This method is used to exit the game.

            Keyword arguments:
            _ -- Not used
        '''

        exit()