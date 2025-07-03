import pygame
from game import Game

def main():
    pygame.init()
    size, sq = 8, 60
    screen = pygame.display.set_mode((size*sq, size*sq))
    pygame.display.set_caption('Chess')

    game = Game(rows=size, cols=size, sq_size=sq)
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.handle_click(pygame.mouse.get_pos())

        game.board.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
