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
