from alien import Alien


class FastAlien(Alien):
    """Alienígena mais rápido."""

    def _speed_multiplier(self):
        return 2
