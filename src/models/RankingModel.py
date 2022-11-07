import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'ranking.csv').replace('models\\', '')

class RankingModel():
    __instance = None

    @staticmethod
    def get_instance():
        if RankingModel.__instance == None:
            RankingModel()
        return RankingModel.__instance

    def __init__(self):
        if RankingModel.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            RankingModel.__instance = self