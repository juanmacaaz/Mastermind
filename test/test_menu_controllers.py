import sys
import itertools
import random

sys.path.insert(0, 'src')

import controllers.GameController as c
from controllers.Tablero import Tablero

def test_game_controller_difficulty():
    controller = c.GameController()
    
    # Particiones equivalentes <-No valido --- 0 --- Valido --- 2 --- No valido->
    # Valido
    out = controller.set_difficulty({'difficulty': '1'})
    assert(out['view'] == 'GameView')

    # No valido por ser mayor que 3
    out = controller.set_difficulty({'difficulty': '4'})
    assert(out['view'] == 'DifficultyView')
    assert('error' in out['data'])

    # No valido por ser menor que 0
    out = controller.set_difficulty({'difficulty': '-1'})
    assert(out['view'] == 'DifficultyView')
    assert('error' in out['data'])

    # Valores limites y frontera
    out = controller.set_difficulty({'difficulty': '1'})
    assert(out['view'] == 'GameView')

    out = controller.set_difficulty({'difficulty': '3'})
    assert(out['view'] == 'GameView')


def test_color_comprobation():
    controller = c.GameController()
    # Caso difficulty = 1
    controller.set_difficulty({'difficulty': '1'})
    correct_combination = [1, 2, 3]
    incorrect_combination = [1, 5, 6]
    # Caso correcto
    correct_res = controller.color_comprobation(correct_combination)
    assert(correct_res == None)
    # Caso incorrecto
    incorrect_res = controller.color_comprobation(incorrect_combination)
    assert(incorrect_res != None)
    
    # Caso difficulty = 2
    controller.set_difficulty({'difficulty': '2'})
    correct_combination = [1, 2, 3, 4, 5]
    incorrect_combination = [1, 5, 6, 7, 1024]
    # Caso correcto
    correct_res = controller.color_comprobation(correct_combination)
    assert(correct_res == None)
    # Caso incorrecto
    incorrect_res = controller.color_comprobation(incorrect_combination)
    assert(incorrect_res != None)
    
    # Caso difficulty = 3
    controller.set_difficulty({'difficulty': '3'})
    correct_combination = [1, 2, 3, 4, 5, 6, 7]
    incorrect_combination = [1, 5, 6, 7, 1024, 1021, 0]
    # Caso correcto
    correct_res = controller.color_comprobation(correct_combination)
    assert(correct_res == None)
    # Caso incorrecto
    incorrect_res = controller.color_comprobation(incorrect_combination)
    assert(incorrect_res != None)


def test_len_comprobation():
    controller = c.GameController()
    # Caso difficulty = 1
    controller.set_difficulty({'difficulty': '1'})
    correct_combination = [1, 2, 3]
    incorrect_combination = [1, 2, 3, 3]
    # Caso correcto
    correct_res = controller.len_comprobation(correct_combination)
    assert(correct_res == None)
    # Caso incorrecto
    incorrect_res = controller.len_comprobation(incorrect_combination)
    assert(incorrect_res != None)

    # Caso difficulty = 2
    controller.set_difficulty({'difficulty': '2'})
    correct_combination = [1, 2, 3, 4, 5]
    incorrect_combination = [1, 2, 3, 4, 5, 5]
    # Caso correcto
    correct_res = controller.len_comprobation(correct_combination)
    assert(correct_res == None)
    # Caso incorrecto
    incorrect_res = controller.len_comprobation(incorrect_combination)
    assert(incorrect_res != None)

    # Caso difficulty = 3
    controller.set_difficulty({'difficulty': '3'})
    correct_combination = [1, 2, 3, 4, 5, 6, 7]
    incorrect_combination = [1]
    # Caso correcto
    correct_res = controller.len_comprobation(correct_combination)
    assert(correct_res == None)
    # Caso incorrecto
    incorrect_res = controller.len_comprobation(incorrect_combination)
    assert(incorrect_res != None)

def test_parse_input():
    controller = c.GameController()

    # Caso difficulty = 1
    controller.set_difficulty({'difficulty': '1'})
    correct_combination = 'RGB'
    incorrect_combination = ''
    # Caso correcto
    correct_res = controller.parse_input(correct_combination)
    assert(correct_res != None)
    # Caso incorrecto
    incorrect_res = controller.parse_input(incorrect_combination)
    assert(incorrect_res == None)
    
    # Caso difficulty = 2
    controller.set_difficulty({'difficulty': '2'})
    correct_combination = 'RGBBB'
    incorrect_combination = 'AGAASFGASGSH'
    # Caso correcto
    correct_res = controller.parse_input(correct_combination)
    assert(correct_res != None)
    # Caso incorrecto
    incorrect_res = controller.parse_input(incorrect_combination)
    assert(incorrect_res == None)

    # Caso difficulty = 3
    controller.set_difficulty({'difficulty': '3'})
    correct_combination = 'RGBBBBB'
    incorrect_combination = 'AGAASASDSGGASGFGASGSH'
    # Caso correcto
    correct_res = controller.parse_input(correct_combination)
    assert(correct_res != None)
    # Caso incorrecto
    incorrect_res = controller.parse_input(incorrect_combination)
    assert(incorrect_res == None)

