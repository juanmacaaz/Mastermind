
class RankingView:

    def __init__(self):
        pass

    def show(self, data):
        print('RANKING')
        for user, points in data:
            print(f'{user} - {points}')

    def input(self):
        input('Press any key to go back...')
        return {'controller': 'menu',
                'action': 'show_menu',
                'data': {}}