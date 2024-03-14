from abc import ABC, abstractmethod


class Pathfinders(ABC):

    @abstractmethod
    def find_path(self, level_map: list, start: tuple, end: tuple):
        pass

    # Check around on the level_map if there are any empty positions around start.
    def check_if_position_is_empty(self, level_map: list, start: tuple):
        empty_positions = []

        up = start[1] - 1
        down = start[1] + 1
        left = start[0] - 1
        right = start[0] + 1

        if up >= 0 and level_map[start[0]][up] == 0:
            empty_positions.append((start[0], up))

        if down <= len(level_map)-1 and level_map[start[0]][down] == 0:
            empty_positions.append((start[0], down))

        if left >= 0 and level_map[left][start[1]] == 0:
            empty_positions.append((left, start[1]))

        if right <= len(level_map)-1 and level_map[right][start[1]] == 0:
            empty_positions.append((right, start[1]))

        return empty_positions

    def calculate_manhattan_distance(self, position1: tuple, position2: tuple):
        result = abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])
        return result


""" 
    This class moves towards the target. In steps:
    1. Set the pointer to current position.
    2. Loop until the target is reached. If the target is reached go to Step 7.
    3. Look for empty positions around current position.
    4. For any empty position check if it's closer to the target than the current position.
    5. If it's closer, set that closer position as the new pointer.
    6. Go back to point 2.
    7. Return path.
"""


class GoTo(Pathfinders):
    def find_path(self, level_map: list, start: tuple, end: tuple):
        path = []
        pointer = start
        while self.calculate_manhattan_distance(pointer, end) >= 1:
            empty_positions = self.check_if_position_is_empty(level_map, pointer)

            for position in empty_positions:
                result = self.calculate_manhattan_distance(position, end)
                check_pointer = self.calculate_manhattan_distance(pointer, end)
                if check_pointer > result:
                    pointer = position

            path.append(pointer)

        return path


class KeepDistance(Pathfinders):
    def find_path(self, level_map: list, start: tuple, end: tuple):
        pass


class GoAway(Pathfinders):
    def find_path(self, level_map: list, start: tuple, end: tuple):
        pass



