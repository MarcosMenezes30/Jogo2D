import sys
import pygame

from bullet import Bullet
from interfaces import BulletFactory, BulletSettings, KeyboardControlledShip


class EventManager:
    def __init__(
        self,
        screen,
        settings: BulletSettings,
        ship: KeyboardControlledShip,
        bullets,
        bullet_class: BulletFactory = Bullet,
    ):
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.bullets = bullets
        self.bullet_class = bullet_class

    def check_keycaps(self):
        """Verifica os eventos de teclado para controlar
            a nave e disparar projéteis"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif (
                event.type == pygame.KEYDOWN
            ):  # Detecta quando uma tecla é pressionada
                if (
                    event.key == pygame.K_RIGHT
                ):  # Verifica se a tecla pressionada é a seta para a direita
                    self.ship.moving_right = True
                elif (
                    event.key == pygame.K_LEFT
                ):  # Verifica se a tecla pressionada é a seta para a esquerda
                    self.ship.moving_left = True
                elif (
                    event.key == pygame.K_SPACE
                ):  # Verifica se a tecla pressionada é a barra de espaço
                    if (
                        len(self.bullets) < self.settings.bullet_allowed
                    ):  # Verifica se o número de projéteis na tela
                        # excede o limite permitido
                        new_bullet = self.bullet_class(
                            self.screen, self.settings, self.ship
                        )  # Cria um novo projétil
                        # Aqui seria necessário adicionar o novo projétil a um
                        # grupo de projéteis para que ele possa ser atualizado
                        # e desenhado na tela
                        self.bullets.add(
                            new_bullet
                        )  # Adiciona o novo projétil ao grupo de projéteis

            elif event.type == pygame.KEYUP:  # Detecta quando uma tecla é
                # liberada
                if (
                    event.key == pygame.K_RIGHT
                ):  # Verifica se a tecla liberada é a seta para a direita
                    self.ship.moving_right = False
                elif (
                    event.key == pygame.K_LEFT
                ):  # Verifica se a tecla liberada é a seta para a esquerda
                    self.ship.moving_left = False
