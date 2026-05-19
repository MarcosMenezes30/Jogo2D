import pygame

from alien import Alien
from interfaces import AlienFactory, FleetSettings, HasRect


class FleetManager:
    """Responsável por criar e gerenciar a frota de alienígenas."""

    def __init__(
        self,
        screen,
        settings: FleetSettings,
        ship: HasRect,
        alien_class: AlienFactory = Alien,
    ):
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.aliens = pygame.sprite.Group()
        self.alien_class = alien_class

    def _create_alien(
        self, alien_number: int, row_number: int, alien_width: int, alien_height: int
    ) -> None:
        """Cria um alienígena e o posiciona na linha."""
        alien = self.alien_class(self.screen, self.settings)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.y = alien_height + 2 * alien_height * row_number
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def create_fleet(self):
        """Cria uma frota de alienígenas."""
        # Cria um alienígena e calcula o número de alienígenas em uma linha
        # O espaçamento entre os alienígenas é igual a um alienígena
        alien = self.alien_class(self.screen, self.settings)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            # Cria a primeira linha de alienígenas
            for alien_number in range(number_aliens_x):
                # Cria um alienígena e o posiciona na linha
                self._create_alien(
                    alien_number, row_number, alien_width, alien_height
                )

    def alien_position(self):
        """Verifica os e atualiza a posição de
            cada alienígena no grupo de alienígenas"""

        for alien in self.aliens.sprites():
            if (
                alien.check_edges()
            ):  # Verifica se algum alienígena atingiu a borda da tela
                for alien in (
                    self.aliens.sprites()
                ):  # Atualiza a posição de cada alienígena no
                    # grupo de alienígenas
                    alien.rect.y += self.settings.fleet_drop_speed
                    # Move cada alienígena para baixo com base na
                    # velocidade de descida da frota
                self.settings.fleet_direction *= -1
                # Inverte a direção da frota para que os alienígenas se
                # movam para o lado oposto na próxima atualização
                break  # Sai do loop após encontrar o primeiro alienígena
                # que atingiu a borda da tela

    def alien_drawn(self):
        """Desenha cada alienígena na tela usando o método blitme."""

        # Desenha os alienígenas presentes no grupo de alienígenas na tela
        self.aliens.draw(
            self.screen
            # Desenha os alienígenas presentes no
            # grupo de alienígenas na tela
        )
