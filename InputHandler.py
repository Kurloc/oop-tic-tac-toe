import abc
from typing import List


class GameInputHandler(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, C):
        if cls is GameInputHandler:
            if any("__iter__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented

    @abc.abstractmethod
    def play_turn(self, taken_map_placements: List[str]) -> str:  # returns position. Ex: a1
        return ''

class ConsoleGameInputHandler(GameInputHandler):
    __valid_map_placements: List[str]

    def __init__(self, valid_map_placements: List[str]):
        self.__valid_map_placements = list(valid_map_placements)

    def play_turn(self, taken_map_placements: List[str]) -> str:
        running = True
        result = []
        for valid_placement in self.__valid_map_placements:
            add = True
            for placement in taken_map_placements:
                if valid_placement is placement:
                    add = False
                    break
            if add:
                result.append(valid_placement)

        print('Valid moves: ')
        print(', '.join(result))
        while running:
            val = input('\nEnter your value: ')
            if val in self.__valid_map_placements:
                if len(taken_map_placements) == 0:
                    return val
                elif val not in taken_map_placements:
                    return val
