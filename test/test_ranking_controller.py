import sys
sys.path.insert(0, 'src')

from controllers.RankingController import RankingController
from controllers.GameController import GameController

controller = RankingController()

# Prova show
def test_show_ranking():
    res = controller.show_ranking(None)
    assert(res['view'] == 'RankingView')

# Prova add ranking
def test_add_ranking(mocker):
    game_controller = GameController()
    game_controller.get_n_intentos = mocker.MagicMock(return_value=4)
    game_controller.get_difficulty = mocker.MagicMock(return_value=1)

    controller.set_controllers({'game': game_controller})
    controller.ranking_model.delete_by_name('Miguel')
    res_ = controller.add_ranking({'name': 'Miguel'})
    res = controller.ranking_model.get_ranking()
    miguel = [x for x in res if x[0] == 'Miguel']

    assert(len(miguel) == 1)
    assert(miguel[0][1] == 8)
    assert(res_['view'] == 'MenuView')


def test_add_not_alphanumerical_ranking(mocker):
    game_controller = GameController()
    game_controller.get_n_intentos = mocker.MagicMock(return_value=4)
    game_controller.get_difficulty = mocker.MagicMock(return_value=1)

    controller.set_controllers({'game': game_controller})
    controller.ranking_model.delete_all()
    res_ = controller.add_ranking({'name': ' Mi;guel*"\''})
    # Get ranking
    res = controller.ranking_model.get_ranking()
    # Find Miguel in ranking
    miguel = [x for x in res if x[0] == ' Mi;guel*"\'']
    # Check if Miguel is in ranking
    assert(len(miguel) == 0)
    assert(res_['view'] == 'WinnerView')