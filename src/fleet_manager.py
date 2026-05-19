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
