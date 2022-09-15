from abc import ABC, abstractmethod


class Skill(ABC):
    user = None
    target = None

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def attack(self):
        pass

    @property
    @abstractmethod
    def stamina_per_hit(self):
        pass

    @abstractmethod
    def skill_effect(self):
        """
        Нанесения урона навыком
        """
        pass

    def use(self, user, target) -> str:
        """
        Метод использования навыка

        :param user: тот кто использует скилл
        :param target: цель которую атакует user
        """
        self.user = user
        self.target = target

        if self.user.stamina_points > self.stamina_per_hit:
            return self.skill_effect()

        return f"{self.user.name} попытался использовать {self.name}, но у него не хватило выносливости."


class FeroKick(Skill):
    name: str = "Свирепый пинок"
    attack: int = 6
    stamina_per_hit: int = 12

    def skill_effect(self) -> str:
        self.target.get_damage(self.attack)
        self.user.stamina_points -= self.stamina_per_hit
        return f"{self.user.name} воспользовался свирепым пинком и нанес {self.attack}"


class PowerInject(Skill):
    name: str = "Мощный укол"
    attack: int = 5
    stamina_per_hit: int = 15

    def skill_effect(self) -> str:
        self.target.get_damage(self.attack)
        self.user.stamina_points -= self.stamina_per_hit
        return f"{self.user.name} воспользовался мощным уколом и нанес {self.attack}"
