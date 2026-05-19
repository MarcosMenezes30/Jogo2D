import sys
import pygame


class CollisionManager:
    def __init__(self, ship, bullets, aliens):
        self.ship = ship
        self.bullets = bullets
        self.aliens = aliens

    def alien_collision(self):
        """Verifica colisões entre projéteis e alienígenas."""

        # Verifica se algum projétil atingiu um alienígena
        # Em caso afirmativo, remove o projétil e o alienígena atingido
        pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )  # Verifica as colisões entre os projéteis e os alienígenas,
        # removendo ambos quando uma colisão é detectada

    def nav_colision(self):
        """Verifica colisões entre a nave e alienígenas."""

        if pygame.sprite.spritecollideany(
            self.ship, self.aliens
        ):  # Verifica se a nave colidiu com algum alienígena
            print(
                "A nave foi atingida!"
            )  # Imprime uma mensagem no console indicando que
            # a nave foi atingida
            sys.exit()  # Encerra o jogo
