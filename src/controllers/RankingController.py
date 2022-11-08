from controllers.Controller import Controller
from models.RankingModel import RankingModel

class RankingController(Controller):
    
    def __init__(self):
        self.ranking_model = RankingModel.get_instance()

    def show_ranking(self, _):
        ranking = self.ranking_model.get_ranking()
        return {'view': 'RankingView', 'data': ranking}
    
    def add_ranking(self, data):
        # Check alphanumerical
        if not data['name'].isalnum():
            return {'view': 'WinnerView',
                    'data': self.ranking_model.get_ranking(),
                    'error': 'El nombre debe ser alfanumerico'}
        intentos = self.controllers['game'].get_n_intentos()
        dificultad = self.controllers['game'].get_difficulty()
        score = intentos * (dificultad + 1)
        self.ranking_model.add_ranking(data['name'], score)
        return {'view': 'MenuView', 'data': {}}
