import sys
sys.path.insert(0, 'src')

from controllers.Tablero import Tablero

def test_create_tablero():

    # Dificultad 1
    tablero = Tablero()
    tablero.set_difficulty(1)
    tablero.create_tablero()
    assert(tablero.get_columns() == 3)
    assert(tablero.get_rows() == 5)
    assert(tablero.get_num_colors() == 5)

    # Dificultad 2
    tablero = Tablero()
    tablero.set_difficulty(2)
    tablero.create_tablero()
    assert(tablero.get_columns() == 5)
    assert(tablero.get_rows() == 5)
    assert(tablero.get_num_colors() == 6)

    # Dificultad 3
    tablero = Tablero()
    tablero.set_difficulty(3)
    tablero.create_tablero()
    assert(tablero.get_columns() == 7)
    assert(tablero.get_rows() == 7)
    assert(tablero.get_num_colors() == 7)

def test_generate_sequence_lv1():
    tablero = Tablero()
    tablero.set_difficulty(1)
    tablero.create_tablero()
    tablero.generate_sequence()
    assert(len(tablero.sequence) == 3)
    assert(all([x in range(1, 6) for x in tablero.sequence]))

def test_generate_sequence_lv2():
    tablero = Tablero()
    tablero.set_difficulty(2)
    tablero.create_tablero()
    tablero.generate_sequence()
    assert(len(tablero.sequence) == 5)
    assert(all([x in range(1, 7) for x in tablero.sequence]))

def test_generate_sequence_lv3():
    tablero = Tablero()
    tablero.set_difficulty(3)
    tablero.create_tablero()
    tablero.generate_sequence()
    assert(len(tablero.sequence) == 7)
    assert(all([x in range(1, 8) for x in tablero.sequence]))

def test_check_combination_lv1():
    tablero = Tablero()
    tablero.set_difficulty(1)
    tablero.create_tablero()

    tablero.sequence = [1, 2, 3]
    assert(tablero.check_combination([1, 2, 3]) == [2, 2, 2])
    assert(tablero.check_combination([1, 2, 4]) == [2, 2, 0])
    assert(tablero.check_combination([1, 4, 3]) == [2, 0, 2])
    assert(tablero.check_combination([4, 2, 3]) == [0, 2, 2])
    assert(tablero.check_combination([4, 4, 3]) == [0, 0, 2])
    assert(tablero.check_combination([4, 4, 4]) == [0, 0, 0])
    assert(tablero.check_combination([4, 1, 4]) == [0, 1, 0])
    assert(tablero.check_combination([4, 1, 1]) == [0, 1, 1])
    assert(tablero.check_combination([2, 3, 1]) == [1, 1, 1])
    assert(tablero.check_combination([2, 3, 4]) == [1, 1, 0])

def test_check_combination_lv2():
    tablero = Tablero()
    tablero.set_difficulty(2)
    tablero.create_tablero()

    tablero.sequence = [1, 2, 3, 4, 5]
    assert(tablero.check_combination([1, 2, 3, 4, 5]) == [2, 2, 2, 2, 2])
    assert(tablero.check_combination([1, 2, 3, 4, 1]) == [2, 2, 2, 2, 1])
    assert(tablero.check_combination([1, 2, 3, 1, 5]) == [2, 2, 2, 1, 2])
    assert(tablero.check_combination([1, 2, 1, 4, 5]) == [2, 2, 1, 2, 2])
    assert(tablero.check_combination([1, 1, 3, 4, 5]) == [2, 1, 2, 2, 2])
    assert(tablero.check_combination([1, 1, 3, 4, 1]) == [2, 1, 2, 2, 1])
    assert(tablero.check_combination([1, 1, 3, 1, 5]) == [2, 1, 2, 1, 2])
    assert(tablero.check_combination([1, 1, 1, 4, 5]) == [2, 1, 1, 2, 2])
    assert(tablero.check_combination([1, 1, 1, 4, 1]) == [2, 1, 1, 2, 1])
    assert(tablero.check_combination([1, 1, 1, 1, 5]) == [2, 1, 1, 1, 2])
    assert(tablero.check_combination([1, 1, 1, 1, 1]) == [2, 1, 1, 1, 1])
    assert(tablero.check_combination([2, 3, 4, 5, 1]) == [1, 1, 1, 1, 1])
    assert(tablero.check_combination([6, 3, 4, 1, 5]) == [0, 1, 1, 1, 2])
    assert(tablero.check_combination([6, 6, 6, 6, 6]) == [0, 0, 0, 0, 0])

def test_check_combination_lv3():
    tablero = Tablero()
    tablero.set_difficulty(3)
    tablero.create_tablero()

    tablero.sequence = [1, 2, 3, 4, 5, 6, 6]
    assert(tablero.check_combination([1, 2, 3, 4, 5, 6, 6]) == [2, 2, 2, 2, 2, 2, 2])
    assert(tablero.check_combination([1, 2, 3, 4, 5, 6, 1]) == [2, 2, 2, 2, 2, 2, 1])
    assert(tablero.check_combination([1, 2, 3, 4, 5, 1, 6]) == [2, 2, 2, 2, 2, 1, 2])
    assert(tablero.check_combination([1, 2, 3, 4, 1, 6, 7]) == [2, 2, 2, 2, 1, 2, 0])
    assert(tablero.check_combination([1, 2, 3, 1, 5, 6, 7]) == [2, 2, 2, 1, 2, 2, 0])
    assert(tablero.check_combination([7, 2, 1, 4, 5, 6, 7]) == [0, 2, 1, 2, 2, 2, 0])
    assert(tablero.check_combination([7, 7, 7, 7, 7, 7, 7]) == [0, 0, 0, 0, 0, 0, 0])

def test_check_winner():
    tablero = Tablero()
    tablero.set_difficulty(3)
    tablero.create_tablero()

    tablero.sequence = [1, 2, 3, 4, 5, 6, 6]
    tablero.add_combination([1, 2, 3, 4, 5, 6, 6])
    assert(tablero.check_winner() == True)

    tablero.sequence = [1, 2, 3, 4, 5, 6, 6]
    tablero.add_combination([1, 2, 3, 4, 5, 6, 1])
    assert(tablero.check_winner() == False)