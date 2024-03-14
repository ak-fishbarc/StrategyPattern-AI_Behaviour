from abc import ABC, abstractmethod


class Pathfinders(ABC):

    @abstractmethod
    def find_path(self, level_map: list, start: tuple, end: tuple):
        pass


class GoTo(Pathfinders):
    def find_path(self, level_map: list, start: tuple, end: tuple):
        pass


class KeepDistance(Pathfinders):
    def find_path(self, level_map: list, start: tuple, end: tuple):
        pass


class GoAway(Pathfinders):
    def find_path(self, level_map: list, start: tuple, end: tuple):
        pass



