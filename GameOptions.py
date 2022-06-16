import abc

from InputHandler import ConsoleGameInputHandler, DummyAiGameInputHandler


class GameOption(metaclass=abc.ABCMeta):
	game_base: object  # GameBase

	@abc.abstractmethod
	#                             GameBase
	def __init__(self, game_base: object):
		self.game_base = game_base

	@abc.abstractmethod
	def get_value(self) -> str:
		return ''

	@abc.abstractmethod
	def back_action(self):
		return

	@abc.abstractmethod
	def next_action(self, selection: int):
		return


class PlayerSetupMenuOption(GameOption):
	#                             GameBase
	def __init__(self, game_base: object):
		super().__init__(game_base)

	def get_value(self):
		return '\t1.Player vs Player\n\t2.Player vs AI.\n\nEnter 0 to go back.'

	def back_action(self):
		return GameMenuOption(self.game_base)

	def next_action(self, selection: int):
		if selection == 0:
			return self.back_action()
		elif selection == 1:
			self.game_base.game_input_handler_player_one = ConsoleGameInputHandler(
				self.game_base.get_valid_map_placements())
			self.game_base.game_input_handler_player_two = ConsoleGameInputHandler(
				self.game_base.get_valid_map_placements())
			self.game_base.game_loop()
			return
		elif selection == 2:
			self.game_base.game_input_handler_player_one = ConsoleGameInputHandler(
				self.game_base.get_valid_map_placements())
			self.game_base.game_input_handler_player_two = DummyAiGameInputHandler(
				self.game_base.get_valid_map_placements())
			self.game_base.game_loop()
			return 2


class GameMenuOption(GameOption):
	#                            GameBase
	def __init__(self, game_base: object):
		super().__init__(game_base)

	def get_value(self):
		return '\t1.Play a game.\n\t2.Set Player Names\n\nEnter 0 to exit the game.'

	def back_action(self):
		self.game_base.game_options_running = False
		return

	def next_action(self, selection: int):
		if selection == 0:
			return self.back_action()
		elif selection == 1:
			return PlayerSetupMenuOption(self.game_base)
		elif selection == 2:
			return
