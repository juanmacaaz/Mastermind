import sys
sys.path.insert(0, 'src')

from controllers.MenuController import MenuController


def init_menu_controller():
    menu = MenuController()
    menu.set_controllers(
        {
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