import abc

from BoardState import BoardState

class GameBoard(metaclass=abc.ABCMeta):
	@classmethod
	def __subclasshook__(cls, C):
		if cls is GameBoard:
			if any("__iter__" in B.__dict__ for B in C.__mro__):
				return True
		return NotImplemented

	@abc.abstractmethod
	def print_game_board(self, board_state: BoardState, display_msg: str):
		return

class ConsoleGameBoard(GameBoard):
	__board_separator: str

	def __init__(self):
		self.__board_separator = "|"

	def print_game_board(self, board_state: BoardState, display_msg: str):
		a1 = board_state.get_value_from_board_space('a1')
		a2 = board_state.get_value_from_board_space('a2')
		a3 = board_state.get_value_from_board_space('a3')
		b1 = board_state.get_value_from_board_space('b1')
		b2 = board_state.get_value_from_board_space('b2')
		b3 = board_state.get_value_from_board_space('b3')
		c1 = board_state.get_value_from_board_space('c1')
		c2 = board_state.get_value_from_board_space('c2')
		c3 = board_state.get_value_from_board_space('c3')
		print('\n' * 20)
		print(f"{display_msg}\n" +
			  f"{a1}{self.__board_separator}{a2}{self.__board_separator}{a3}\n" +
			  f"{b1}{self.__board_separator}{b2}{self.__board_separator}{b3}\n" +
			  f"{c1}{self.__board_separator}{c2}{self.__board_separator}{c3}")
		return
