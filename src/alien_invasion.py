import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class FleetManager:
    def __init__(self, game):
        self.game = game

    def create_fleet(self):
        """Cria uma frota de alienígenas."""
        # Cria um alienígena e calcula o número de alienígenas em uma linha
        # O espaçamento entre os alienígenas é igual a um alienígena
        alien = Alien(self.game.screen, self.game.settings)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        available_space_x = self.game.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        ship_height = self.game.ship.rect.height
        available_space_y = (
            self.game.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            # Cria a primeira linha de alienígenas
            for alien_number in range(number_aliens_x):
                # Cria um alienígena e o posiciona na linha
                alien = Alien(self.game.screen, self.game.settings)
                alien.x = alien_width + 2 * alien_width * alien_number
                alien.rect.x = alien.x
                alien.y = alien_height + 2 * alien_height * row_number
                alien.rect.y = alien.y
                self.game.aliens.add(alien)

    def alien_position(self):
        """Verifica os e atualiza a posição de
            cada alienígena no grupo de alienígenas"""

        for alien in self.game.aliens.sprites():
            if (
                alien.check_edges()
            ):  # Verifica se algum alienígena atingiu a borda da tela
                for alien in (
                    self.game.aliens.sprites()
                ):  # Atualiza a posição de cada alienígena no
                    # grupo de alienígenas
                    alien.rect.y += self.game.settings.fleet_drop_speed
                    # Move cada alienígena para baixo com base na
                    # velocidade de descida da frota
                self.game.settings.fleet_direction *= -1
                # Inverte a direção da frota para que os alienígenas se
                # movam para o lado oposto na próxima atualização
                break  # Sai do loop após encontrar o primeiro alienígena
                # que atingiu a borda da tela

    def alien_drawn(self):
        """Desenha cada alienígena na tela usando o método blitme."""

        # Desenha os alienígenas presentes no grupo de alienígenas na tela
        self.game.aliens.draw(
            self.game.screen
            # Desenha os alienígenas presentes no
            # grupo de alienígenas na tela
        )


class EventManager:
    def __init__(self, game):
        self.game = game

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
                    self.game.ship.moving_right = True
                elif (
                    event.key == pygame.K_LEFT
                ):  # Verifica se a tecla pressionada é a seta para a esquerda
                    self.game.ship.moving_left = True
                elif (
                    event.key == pygame.K_SPACE
                ):  # Verifica se a tecla pressionada é a barra de espaço
                    if (
                        len(self.game.bullets) < self.game.settings.bullet_allowed
                    ):  # Verifica se o número de projéteis na tela
                        # excede o limite permitido
                        new_bullet = Bullet(
                            self.game.screen, self.game.settings, self.game.ship
                        )  # Cria um novo projétil
                        # Aqui seria necessário adicionar o novo projétil a um
                        # grupo de projéteis para que ele possa ser atualizado
                        # e desenhado na tela
                        self.game.bullets.add(
                            new_bullet
                        )  # Adiciona o novo projétil ao grupo de projéteis

            elif event.type == pygame.KEYUP:  # Detecta quando uma tecla é
                # liberada
                if (
                    event.key == pygame.K_RIGHT
                ):  # Verifica se a tecla liberada é a seta para a direita
                    self.game.ship.moving_right = False
                elif (
                    event.key == pygame.K_LEFT
                ):  # Verifica se a tecla liberada é a seta para a esquerda
                    self.game.ship.moving_left = False


class BulletManager:
    def __init__(self, game):
        self.game = game

    def check_bullets(self):
        """Verifica os eventos projeteis lançados
            e atualiza suas posições"""

        for bullet in (
            self.game.bullets.sprites()
                ):  # Atualiza a posição de cada projétil no grupo de projéteis
            bullet.draw_bullet()  # Desenha cada projétil na tela

            self.game.bullets.update()  # Atualiza a posição de cada projétil
            # no grupo de projéteis
            for (
                bullet
            ) in self.game.bullets.copy():  # Verifica se algum projétil
                # saiu da tela
                if (
                    bullet.rect.bottom <= 0
                ):  # Se o projétil saiu da tela (parte inferior do retângulo
                    # do projétil é menor ou igual a 0)
                    self.game.bullets.remove(
                        bullet
                    )  # Remove o projétil do grupo de projéteis


class CollisionManager:
    def __init__(self, game):
        self.game = game

    def alien_collision(self):
        """Verifica colisões entre projéteis e alienígenas."""

        # Verifica se algum projétil atingiu um alienígena
        # Em caso afirmativo, remove o projétil e o alienígena atingido
        pygame.sprite.groupcollide(
            self.game.bullets, self.game.aliens, True, True
        )  # Verifica as colisões entre os projéteis e os alienígenas,
        # removendo ambos quando uma colisão é detectada

    def nav_colision(self):
        """Verifica colisões entre a nave e alienígenas."""

        if pygame.sprite.spritecollideany(
            self.game.ship, self.game.aliens
        ):  # Verifica se a nave colidiu com algum alienígena
            print(
                "A nave foi atingida!"
            )  # Imprime uma mensagem no console indicando que
            # a nave foi atingida
            sys.exit()  # Encerra o jogo


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
