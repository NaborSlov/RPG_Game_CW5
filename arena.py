from unit import Player, Enemy


class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class Arena(metaclass=Singleton):
    STAMINA_PER_ROUND = 1
    player = None
    enemy = None
    game_is_running = False

    def start_game(self, player: Player, enemy: Enemy):
        self.player = player
        self.enemy = enemy
        self.game_is_running = True

    def _check_player_health(self) -> str:
        self.battle_result = None

        if self.player.health_points < 0:
            self.battle_result = "Игрок проиграл битву"

        if self.enemy.health_points < 0:
            self.battle_result = "Игрок выиграл битву"

        if self.player.health_points < 0 and self.enemy.health_points < 0:
            self.battle_result = "Ничья"

        return self.battle_result

    def _regenerate_stamina(self):
        for unit in (self.player, self.enemy):
            if unit.stamina_points < unit.unit_class.max_stamina:
                unit.stamina_points += self.STAMINA_PER_ROUND * unit.unit_class.stamina

                if unit.stamina_points > unit.unit_class.max_stamina:
                    unit.stamina_points = unit.unit_class.max_stamina

    def next_turn(self) -> str:
        if self._check_player_health():
            return self._end_game()

        if self.game_is_running:
            self._regenerate_stamina()
            return self.enemy.hit(self.player)

        return self.battle_result

    def _end_game(self) -> str:
        self._instances = {}
        self.game_is_running = False
        return self.battle_result

    def hit_player(self) -> str:
        if self.game_is_running:
            result = f"{self.player.hit(self.enemy)} {self.next_turn()}"
            return result

        return self.battle_result

    def use_skill_player(self):
        if self.game_is_running:
            result = f"{self.player.skill_attack(self.enemy)} {self.next_turn()}"
            return result

        return self.battle_result


