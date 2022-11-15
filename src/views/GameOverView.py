from views.GameView import GameView

class GameOverView:
    
    def __init__(self):
        self.game_view = GameView()

    def show(self, _):
        self.game_view.show(_)
        print("You lose!")

    def input(self):
        input('Press any key to go back...')
        return {'controller': 'menu',
                'action': 'show_menu',
                'data': {}}