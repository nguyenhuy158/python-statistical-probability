import pygame

pygame.init()
size = (800, 600)
display = pygame.display.set_mode(size)

back = (0, 0, 0)
white = (255, 255, 255)
pygame.display.set_caption('Game')
gameOn = True
clock = pygame.time.Clock()

while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
        # print(event)

    display.fill((1, 2, 3))
    pygame.draw.line(display, white, [10, 0], [200, 200], 2)
    pygame.display.update()

    clock.tick(60)

pygame.quit()
