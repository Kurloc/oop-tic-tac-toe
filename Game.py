from GameBoard import GameBoard, ConsoleGameBoard
from GameState import GameState
from InputHandler import GameInputHandler, ConsoleGameInputHandler


class Game:
    __game_running: bool
    __game_state: GameState
    __game_board: GameBoard
    __game_input_handler: GameInputHandler

    def __init__(self):
        self.__game_running = False
        self.__game_state = GameState()
        self.__game_board = ConsoleGameBoard()
        self.__game_input_handler = ConsoleGameInputHandler(self.__game_state.board_state.board_state_dictionary.keys())
        self.start_game()

    def game_loop(self):
        newPosition: str
        playerCharacter: str
        self.__game_running = True
        while self.__game_running:
            if self.__game_state.current_players_turn is 1:
                playerCharacter = self.__game_state.player_one_character
                newPosition = self.player_turn(1)
                self.__game_state.current_players_turn = 2

            elif self.__game_state.current_players_turn is 2:
                playerCharacter = self.__game_state.player_two_character
                newPosition = self.player_turn(2)
                self.__game_state.current_players_turn = 1

            else:
                raise Exception("Game is only built for two players")

            self.__game_state.update_player_turn(playerCharacter, newPosition)

            (game_over, winner_character) = self.__game_state.check_for_win()
            if game_over:
                winning_player = self.__game_state.get_winning_player(winner_character)
                if winning_player > 0:
                    self.print_game_board(f'Player {winning_player} has won')
                    self.__game_running = False
                    break

    def start_game(self):
        self.game_loop()

    def player_turn(self, player_turn: int) -> str:
        self.print_game_board(f'It is {player_turn}\'s turn now:')
        return self.__game_input_handler.play_turn(self.__game_state.board_state.get_taken_board_state())

    def print_game_board(self, display_msg: str):
        self.__game_board.print_game_board(self.__game_state.board_state, display_msg)
