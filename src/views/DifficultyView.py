
class DifficultyView:

    def show(self, _):
        print('\033[91m Difficulty \033[0m')
        print('1 - Easy')
        print('2 - Medium')
        print('3 - Hard')

    def input(self):
        value = input("Input value: ")
        return {'controller': 'game',
                'action': 'set_difficulty',
                'data': {'difficulty': value}}