from abc import ABC, abstractmethod


class Creature(ABC):

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass


class Hero(Creature):
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points,
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(Creature):
    def __init__(self, obj):
        self.obj = obj

    def get_positive_effects(self):
        self.obj.get_positive_effects()

    def get_negative_effects(self):
        self.obj.get_negative_effects()

    def get_stats(self):
        self.obj.get_stats()


class AbstractPositive(AbstractEffect):
    pass


class AbstractNegative(AbstractEffect):
    pass


class Berserk(AbstractPositive):
    pass


class Blessing(AbstractPositive):
    pass


class Weakness(AbstractNegative):
    pass


class Curse(AbstractNegative):
    pass


class EvilEye(AbstractNegative):
    pass
