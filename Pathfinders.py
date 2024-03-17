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
        """ path will get inserted as a value into paths with the counter as the key.
            pointer points to the current position in search.
            nodes are assigned with position as key and the cost to the end position as value
            alternative_nodes are assigned when two positions have the same value, one of them will
            get used as a pointer and another one will be inserted into alternative_nodes. Later
            alternative nodes get explored as a potential path to the end.
            current_node is used for iteration through nodes.
            paths are assigned when path is built.
            empty_positions checks for any empty position around the current position - pointer. """
        path = [start]
        pointer = start
        nodes = {}
        alternative_nodes = []
        current_node = None
        counter = 0
        paths = {}
        empty_positions = self.check_if_position_is_empty(level_map, start)

        while pointer != end or len(alternative_nodes) > 0:
            """ If current path was explored, check for any alternative node to search for alternative
                path. """
            if pointer == end and len(alternative_nodes) > 0:
                path = [start]
                pointer = alternative_nodes.pop()
                path.append(pointer)
                empty_positions = self.check_if_position_is_empty(level_map, pointer)
            # Attach value to any empty position available.
            for position in empty_positions:
                result_position = self.calculate_euclidean_distance(position, end)
                nodes[position] = result_position

            """ Check nodes and find the node with the best cost.
                If two nodes have the same value - Pick one as the pointer and leave the other
                in alternative_nodes for exploration later. """
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
            # Path exploration is finished. Check if there are any alternative nodes left.
            if pointer == end:
                paths[counter] = path
                counter += 1

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
            if current_path is None:
                current_path = path
            if current_path != path and len(paths[current_path]) > len(paths[path]):
                current_path = path

        # Return shortest path.
        return paths[current_path]


class KeepDistance(Pathfinders):
    def find_path(self, level_map: list, start: tuple, end: tuple):
        pass


class GoAway(Pathfinders):
    def find_path(self, level_map: list, start: tuple, end: tuple):
        pass



