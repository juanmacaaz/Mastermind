from controllers.Controller import Controller

class GameController(Controller):
    pass

    def show_difficulty(self, data = {}):
        return {'view': 'DifficultyView', 'data': data}