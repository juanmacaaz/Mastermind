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