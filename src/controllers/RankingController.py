from controllers.Controller import Controller
from models.RankingModel import RankingModel

class RankingController(Controller):
    '''
        This class is used to manage the ranking.
    '''

    def __init__(self):
        self.ranking_model = RankingModel.get_instance()


    def show_ranking(self, _):
        '''
            This method is used to show the ranking.
            
            Keyword arguments:
            _ -- Not used

            Returns:
            dict -- The view to show and the data to show
        '''
        ranking = self.ranking_model.get_ranking()
        return {'view': 'RankingView', 'data': ranking}
    

    def add_ranking(self, data):
        '''
            Add a new player-poins to the ranking.
            Only permit alphanumeric characters.
            The score is calculated with this formula: 
                intents * (difficulty + 1)

            Keyword arguments:
            data['name'] -- The name of the player (string)

            Returns:
            dict -- The view to show and the data to show
        '''

        # Check alphanumerical characters
        if not data['name'].isalnum():
            return {'view': 'WinnerView',
                    'data': self.ranking_model.get_ranking(),
                    'error': 'El nombre debe ser alfanumerico'}
        intentos = self.controllers['game'].get_n_intentos()
        dificultad = self.controllers['game'].get_difficulty()
        score = intentos * (dificultad + 1)
        self.ranking_model.add_ranking(data['name'], score)
        return {'view': 'MenuView', 'data': {}}
