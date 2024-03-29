from abc import ABC, abstractmethod
from random import randint


class DistanceCalculator:

    def calculate_manhattan_distance(self, position1: tuple, position2: tuple):
        result = abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])
        return result

    def calculate_euclidean_distance(self, position1: tuple, position2: tuple):
        result = ((position1[0] - position2[0])**2 + (position1[1] - position2[1])**2)**0.5
        return result


class Pathfinders(ABC):

    @abstractmethod
    def find_path(self, level_map: list, start: tuple, end: tuple):
        pass

    """ Check around start position on the level_map if there are any empty positions.
        level_map width and height need to be equal. """
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

    def track_path(self, level_map, start: tuple, end: tuple):
        distance_calculator = DistanceCalculator()
        """ path will get inserted as a value into paths with the counter as the key.
            pointer points to the current position in search.
            nodes are assigned with position as key and the cost to the end position as value
            alternative_nodes are assigned when two positions have the same value, one of them will
            get used as a pointer and another one will be inserted into alternative_nodes. Later
            alternative_nodes get explored as a potential path to the end.
            current_node is used for iteration through nodes.
            paths are assigned when path is built.
            empty_positions checks for any empty position around the current position - pointer.
            visited_nodes is used for backtracking when the current path meets dead end."""
        path = [start]
        pointer = start
        nodes = {}
        alternative_nodes = []
        current_node = None
        counter = 0
        paths = {}
        empty_positions = self.check_if_position_is_empty(level_map, start)
        visited_nodes = []

        while pointer != end or len(alternative_nodes) > 0:
            """ If current path was explored, check for any alternative node to search for alternative
                path. """
            if pointer == end and len(alternative_nodes) > 0:
                counter += 1
                pointer = alternative_nodes.pop()
                path = [pointer]
                empty_positions = self.check_if_position_is_empty(level_map, pointer)
            # Attach value to any empty position available.
            for position in empty_positions:
                result_position = distance_calculator.calculate_euclidean_distance(position, end)
                nodes[position] = result_position

            """ Check nodes and find the node with the best cost.
                If two nodes have the same value - Pick one as the pointer and leave the other
                in alternative_nodes for exploration later. """
            for node in nodes:
                if current_node is None and node not in path and node not in visited_nodes:
                    current_node = node

                if current_node is not None and current_node != node and nodes[current_node] > nodes[node] and node not in path\
                        and node not in visited_nodes:
                    current_node = node

                elif current_node is not None and current_node != node and nodes[current_node] == nodes[node] and node not in path\
                        and node not in visited_nodes:
                    alternative_nodes.append(node)

            if current_node is not None and current_node not in path:
                visited_nodes.append(current_node)
                path.append(current_node)
                pointer = current_node

            # If got stuck, go back until there's another way.
            if current_node is None:
                go_back = path.pop()
                if go_back not in visited_nodes:
                    visited_nodes.append(go_back)
                if len(path) >= 1:
                    pointer = path[-1]
                elif len(path) == 0:
                    """ If after all the checks there's no other path in paths and this
                        path is empty and it's the only path - return empty path as a message
                        that there are no valid paths on this level_map. """
                    if len(paths) == 0:
                        paths[counter] = path
                    return paths

            current_node = None
            nodes = {}
            empty_positions = self.check_if_position_is_empty(level_map, pointer)
            # Path exploration is finished. Check if there are any alternative nodes left.
            if pointer == end:
                paths[counter] = path

        return paths


class GoTo(Pathfinders):
    def find_path(self, level_map: list, start: tuple, end: tuple):
        """ Start by looking for any paths from start to end. """
        paths = self.track_path(level_map, start, end)
        """ This part of the code will go through all the positions in all the paths.
            Every position will:
            1. Look for a path from itself to the start.
            2. Look for a path from itself to the end.
            3. If it can reach both start and end from itself it'll combine both paths.
            4. All the combined paths are added to paths for cost evaluation. 
            This will check if the shortest path can be found from all the paths explored at first. """
        combined_paths = {}
        counter = 0
        for key in paths:
            counter = key
        for path in paths:
            for position in paths[path]:
                counter += 1
                combine_paths = []
                check_path_to_start = self.track_path(level_map, position, start)
                check_path_to_end = self.track_path(level_map, position, end)

                for key in check_path_to_start:
                    for value in reversed(check_path_to_start[key]):
                        if value not in combine_paths:
                            combine_paths.append(value)

                for key in check_path_to_end:
                    for value in check_path_to_end[key]:
                        if value not in combine_paths:
                            combine_paths.append(value)

                if len(combine_paths) > 0 and start in combine_paths and end in combine_paths:
                    combined_paths[counter] = combine_paths

        for key in combined_paths:
            paths[key] = combined_paths[key]

        current_path = None
        # Evaluate the cost of each path in paths.
        for path in paths:
            if current_path is None and start in paths[path] and end in paths[path]:
                current_path = path
            if current_path is not None and current_path != path and len(paths[current_path]) > len(paths[path]) \
                    and start in paths[path] \
                    and end in paths[path]:
                current_path = path
            # If there is only one path in paths and that path is empty, it means that there's no
            # valid path on this level_map.
            elif len(paths) == 1 and len(paths[path]) == 0:
                current_path = path

        # Return shortest path.
        return paths[current_path]


