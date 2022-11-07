import sys
sys.path.insert(0, 'src')

from models.RankingModel import RankingModel

model = RankingModel.get_instance()

def test_singleton():
    try:
        RankingModel()
    except Exception:
        assert(True)

def test_add_ranking():
    model.delete_all()
    model.add_ranking('Miguel', 1)
    res = model.get_ranking()
    miguel = [x for x in res if x[0] == 'Miguel']
    assert(len(miguel) == 1)
    assert(miguel[0][0] == 'Miguel')
    assert(miguel[0][1] == 1)


def test_delete_all():
    model.add_ranking('Miguel', 10)
    model.add_ranking('Paco', 20)
    model.delete_all()
    res = model.get_ranking()
    assert(len(res) == 0)


def test_get_ranking():
    model.delete_all()
    model.add_ranking('Miguel', 10)
    res = model.get_ranking()
    assert(type(res) == list)
    assert(res[0][0] == 'Miguel')
    assert(res[0][1] == 10)
    