from controllers.Controller import Controller
from models.RankingModel import RankingModel

class RankingController(Controller):
    
    def __init__(self):
        self.ranking_model = RankingModel.get_instance()

    def show_ranking(self, _):
        ranking = self.ranking_model.get_ranking()
        return {'view': 'RankingView', 'data': ranking}