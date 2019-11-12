from abc import ABC, abstractmethod
#
#
# class Creature(ABC):
#
#     @abstractmethod
#     def get_positive_effects(self):
#         pass
#
#     @abstractmethod
#     def get_negative_effects(self):
#         pass
#
#     @abstractmethod
#     def get_stats(self):
#         pass
#
#
class Hero:
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


class AbstractEffect(Hero, ABC):
    def __init__(self, base):
        super(AbstractEffect, self).__init__()
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        self.base.get_stats()


class AbstractPositive(AbstractEffect):
    def __init__(self, base):
        super().__init__(base)

    @abstractmethod
    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects()



class AbstractNegative(AbstractEffect):
    def __init__(self, base):
        super().__init__(base)
    # @abstractmethod
    def get_positive_effects(self):
        return self.base.get_positive_effects()

    @abstractmethod
    def get_negative_effects(self):
        buff = self.base.get_positive_effects()
        buff.append(self.__class__.__name__)
        return buff


"""
Увеличивает характеристики: Сила, Выносливость, Ловкость, Удача на 7;
уменьшает характеристики: Восприятие, Харизма, Интеллект на 3;
количество единиц здоровья увеличивается на 50.
"""
class Berserk(AbstractPositive):
    """
        "Strength": 15,  # сила
        "Perception": 4,  # восприятие
        "Endurance": 8,  # выносливость
        "Charisma": 2,  # харизма
        "Intelligence": 3,  # интеллект
        "Agility": 8,  # ловкость
        "Luck": 1
    """

    def get_positive_effects(self):
        buff = self.base.get_positive_effects()
        buff.append(self.__class__.__name__)
        return buff

    def get_stats(self):
        buff = self.base.get_stats()
        buff['Strength'] += 7
        buff['Endurance'] += 7
        buff['Agility'] += 7
        buff['Luck'] += 7

        buff['Perception'] -= 3
        buff['Charisma'] -= 3
        buff['Intelligence'] -= 3

        buff['HP'] +=50
        return buff

"""
увеличивает все основные характеристики на 2.
"""
class Blessing(AbstractPositive):

    def get_positive_effects(self):
        buff = self.base.get_positive_effects()
        buff.append(self.__class__.__name__)
        return buff

    def get_stats(self):
        buff = self.base.get_stats()
        buff['Strength'] += 2
        buff['Perception'] += 2
        buff['Endurance'] += 2
        buff['Charisma'] += 2
        buff['Intelligence'] += 2
        buff['Agility'] += 2
        buff['Luck'] += 2
        return buff

"""
уменьшает характеристики: Сила, Выносливость, Ловкость на 4
"""
class Weakness(AbstractNegative):
    """
        "Strength": 15,  # сила
        "Perception": 4,  # восприятие
        "Endurance": 8,  # выносливость
        "Charisma": 2,  # харизма
        "Intelligence": 3,  # интеллект
        "Agility": 8,  # ловкость
        "Luck": 1
    """

    def get_negative_effects(self):
        buff = self.base.get_negative_effects()
        buff.append(self.__class__.__name__)
        return buff

    def get_stats(self):
        buff = self.base.get_stats()
        buff['Strength'] -= 4
        buff['Endurance'] -= 4
        buff['Agility'] -= 4
        return buff

"""
уменьшает все основные характеристики на 2.
"""
class Curse(AbstractNegative):

    def get_negative_effects(self):
        buff = self.base.get_negative_effects()
        buff.append(self.__class__.__name__)
        return buff

    def get_stats(self):
        buff = self.base.get_stats()
        buff['Strength'] -= 2
        buff['Perception'] -= 2
        buff['Endurance'] -= 2
        buff['Charisma'] -= 2
        buff['Intelligence'] -= 2
        buff['Agility'] -= 2
        buff['Luck'] -= 2
        return buff

"""
уменьшает  характеристику Удача на 10.
"""
class EvilEye(AbstractNegative):

    def get_negative_effects(self):
        buff = self.base.get_negative_effects()
        buff.append(self.__class__.__name__)
        return buff

    def get_stats(self):
        buff = self.base.get_stats()
        buff['Luck'] -= 10
        return buff
