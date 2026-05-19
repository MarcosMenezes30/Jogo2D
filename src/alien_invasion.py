import pygame

from settings import Settings
from ship import Ship
from fleet_manager import FleetManager
from event_manager import EventManager
from bullet_manager import BulletManager
from collision_manager import CollisionManager


class AlienInvasion:
    """Gerencia o jogo e seus comportamentos."""

    def __init__(self):
        """Construtor da classe que inicializa o jogo e cria
        os recursos básicos"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # Criando uma instância da classe Ship para representar a nave espacial
        self.ship = Ship(self.screen, self.settings)

        # Mudando a cor do plano de fundo em RGB
        self.bg_color = self.settings.bg_color

        self.bullets = (
            pygame.sprite.Group()
        )  # Cria um grupo para armazenar os projéteis disparados pela nave

        self.aliens = (
            pygame.sprite.Group()
        )  # Cria um grupo para armazenar os alienígenas presentes no jogo

        self.fleet_manager = FleetManager(self)
        self.event_manager = EventManager(self)
        self.bullet_manager = BulletManager(self)
        self.collision_manager = CollisionManager(self)

    def run_game(self):
        """Cria um laço de repetição para a tela sempre ficar visível até
        que o usuário decida fechar a janela."""

        self.fleet_manager.create_fleet()  # Cria a frota de alienígenas
        # para ser desenhada na tela

        while True:

            # Verifica os eventos de teclado para controlar a
            # nave e disparar projéteis
            self.event_manager.check_keycaps()

            # Redesenha a tela a cada passagem pelo laço
            self.screen.fill(self.bg_color)

            # Redesenha a nave em sua posição atual
            self.ship.blitme()

            # Desenha cada alienígena na tela usando o método blitme
            self.fleet_manager.alien_drawn()

            # Atualiza a posição da nave com base na variável de controle
            self.ship.update()

            # Verifica os eventos projeteis lançados e atualiza suas posições
            self.bullet_manager.check_bullets()

            # Verifica se algum projétil atingiu um alienígena
            self.collision_manager.alien_collision()

            # Verifica os e atualiza a posição de cada alienígena
            # no grupo de alienígenas
            self.fleet_manager.alien_position()

            # Torna visível a tela mais recente
            pygame.display.flip()

            self.bullets.update()  # Atualiza a posição de cada projétil no
            # grupo de projéteis

            self.aliens.update()  # Atualiza a posição de cada alienígena no
            # grupo de alienígenas

            # Verifica se algum alienígena colidiu com a nave
            self.collision_manager.nav_colision()


if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
