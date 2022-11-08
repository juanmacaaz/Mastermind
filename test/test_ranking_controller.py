import sys
sys.path.insert(0, 'src')

from controllers.RankingController import RankingController
from controllers.GameController import GameController

controller = RankingController()

# Prova show
def test_show_ranking():
    res = controller.show_ranking(None)
    assert(res['view'] == 'RankingView')