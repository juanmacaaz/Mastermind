import csv
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'ranking.csv').replace('models\\', '')

class RankingModel():
    '''
        Singleton implementation of the class RankingModel.
        Controls the access to the file ranking.csv
    '''
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

    def get_ranking(self):
        '''
            Returns the ranking from the file ordered by score
        '''
        ranking = []
        with open(DATA_DIR, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                ranking.append(row)

        # Sort the ranking
        ranking.sort(key=lambda x: int(x[1]), reverse=True)
        ranking = list(map(lambda x: [x[0], int(x[1])], ranking))
        return ranking

    def add_ranking(self, name, score):
        '''
        Adds a new ranking to the ranking file
        If the user is already in the ranking, it updates the score
        '''
        ranking = self.get_ranking()
        # Check if the user is already in the ranking
        for i in range(len(ranking)):
            if ranking[i][0] == name:
                if score > ranking[i][1]:
                    ranking[i][1] = score
                break
        else:
            ranking.append([name, score])
        # Sort the ranking
        ranking.sort(key=lambda x: int(x[1]), reverse=True)
        # Write the ranking to the file
        with open(DATA_DIR, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(ranking)
        

    def delete_by_name(self, name):
        '''
            Deletes the ranking of the player with the name passed as parameter
        '''
        ranking = self.get_ranking()
        ranking = list(filter(lambda x: x[0] != name, ranking))
        # Write the ranking to the file
        with open(DATA_DIR, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(ranking)


    def delete_all(self):
        '''
            Deletes all the ranking
        '''
        with open(DATA_DIR, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows([])
            
