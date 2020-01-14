import pygame
from GameHome import *
pygame.init()
pygame.font.init()
pygame.font.get_default_font()
# width , height in pixels of display
# displayConfig = (600,600)
# window = pygame.display.set_mode(displayConfig)
# rwidth = 600
# rheight = 25
# rect1 = pygame.Rect(0,150,rwidth,rheight)
# rect2 = pygame.Rect(0,displayConfig[0]-200,rwidth,rheight)
# vert1 = pygame.Rect(150,0,rheight,rwidth)
# vert2 = pygame.Rect(displayConfig[1] -200,0,rheight,rwidth)
# #square = pygame.draw.rect(window,(0,255,255),rect1)
# #pygame.Fon
# def checkMouseBox(x,y):
#     if  y <150:
#         if x < 150:
#             print("Top Left")
#         elif x > 150 and x < 400:
#             print("Top Middle")
#         elif x > 400:
#             print("Top Right")
#     elif y > 150 and y < 400:
#         if x < 150:
#             print("Middle Left")
#         elif x > 150 and x < 400:
#             print("Middle Middle")
#         elif x > 400:
#             print("Middle Right")
#     elif y > 400 :
#         if x < 150:
#             print("Bot Left")
#         elif x > 150 and x < 400:
#             print("Bot Middle")
#         elif x > 400:
#             print("Bot Right")
#
# # loop to keep window open
# Running = True
# count = 0
# text = f"count: {count}"
# #font = pygame.font.Font(text,20)
# while Running:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             Running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             count += 1
#             #print(f'clicked {count}')
#             print(f" x: {MouseX} y:{MouseY}")
#             checkMouseBox(MouseX,MouseY)
#
#
#     MouseX = pygame.mouse.get_pos()[0]
#     MouseY = pygame.mouse.get_pos()[1]
#     #pygame.Surface.fill()
#     #square.blit()
#     #for row in range(3):
#     pygame.draw.rect(window, (0, 0, 255), rect1)
#     pygame.draw.rect(window, (0, 255,0), rect2)
#     pygame.draw.rect(window, (255, 0,0), vert1)
#     pygame.draw.rect(window, (200, 0,0), vert2)
#     # pygame.font.Font.render(font,text,0,(0,10,10))
#
#



    # pygame.display.update()

   # window.fill((0,0,0))
    #pygame.display.update()
global clicked
grid = GRID()
grid.printGrid()


grid.printGrid(   )
g = Game()


g.run()