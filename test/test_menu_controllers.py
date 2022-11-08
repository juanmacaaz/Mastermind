import sys
sys.path.insert(0, 'src')

from controllers.GameController import GameController
from controllers.MenuController import MenuController
from controllers.RankingController import RankingController


def init_menu_controller():
    menu = MenuController()
    menu.set_controllers(
        {
            'game': GameController(),
            'ranking': RankingController(),
            'menu': menu
        })
    return menu

menu = init_menu_controller()

def test_show_menu():
    res = menu.show_menu()
    assert(res['view'] == 'MenuView')

def test_show_exit():
    res = menu.show_exit()
    assert(res['view'] == 'ExitView')

def test_exit():
    try:
        menu.exit({})
    except SystemExit:
        assert(True)

def test_menu_input():
    res = menu.select_option({'option': 1})
    assert(res['view'] == 'DifficultyView')

    res = menu.select_option({'option': 2})
    assert(res['view'] == 'RankingView')

    res = menu.select_option({'option': 3})
    assert(res['view'] == 'ExitView')

    res = menu.select_option({'option': 4})
    assert(res['view'] == 'MenuView')
    assert(res['data']['error'] == 'Invalid option')

    res = menu.select_option({'option': 'a'})
    assert(res['view'] == 'MenuView')
    assert(res['data']['error'] == 'Invalid Type')
