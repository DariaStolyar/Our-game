import pygame
pygame.init()
size = [500, 600]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

my_image = pygame.image.load("data/owls.png").convert_alpha()

# уменьшил до размера (100, 100)
scaled_image = pygame.transform.scale(my_image, (100, 100))
rotated_image = pygame.transform.rotate(my_image, 0)
screen.blit(rotated_image, (100, 150))
pygame.display.flip()
angle = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pass
            r = True
            while r:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        r = False
                angle += 1
                screen.fill((0, 0, 0))
                rotated_image = pygame.transform.rotate(my_image, angle)
                screen.blit(rotated_image, (100, 150))

                pygame.display.flip()
                clock.tick(10)
pygame.quit()