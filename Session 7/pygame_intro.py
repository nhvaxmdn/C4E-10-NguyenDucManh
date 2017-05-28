import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Sukoban")
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255,255,255))
    pygame.display.flip()
