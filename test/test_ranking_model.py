import sys
sys.path.insert(0, 'src')

from models.RankingModel import RankingModel

model = RankingModel.get_instance()

def test_get_ranking():
    res = model.get_ranking()
    assert(type(res) == list)


def test_add_ranking():
    model.delete_by_name('Miguel')
    model.add_ranking('Miguel', 1)
    res = model.get_ranking()
    miguel = [x for x in res if x[0] == 'Miguel']
    assert(len(miguel) == 1)
    assert(miguel[0][0] == 'Miguel')
    assert(miguel[0][1] == 1)


def test_update_ranking():
    model.add_ranking('Miguel', 10)
    res = model.get_ranking()
    miguel = [x for x in res if x[0] == 'Miguel']
    assert(len(miguel) == 1)
    assert(miguel[0][0] == 'Miguel')
    assert(miguel[0][1] == 10)


def test_delete_by_name():
    model.add_ranking('Miguel', 10)
    model.delete_by_name('Miguel')
    res = model.get_ranking()
    miguel = [x for x in res if x[0] == 'Miguel']
    assert(len(miguel) == 0)


def test_order():
    model.delete_all()
    model.delete_by_name('Miguel')
    model.delete_by_name('Paco')
    model.add_ranking('Miguel', 10)
    model.add_ranking('Paco', 20)
    res = model.get_ranking()
    assert(res[0][0] == 'Paco')
    assert(res[0][1] == 20)
    assert(res[1][0] == 'Miguel')
    assert(res[1][1] == 10)


def test_delete_all():
    model.add_ranking('Miguel', 10)
    model.add_ranking('Paco', 20)
    model.delete_all()
    res = model.get_ranking()
    assert(len(res) == 0)


def test_singleton():
    try:
        RankingModel()
    except Exception:
        assert(True)


def test_loop_simple():
    # No loop
    model.delete_all()
    model.add_ranking('Miguel', 10)
    assert(len(model.get_ranking()) == 1)

    # 1 Loop
    model.add_ranking('Paco', 20)
    assert(len(model.get_ranking()) == 2)

    # 2 Loops
    model.add_ranking('Juan', 30)
    assert(len(model.get_ranking()) == 3)

    # 3 Loops
    model.add_ranking('Pepe', 40)
    assert(len(model.get_ranking()) == 4)

    # 4 Loops
    model.add_ranking('Jose', 50)
    assert(len(model.get_ranking()) == 5)

    # 1 Loop (Sin aumentar el tamaño)
    model.add_ranking('Jose', 60)
    assert(len(model.get_ranking()) == 5)

    # 2 Loops (Sin aumentar el tamaño)
    model.add_ranking('Pepe', 45)
    assert(len(model.get_ranking()) == 5)

    # 3 Loops (Sin aumentar el tamaño)
    model.add_ranking('Juan', 35)
    assert(len(model.get_ranking()) == 5)

    # 4 Loops (Sin aumentar el tamaño)
    model.add_ranking('Paco', 25)
    assert(len(model.get_ranking()) == 5)

    # 5 Loops (Sin aumentar el tamaño)
    model.add_ranking('Miguel', 15)
    assert(len(model.get_ranking()) == 5)
