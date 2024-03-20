from abc import ABC, abstractmethod
from Pathfinders import Pathfinders


class HasBehaviour(ABC):

    # my_position and target take coordinates x and y as tuple.
    @abstractmethod
    def move(self, level_map: list, my_position: tuple, target: tuple) -> tuple:
        pass


# Move towards the target.
class IsAggressive(HasBehaviour):
    def move(self, level_map: list, my_position: tuple, target: tuple) -> tuple:
        pass


# Keep the distance from the target.
class IsDefensive(HasBehaviour):
    def move(self, level_map: list, my_position: tuple, target: tuple) -> tuple:
        pass


# Run away from the target.
class IsCowardly(HasBehaviour):
    def move(self, level_map: list, my_position: tuple, target: tuple) -> tuple:
        pass

