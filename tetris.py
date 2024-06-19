import pygame, sys
from game import Game

pygame.init()

#cor
dark_blue = (44, 44, 127)

#JANELA DO JOGO
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

#relogio para o fps funcionar
clock = pygame.time.Clock()

game = Game()

#LOOP PRINCIPAL 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
#Desenho da tela
    screen.fill(dark_blue)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)


