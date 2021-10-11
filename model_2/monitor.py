import os, sys
import pygame
project = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project)

from model_2 import agent
pygame.init()
pygame.display.set_caption('Connect X')
clock = pygame.time.Clock()
(width, height) = (1100, 800)
screen = pygame.display.set_mode((width, height))
imgPath = project+"/pictures/"
rows = 6
columns = 7

game = []
for i in agent.tracker.boards:
    game.append(i)

#Upload the resources
box_icon = pygame.image.load(imgPath+"box.png")
checker1_icon = pygame.image.load(imgPath+"checker1.png")
checker2_icon = pygame.image.load(imgPath+"checker2.png")

#Board contruction
box_width = width/columns
box_height = height/rows

def place(row, column):
    pos_x = (box_width * column) + 35
    pos_y = (box_height * row) + 10
    return pos_x, pos_y

def paint_box(row, column):
    screen.blit(box_icon, (place(row, column)))

def paint_checker1(row, column):
    screen.blit(checker1_icon, (place(row, column)))

def paint_checker2(row, column):
    screen.blit(checker2_icon, (place(row, column)))

running = True
speed = 2.5
while running:
    screen.fill((0, 10, 53))
    time = pygame.time.get_ticks() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for step in range(len(game)):
        if time > (step / speed):
            for i in range(rows*columns):
                column = i % columns
                row = int(i/columns)
                if game[step][i] == 0:
                    paint_box(row, column)
                elif game[step][i] == 1:
                    paint_checker1(row, column)
                elif game[step][i] == 2:
                    paint_checker2(row, column)

    pygame.display.flip()
