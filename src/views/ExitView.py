
class ExitView:

    def show(self, _):
        print("Goodbye!")

    def input(self):
        input('Press any key to exit...')
        return {'controller': 'menu', 'action': 'exit', 'data': {}}