def test_add_combination_invalid_values_lv1():
    
    invalid_values = [
        ({'combination': ''}, 'Invalid combination'),
        ({'combination': 'R'}, 'Invalid len'),
        ({'combination': 'RR'}, 'Invalid len'),
        ({'combination': 'RRZ'}, 'Invalid combination'),
        ({'combination': 'RRRR'}, 'Invalid len'),
        ({'combination': 'RRM'}, 'Invalid color'),
    ]

    controller = c.GameController()
    controller.set_difficulty({'difficulty': '1'})
    
    for combination, error in invalid_values:
        res = controller.add_combination(combination)
        assert(res['data']['error'] == error)


def test_add_combination_invalid_values_lv2():
    
    invalid_values = [
        ({'combination': ''}, 'Invalid combination'),
        ({'combination': 'R'}, 'Invalid len'),
        ({'combination': 'RR'}, 'Invalid len'),
        ({'combination': 'RRR'}, 'Invalid len'),
        ({'combination': 'RRRR'}, 'Invalid len'),
        ({'combination': 'RRRRM'}, 'Invalid color'),
        ({'combination': 'RRRRRR'}, 'Invalid len'),
        ({'combination': 'ZZZZZZZ'}, 'Invalid combination'),
    ]

    controller = c.GameController()
    controller.set_difficulty({'difficulty': '2'})
    
    for combination, error in invalid_values:
        res = controller.add_combination(combination)
        assert(res['data']['error'] == error)

def test_add_combination_invalid_values_lv3():

    invalid_values = [
        ({'combination': ''}, 'Invalid combination'),
        ({'combination': 'R'}, 'Invalid len'),
        ({'combination': 'RR'}, 'Invalid len'),
        ({'combination': 'RRR'}, 'Invalid len'),
        ({'combination': 'RRRR'}, 'Invalid len'),
        ({'combination': 'RRRRR'}, 'Invalid len'),
        ({'combination': 'ZZZZZZZ'}, 'Invalid combination'),
        ({'combination': 'RRRRRRRR'}, 'Invalid len'),
    ]

    controller = c.GameController()
    controller.set_difficulty({'difficulty': '3'})
    
    for combination, error in invalid_values:
        res = controller.add_combination(combination)
        assert(res['data']['error'] == error)


def pairwise_testing(posible_values, number_of_variables):
        random.seed(42)
        
        combinations = list(itertools.product(
            *[posible_values for _ in range(number_of_variables)]
        ))

        pair_test = []
        i = 0

        while i < len(combinations):
            v = random.randint(0, len(posible_values))
            pair_test.append(combinations[i+v])
            i += len(posible_values)

        return pair_test


def test_add_combinations_pairwise_valid_input_lv1():
    controller = c.GameController()
    
    for combination in pairwise_testing([1, 2, 3, 4, 5], 3):
        controller.set_difficulty({'difficulty': '1'})
        data = {'combination':combination}
        res = controller.add_combination(data)
        assert(res['view'] == 'GameView')
        assert('error' not in res)


def test_add_combinations_pairwise_valid_input_lv2():
    controller = c.GameController()
    
    for combination in pairwise_testing([1, 2, 3, 4, 5, 6, 7], 3):
        controller.set_difficulty({'difficulty': '2'})
        data = {'combination':combination}
        res = controller.add_combination(data)
        assert(res['view'] == 'GameView')
        assert('error' not in res)


def test_add_combinations_pairwise_valid_input_lv3():
    controller = c.GameController()
    
    for combination in pairwise_testing([1, 2, 3, 4, 5, 6, 7], 4):
        controller.set_difficulty({'difficulty': '3'})
        data = {'combination':combination}
        res = controller.add_combination(data)
        assert(res['view'] == 'GameView')
        assert('error' not in res)

def test_show_dificulty():
    controller = c.GameController()
    controller.set_difficulty({'difficulty': '1'})
    res = controller.show_difficulty()
    assert(res['view'] == 'DifficultyView')

def test_win_game_lv1(mocker):
    controller = c.GameController()
    # Mock de la funcion check_win
    controller.tablero.check_winner = mocker.MagicMock(return_value=True)
    controller.set_difficulty({'difficulty': '1'})
    res = controller.add_combination({'combination': 'RGB'})
    assert(res['view'] == 'WinnerView')
    
def test_loss_game_lv1(mocker):
    controller = c.GameController()
    # Mock de la funcion check_win
    controller.tablero.check_winner = mocker.MagicMock(return_value=False)
    controller.set_difficulty({'difficulty': '1'})
    for _ in range(5):
        res = controller.add_combination({'combination': 'RGB'})
    assert(res['view'] == 'GameOverView')


def test_get_difficulty():
    controller = c.GameController()
    controller.set_difficulty({'difficulty': '1'})
    res = controller.get_difficulty()
    assert(res == 1)

def test_get_n_intentos():
    n_intentos = [5, 5, 7]

    for i, n in enumerate(n_intentos):
        controller = c.GameController()
        controller.set_difficulty({'difficulty': str(i+1)})
        res = controller.get_n_intentos()
        assert(res == n)