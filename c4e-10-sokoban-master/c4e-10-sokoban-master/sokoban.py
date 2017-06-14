import pygame
from game_object.Game import Game
from game_object.map import Map
from game_object.pusher import Pusher
from game_object.box import  Box
from game_object.dest import Dest




#object = Class()
sokoban = Game()
sokoban.map = Map(5, 5)
sokoban.pusher = Pusher(1, 1)
sokoban.box = Box(2, 2)
sokoban.dest = Dest(3, 3)
sokoban.console_draw()

pygame.init()
screen = pygame.display.set_mode((640, 640))
done = False
pusher_image = pygame.image.load("images/pusher.png")
box_image = pygame.image.load("images/box.png")
ground_image = pygame.image.load("images/ground.png")
dest_image = pygame.image.load("images/dest.png")
sokoban.pusher.image = pusher_image
sokoban.box.image = box_image
sokoban.dest.image = dest_image


pixel = 64

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        sokoban.handle_input(event)

    screen.fill((0,0,0))
    sokoban.draw(screen, ground_image)
    pygame.display.flip()