class KeepDistance(Pathfinders):
    """ This code could also be used for turn based rpg/strategy game for highlighting
        squares/hexagons/fields where the unit can move """
    def find_path(self, level_map: list, start: tuple, end: tuple):
        distance_calculator = DistanceCalculator()
        counter = 0
        visited_positions = [end]
        valid_positions = []
        paths = {}
        possible_paths = {}
        """ Check which positions are 4 steps away from the target. 
            1. Set end in visited_position.
            2. Loop through each visited_position; At every step set visited_position as pointer.
            3. Check positions around the pointer. Check if any of them is empty.
            4. For each empty position if it was not visited yet set it in visited_positions and check
            if it's 4 steps away from the target. If it is set it in valid_positions. """
        while counter < 4:
            counter += 1
            for visited_position in visited_positions:
                pointer = visited_position
                check_positions = self.check_if_position_is_empty(level_map, pointer)
                for position in check_positions:
                    if position not in visited_positions:
                        visited_positions.append(position)
                        validate_position = distance_calculator.calculate_manhattan_distance(position, end)
                        if validate_position == 4:
                            valid_positions.append(position)
        """ From all the positions 4 steps away from the target - Find path to them from start position. """
        counter = 0
        for position in valid_positions:
            possible_paths = self.track_path(level_map, start, position)
            for path in possible_paths:
                if 1 <= len(possible_paths[path]) <= 5:
                    paths[counter] = possible_paths[path]
                    counter += 1

        # Because there could be more than one position 4 steps away from the target, we can choose randomly.
        # Separate function could be made for non-random choice.
        if len(paths) > 0:
            choose_path_random = randint(0, len(paths)-1)
            return paths[choose_path_random]
        else:
            return []


class GoAway(Pathfinders):
    def find_path(self, level_map: list, start: tuple, end: tuple):
        distance_calculator = DistanceCalculator()
        """ 1. Check each position around the point on the map; starting from the start.
            2. If position is empty and it's X blocks away from the target, add it to the list;
            X = counter.
            Each step should be further and further away from the target. How far it should go could
            be tweaked depending on the need of the game. """
        counter = 0
        checked_points = [start]
        distance_from_start_to_end = distance_calculator.calculate_manhattan_distance(start, end)
        while counter < len(level_map)-1:
            counter += 1
            for step in checked_points:
                check_positions = self.check_if_position_is_empty(level_map, step)
                for position in check_positions:
                    distance_from_position_to_end = distance_calculator.calculate_manhattan_distance(position, end)
                    distance_from_position_to_start = distance_calculator.calculate_manhattan_distance(position, start)
                    if distance_from_position_to_end >= distance_from_start_to_end \
                       and distance_from_position_to_start < distance_from_position_to_end \
                            and position not in checked_points:
                        checked_points.append(position)
        """ 1. Once we get all the points that are away from the target we will look for points that
            are furthest away. 
            2. We know that previous steps were making a list of points going from the nearest to the 
            furthest point. So, we will reverse the list and check all the points that are furthest away 
            from the target. 
            3. If there are a few points, we will choose randomly where to go. """
        pointer = None
        for position in reversed(checked_points):
            if pointer is None:
                pointer = position
            if pointer != position:
                check_distance_pointer = distance_calculator.calculate_manhattan_distance(pointer, end)
                check_distance_position = distance_calculator.calculate_manhattan_distance(position, end)
                if check_distance_pointer > check_distance_position:
                    checked_points.remove(position)
                elif check_distance_pointer < check_distance_position:
                    pointer = position

        choose_path_randomly = randint(0, len(checked_points)-1)
        path = self.track_path(level_map, start, checked_points[choose_path_randomly])
        if len(path) > 0:
            return path[0]
        else:
            return []








