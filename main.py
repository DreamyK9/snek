#!/bin/python
# Example file showing a circle moving on screen
import pygame

class Player:
    def __init__(self):
        self.size = (50, 50)
        self.direction = pygame.Vector2(1, 0)
        self.speed = 5
        self.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.sprite = pygame.Rect(self.pos, self.size)

    def update(self):
        self.sprite.update(self.pos, self.size)

    def draw(self):
        pygame.draw.rect(screen, "green", self.sprite) 

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player = Player()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey25")

    player.update()
    player.draw()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.direction.update(0, -1)
    if keys[pygame.K_s]:
        player.direction.update(0, 1)
    if keys[pygame.K_a]:
        player.direction.update(-1, 0)
    if keys[pygame.K_d]:
        player.direction.update(1, 0)

    # move character
    player.pos.update(player.pos + player.speed * player.direction)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
