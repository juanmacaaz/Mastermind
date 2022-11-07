import sys
sys.path.insert(0, 'src')

from models.RankingModel import RankingModel

def test_singleton():
    try:
        RankingModel()
    except Exception:
        assert(True)