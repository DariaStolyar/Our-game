import pygame

window = w, h = 800, 800
FPS = 15
maps_d = 'MAPS'
tile_size = 32


class Lab:
    def __init__(self, filename):
        self.map = []
        with open(f"{maps_d}/{filename}") as input_file:
            for line in input_file:
                self.map.append(list(map(int, line.split())))
        self.h = len(self.map)
        self.w = len(self.map[0])
        self.tile_size = tile_size

    def render(self, screen):
        colors = {0: (0, 0, 0), 1: (255, 0, 0)}
        for y in range(self.h):
            for x in range(self.w):
                rect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                screen.fill(colors[self.get_tile_id((x, y))], rect)

    def get_tile_id(self, position):
        return self.map[position[1]][position[0]]


class Game:
    def __init__(self, lab):
        self.lab = lab

    def render(self, screen):
        self.lab.render(screen)


def main():
    pygame.init()
    pygame.display.set_caption('Caper')
    screen = pygame.display.set_mode(window)

    lab = Lab('uo.txt')
    game = Game(lab)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                k = 'uo.txt'
                game = Game(lab)
        screen.fill((0, 0, 0))
        game.render(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()