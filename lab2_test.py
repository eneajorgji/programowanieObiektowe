from abc import ABC, abstractmethod


class GameObject(ABC):
    def __init__(self, health_point_count):
        self.health_point_count = health_point_count

    def is_living(self):
        if self.health_point_count > 0:
            return True
        else:
            return False

    @abstractmethod
    def interact(self):
        pass


class Player(GameObject):
    pass


class Monster(GameObject):
    pass


class Door(GameObject):
    pass
