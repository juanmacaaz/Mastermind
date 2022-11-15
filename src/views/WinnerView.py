from views.GameView import GameView

class WinnerView:

    def __init__(self):
        self.game_view = GameView()

    def show(self, data):
        print('Congratulations!')
        self.game_view.show(data)
        print('You won!')
        print('Put your name in the ranking')

    def input(self):
        value = input("Your name: ")
        return {'controller': 'ranking',
                'action': 'add_ranking',
                'data': {'name': value}}