from abc import ABC, abstractmethod
import Pathfinders


class HasBehaviour(ABC):

    # my_position and target take coordinates x and y as tuple.
    @abstractmethod
    def move(self, level_map: list, my_position: tuple, target: tuple) -> tuple:
        pass


# Move towards the target.
class IsAggressive(HasBehaviour):
    def move(self, level_map: list, my_position: tuple, target: tuple) -> tuple:
        pathfinder = Pathfinders.GoTo().find_path(level_map, my_position, target)
        if len(pathfinder) > 0:
            return pathfinder[1]
        elif len(pathfinder) == 0:
            return my_position


# Keep the distance from the target.
class IsDefensive(HasBehaviour):
    def move(self, level_map: list, my_position: tuple, target: tuple) -> tuple:
        pass


# Run away from the target.
class IsCowardly(HasBehaviour):
    def move(self, level_map: list, my_position: tuple, target: tuple) -> tuple:
        pass

