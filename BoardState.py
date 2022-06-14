from typing import List


class BoardState:
    board_state_dictionary = {
        'a1': ' ',
        'a2': ' ',
        'a3': ' ',
        'b1': ' ',
        'b2': ' ',
        'b3': ' ',
        'c1': ' ',
        'c2': ' ',
        'c3': ' '
    }

    def get_taken_board_state(self) -> List[str]:
        taken_board_positions = []
        for key, value in self.board_state_dictionary.items():
            if len(value) > 0 and value is not ' ':
                taken_board_positions.append(key)

        return taken_board_positions

    def get_board_as_2d_array(self) -> List[List[str]]:
        b = self.board_state_dictionary
        return [
            [b['a1'], b['a2'], b['a3']],
            [b['b1'], b['b2'], b['b3']],
            [b['c1'], b['c2'], b['c3']],
        ]
