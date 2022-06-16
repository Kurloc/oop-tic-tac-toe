from typing import List


class BoardState:
	__base_board_state_dictionary = {
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

	__board_state_dictionary = {
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
		for key, value in self.__board_state_dictionary.items():
			if len(value) > 0 and value is not ' ':
				taken_board_positions.append(key)

		return taken_board_positions

	def get_board_as_2d_array(self) -> List[List[str]]:
		b = self.__board_state_dictionary
		return [
			[b['a1'], b['a2'], b['a3']],
			[b['b1'], b['b2'], b['b3']],
			[b['c1'], b['c2'], b['c3']],
		]

	def reset_board_state(self):
		self.__board_state_dictionary = self.__base_board_state_dictionary.copy()

	def valid_board_placements(self) -> List[str]:
		return list(self.__board_state_dictionary.keys())

	def get_value_from_board_space(self, key: str) -> str:
		return self.__board_state_dictionary[key]

	def set_value_of_board_space(self, key: str, value: str):
		self.__board_state_dictionary[key] = value
