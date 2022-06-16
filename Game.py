import abc
import time
from typing import Union

from GameBoard import GameBoard, ConsoleGameBoard
from GameOptions import GameMenuOption
from GameState import GameState
from InputHandler import GameInputHandler
from GameOptions import GameOption

class GameBase(metaclass=abc.ABCMeta):
	game_running: bool
	game_state: GameState
	game_board: GameBoard
	game_input_handler_player_one: GameInputHandler
	game_input_handler_player_two: GameInputHandler
	game_options_running: bool
	current_game_option: object

	@abc.abstractmethod
	def start_game(self):
		return

	@abc.abstractmethod
	def print_game_board(self, display_msg: str):
		return

	@abc.abstractmethod
	def player_turn(self, player_turn: int) -> Union[str, int]:
		return ''

	@abc.abstractmethod
	def game_loop(self):
		return

	@abc.abstractmethod
	def game_options_loop(self):
		return

	def get_valid_map_placements(self):
		return self.game_state.board_state.valid_board_placements()

class Game(GameBase):

	def __init__(self):
		self.game_running = False
		self.game_state = GameState()
		self.game_board = ConsoleGameBoard()
		self.game_options_loop()

	def game_options_loop(self):
		self.game_options_running = True
		self.current_game_option = GameMenuOption(self)
		while self.game_options_running:
			try:
				print('\n' * 20)
				selection = int(input("Please select a valid option:\n" + self.current_game_option.get_value() + '\n:'))
			except Exception:
				print("Value must be a integer")

			action_response: Union[GameOption, None] = self.current_game_option.next_action(selection)
			if isinstance(action_response, GameOption):
				self.current_game_option = action_response
				continue

	def game_loop(self):
		# setup the game state
		self.game_running = True
		self.game_state.player_two_turns = []
		self.game_state.player_one_turns = []
		self.game_state.board_state.reset_board_state()
		self.game_state.current_players_turn = 1
		self.current_game_option = GameMenuOption(self)

		newPosition: str
		playerCharacter: str
		while self.game_running:
			if self.game_over() is True:
				break

			if self.game_state.current_players_turn == 1:
				playerCharacter = self.game_state.player_one_character
				newPosition = self.player_turn(1)
				self.game_state.update_player_turn(playerCharacter, newPosition)
				self.game_state.current_players_turn = 2

			elif self.game_state.current_players_turn == 2:
				playerCharacter = self.game_state.player_two_character
				newPosition = self.player_turn(2)
				self.game_state.update_player_turn(playerCharacter, newPosition)
				self.game_state.current_players_turn = 1

			else:
				raise Exception("Game is only built for two players")

			print(str(newPosition) + ' was played')
			if self.game_over() is True:
				break

	def game_over(self) -> bool:
		(game_over, winner_character) = self.game_state.check_for_win()
		if game_over:
			winning_player = self.game_state.get_winning_player(winner_character)
			if winning_player > 0:
				self.print_game_board(f'Player {winning_player} has won')
				time.sleep(2)
				return True
			else:
				self.print_game_board(f'The game was a draw')
				time.sleep(2)
				return True
		return False

	def player_turn(self, player_turn: int) -> str:
		self.print_game_board(f'It is {player_turn}\'s turn now:')
		if player_turn == 1:
			return self.game_input_handler_player_one.play_turn(self.game_state.board_state.get_taken_board_state())
		elif player_turn == 2:
			return self.game_input_handler_player_two.play_turn(self.game_state.board_state.get_taken_board_state())

	def print_game_board(self, display_msg: str):
		self.game_board.print_game_board(self.game_state.board_state, display_msg)

	def start_game(self):
		self.game_loop()
