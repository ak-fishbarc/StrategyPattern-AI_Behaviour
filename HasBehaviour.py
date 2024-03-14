from abc import ABC, abstractmethod


class HasBehaviour(ABC):

    # target takes coordinates x and y as tuple
    @abstractmethod
    def move(self, my_position: tuple, target: tuple) -> tuple:
        pass


# Move towards the target.
class IsAggressive(HasBehaviour):
    def move(self, my_position: tuple, target: tuple) -> tuple:
        pass


# Keep the distance from the target.
class IsDefensive(HasBehaviour):
    def move(self, my_position: tuple, target: tuple) -> tuple:
        pass


# Run away from the target.
class IsCowardly(HasBehaviour):
    def move(self, my_position: tuple, target: tuple) -> tuple:
        pass

