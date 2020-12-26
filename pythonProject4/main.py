import os
import sys
import pygame
import pygame_gui

maps_d = 'MAPS'
tile_size = 32
pygame.init()
size = width, height = 620, 560
screen = pygame.display.set_mode(size)

background = pygame.Surface((620, 560))
color = 'coral'
background.fill(pygame.Color(color))
manager = pygame_gui.UIManager((620, 560))
screen.blit(background, (0, 0))

start = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 10), (300, 300)),
    text='START',
    manager=manager)


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


class Hero:
    def __init__(self, position, filename):
        self.x, self.y = position
        self.map = []
        with open(f"{maps_d}/{filename}") as input_file:
            for line in input_file:
                self.map.append(list(map(int, line.split())))
        self.h = len(self.map)
        self.w = len(self.map[0])
        self.tile_size = tile_size

    def get_position(self):
        return self.x, self.y

    def set_position(self, position):
        self.x, self.y = position

    def render(self, screen):
        if self.map[self.x - 1][self.y - 1] == 1:
            center = self.x * tile_size + tile_size // 2, self.y * tile_size + tile_size // 2
            ter = self.x * tile_size, self.y * tile_size
            pygame.draw.line(screen, (200, 200, 200), center, ter, 2)
        elif self.map[self.x + 1][self.y + 1] == 1:
            center = self.x * tile_size + tile_size // 2, self.y * tile_size + tile_size // 2
            ter = self.x * tile_size, self.y * tile_size
            pygame.draw.line(screen, (200, 200, 200), center, ter, 2)
        elif self.map[self.x][self.y + 1] == 1:
            center = self.x * tile_size + tile_size // 2, self.y * tile_size + tile_size // 2
            ter = self.x * tile_size, self.y * tile_size
            pygame.draw.line(screen, (200, 200, 200), center, ter, 2)
        elif self.map[self.x + 1][self.y] == 1:
            center = self.x * tile_size + tile_size // 2, self.y * tile_size + tile_size // 2
            ter = self.x * tile_size, self.y * tile_size
            pygame.draw.line(screen, (200, 200, 200), center, ter, 2)


class Game:
    def __init__(self, lab):
        self.lab = lab

    def render(self, screen):
        self.lab.render(screen)


clock = pygame.time.Clock()
running = True
while running:
    g = 1
    time_de = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_START_PRESS:
                if event.ui_element == start:
                    size = width, height = 650, 700
                    screen = pygame.display.set_mode(size)

                    background = pygame.Surface((650, 700))
                    background.fill(pygame.Color(color))
                    manager = pygame_gui.UIManager((650, 700))
                    switch = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((10, 10), (100, 50)),
                        text='1',
                        manager=manager)
                    switch1 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((110, 10), (100, 50)),
                        text='2',
                        manager=manager)
                    switch2 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((210, 10), (100, 50)),
                        text='3',
                        manager=manager)
                    switch3 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((310, 10), (100, 50)),
                        text='4',
                        manager=manager)
                    switch4 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((410, 10), (100, 50)),
                        text='5',
                        manager=manager)
                    switch5 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((510, 10), (100, 50)),
                        text='6',
                        manager=manager)
                    switch6 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((10, 100), (100, 50)),
                        text='7',
                        manager=manager)
                    switch7 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((110, 100), (100, 50)),
                        text='8',
                        manager=manager)
                    switch8 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((210, 100), (100, 50)),
                        text='9',
                        manager=manager)
                    switch9 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((310, 100), (100, 50)),
                        text='10',
                        manager=manager)
                    switch10 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((410, 100), (100, 50)),
                        text='11',
                        manager=manager)
                    switch11 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((510, 100), (100, 50)),
                        text='12',
                        manager=manager)
                    switch12 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((10, 200), (100, 50)),
                        text='13',
                        manager=manager)
                    switch13 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((110, 200), (100, 50)),
                        text='14',
                        manager=manager)
                    switch14 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((210, 200), (100, 50)),
                        text='15',
                        manager=manager)
                    switch15 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((310, 200), (100, 50)),
                        text='16',
                        manager=manager)
                    switch16 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((410, 200), (100, 50)),
                        text='17',
                        manager=manager)
                    switch17 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((510, 200), (100, 50)),
                        text='18',
                        manager=manager)
                    switch18 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((10, 300), (100, 50)),
                        text='19',
                        manager=manager)
                    switch19 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((110, 300), (100, 50)),
                        text='20',
                        manager=manager)
                    switch20 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((210, 300), (100, 50)),
                        text='21',
                        manager=manager)
                    switch21 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((310, 300), (100, 50)),
                        text='22',
                        manager=manager)
                    switch22 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((410, 300), (100, 50)),
                        text='23',
                        manager=manager)
                    switch23 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((510, 300), (100, 50)),
                        text='24',
                        manager=manager)
                    switch24 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((10, 400), (100, 50)),
                        text='25',
                        manager=manager)
                    switch25 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((110, 400), (100, 50)),
                        text='26',
                        manager=manager)
                    switch26 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((210, 400), (100, 50)),
                        text='27',
                        manager=manager)
                    switch27 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((310, 400), (100, 50)),
                        text='28',
                        manager=manager)
                    switch28 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((410, 400), (100, 50)),
                        text='29',
                        manager=manager)
                    switch29 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((510, 400), (100, 50)),
                        text='30',
                        manager=manager)
                    switch30 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((10, 500), (100, 50)),
                        text='31',
                        manager=manager)
                    switch31 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((110, 500), (100, 50)),
                        text='32',
                        manager=manager)
                    switch32 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((210, 500), (100, 50)),
                        text='33',
                        manager=manager)
                    switch33 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((310, 500), (100, 50)),
                        text='34',
                        manager=manager)
                    switch34 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((410, 500), (100, 50)),
                        text='35',
                        manager=manager)
                    switch35 = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((510, 500), (100, 50)),
                        text='36',
                        manager=manager)
                    pygame.display.update()
                    manager.process_events(event)
                    manager.update(time_de)
                    screen.blit(background, (0, 0))
                    manager.draw_ui(screen)
                    pygame.display.update()
                    clock.tick(60)
                    continue
                if event.ui_element == switch:
                    k = 'uo.txt'
                if event.ui_element == switch1:
                    k = 'map'
                if event.ui_element == switch2:
                    k = 'map1'
                if event.ui_element == switch3:
                    k = 'map2'
                if event.ui_element == switch4:
                    k = 'map3'
                if event.ui_element == switch5:
                    k = 'map4'
                if event.ui_element == switch6:
                    k = 'map5'
                if event.ui_element == switch7:
                    k = 'map6'
                size = width, height = 650, 700
                screen1 = pygame.display.set_mode(size)

                manager = pygame_gui.UIManager((650, 700))
                lab = Lab(k)
                game = Game(lab)
                game.render(screen1)
                pygame.display.update()
        manager.process_events(event)
    manager.update(time_de)
    manager.draw_ui(screen)
    pygame.display.update()
    clock.tick(60)
pygame.quit()