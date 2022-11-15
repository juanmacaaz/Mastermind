
class GameView:

    def __init__(self):
        
        self.color_map = {
            1: ['\033[91m', 'R'], # red
            2: ['\033[92m', 'G'], # green
            3: ['\033[94m', 'B'], # blue
            4: ['\033[96m', 'C'], # cyan
            5: ['\033[97m', 'W'], # white
            6: ['\033[93m', 'Y'], # yellow
            7: ['\033[95m', 'M'], # magenta
            8: ['\033[90m', 'G'], # grey
            9: ['\033[90m', 'B'], # black
        }

    def show(self, data):
        print('Colores validos: ', end='')
        for i in range(1, data['colors'] + 1):
            print(f'{self.color_map[i][0]}{self.color_map[i][1]}\033[0m', end=' ')
        print()

        print('\033[91m Tablero \033[0m')
        for row, res in zip(data['tablero'], data['results']):
            for column in row:
                print(self.color_map[int(column)][0] + '■' + '\033[0m', end=' ')
            print(' ', end='')
            for column in res:
                if column == 0:
                    print('\033[90m■\033[0m', end=' ')
                elif column == 1:
                    print('\033[93m■\033[0m', end=' ')
                elif column == 2:
                    print('\033[92m■\033[0m', end=' ')
            print()

        for _ in range(data['rows'] - len(data['tablero'])):
            for _ in range(data['columns']):
                print('■', end=' ')
            print(' ', end='')
            for _ in range(data['columns']):
                print('■', end=' ')
            print()
        if 'error' in data:
            print(f'Error: {data["error"]}')

    def input(self):
        data = input('Escribe la combinacion: ')
        return {'controller': 'game',
                'action': 'add_combination',
                'data': {'combination': data}}