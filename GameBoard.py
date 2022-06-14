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
		board_dict = board_state.board_state_dictionary
		print('\n' * 100)
		print(f"{display_msg}\n" +
			  f"{board_dict['a1']}{self.__board_separator}{board_dict['a2']}{self.__board_separator}{board_dict['a3']}\n" +
			  f"{board_dict['b1']}{self.__board_separator}{board_dict['b2']}{self.__board_separator}{board_dict['b3']}\n" +
			  f"{board_dict['c1']}{self.__board_separator}{board_dict['c2']}{self.__board_separator}{board_dict['c3']}")
		return
