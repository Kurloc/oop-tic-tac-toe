from typing import List, Tuple, Union

from BoardState import BoardState


class GameState:
    current_players_turn: int  # 1 or 2
    player_one_turns: []
    player_one_character: str
    player_two_turns: []
    player_two_character: str
    board_state: BoardState

    def __init__(self):
        self.player_one_turns = []
        self.player_one_character = "X"
        self.player_two_turns = []
        self.player_two_character = "O"
        self.board_state = BoardState()
        self.current_players_turn = 1

    def update_player_turn(self, player_character: str, position: str):
        self.board_state.board_state_dictionary[position] = player_character

    def check_for_win(self) -> Tuple[bool, str]:
        board_values = self.board_state.get_board_as_2d_array()
        (game_over, winner) = self.__check_rows(board_values)
        if game_over:
            return True, winner

        (game_over, winner) = self.__check_diagonals(board_values)
        if game_over:
            return True, winner

        return False, ''

    @staticmethod
    def __check_rows(board_values: List[List[str]]) -> Tuple[bool, str]:
        for row in board_values:
            if len(set(row)) == 1:
                return True, row[0]

        return False, ''

    @staticmethod
    def __check_diagonals(board_values: List[List[str]]) -> Tuple[bool, str]:
        if len(set([board_values[i][i] for i in range(len(board_values))])) == 1:
            return True, board_values[0][0]

        if len(set([board_values[i][len(board_values) - i - 1] for i in range(len(board_values))])) == 1:
            return True, board_values[0][len(board_values) - 1]

        return False, ''

    def get_winning_player(self, winner_character: str):
        if winner_character is self.player_one_character:
            return 1

        if winner_character is self.player_two_character:
            return 2

        return 0
