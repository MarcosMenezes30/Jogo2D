class BulletManager:
    def __init__(self, bullets):
        self.bullets = bullets

    def check_bullets(self):
        """Verifica os eventos projeteis lançados
            e atualiza suas posições"""

        for bullet in (
            self.bullets.sprites()
                ):  # Atualiza a posição de cada projétil no grupo de projéteis
            bullet.draw_bullet()  # Desenha cada projétil na tela

            self.bullets.update()  # Atualiza a posição de cada projétil
            # no grupo de projéteis
            for (
                bullet
            ) in self.bullets.copy():  # Verifica se algum projétil
                # saiu da tela
                if (
                    bullet.rect.bottom <= 0
                ):  # Se o projétil saiu da tela (parte inferior do retângulo
                    # do projétil é menor ou igual a 0)
                    self.bullets.remove(
                        bullet
                    )  # Remove o projétil do grupo de projéteis
