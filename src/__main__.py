import os

import Pipeline

if __name__ == '__main__':

    views = {}

    pipeline = Pipeline.Pipeline()

    # Load the views from the views folder
    for view in os.listdir('views'):
        if view.endswith('.py'):
            view = view.replace('.py', '')
            exec(f'from views import {view}')
            views[view] = eval(f'{view}.{view}()')

    # Show the initial view
    response = pipeline('menu', 'show_menu', {})

    while True:

        os.system('cls')

        views[response['view']].show(response['data'])
        value = views[response['view']].input()

        response = pipeline(value['controller'],
                            value['action'],
                            {} if len(value) == 1 else value['data'])