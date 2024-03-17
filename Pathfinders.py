from abc import ABC, abstractmethod


class Pathfinders(ABC):

    @abstractmethod
    def find_path(self, level_map: list, start: tuple, end: tuple):
        pass

    # Check around start position on the level_map if there are any empty positions.
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

    def calculate_euclidean_distance(self, position1: tuple, position2: tuple):
        result = ((position1[0] - position2[0])**2 + (position1[1] - position2[1])**2)**0.5
        return result

    def track_path(self, level_map, start: tuple, end: tuple):
        path = [start]
        pointer = start
        nodes = {}
        alternative_nodes = []
        current_node = None
        counter = 0
        paths = {}
        empty_positions = self.check_if_position_is_empty(level_map, start)

        while pointer != end or len(alternative_nodes) > 0:

            if pointer == end and len(alternative_nodes) > 0:
                path = [start]
                pointer = alternative_nodes.pop()
                path.append(pointer)
                empty_positions = self.check_if_position_is_empty(level_map, pointer)

            for position in empty_positions:
                result_position = self.calculate_euclidean_distance(position, end)
                nodes[position] = result_position

            for node in nodes:
                if current_node is None and node not in path:
                    current_node = node

                if current_node is not None and current_node != node and nodes[current_node] > nodes[node] and node not in path:
                    current_node = node
                elif current_node is not None and current_node != node and nodes[current_node] == nodes[node] and node not in path:
                    alternative_nodes.append(node)

            if current_node is not None and current_node not in path:
                path.append(current_node)
                pointer = current_node

            if current_node is None:
                return paths
            current_node = None
            nodes = {}
            empty_positions = self.check_if_position_is_empty(level_map, pointer)

            if pointer == end:
                paths[counter] = path
                counter += 1

        return paths


class GoTo(Pathfinders):
    def find_path(self, level_map: list, start: tuple, end: tuple):
        paths = self.track_path(level_map, start, end)
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

        for path in paths:
            if current_path is None:
                current_path = path
            if current_path != path and len(paths[current_path]) > len(paths[path]):
                current_path = path
        return paths[current_path]


class KeepDistance(Pathfinders):
    def find_path(self, level_map: list, start: tuple, end: tuple):
        pass


class GoAway(Pathfinders):
    def find_path(self, level_map: list, start: tuple, end: tuple):
        pass



