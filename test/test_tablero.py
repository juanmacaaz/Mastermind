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