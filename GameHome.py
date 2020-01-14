import pygame
from gameSettings import *
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        #self.image_surface = pygame.Surface()
        self.clock = pygame.time.Clock()
        self.lastClick = []
        self.P1 = Player('X',0,0)
        self.P2 = Player('O',0,0)
        #self.all_sprites =
        self.Board = GRID()

        self.turn = 'x'

    def quit (self):
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               self.quit()

                # handle mouse input calling functino that updates the screen with image
            if event.type == pygame.MOUSEBUTTONDOWN:
                MouseX = pygame.mouse.get_pos()[0] // TILESIZE# get x, y position of mouse click
                MouseY = pygame.mouse.get_pos()[1] // TILESIZE

                #self.lastClick.append ((MouseX,MouseY))

                self.drawPlayer(MouseX, MouseY) # this also updates the board
                #print(f" {MouseX}, {MouseY}")


    def update(self):
        self.Board.printGrid()
        self.Board.checkWin()
        pass


    def run(self):
        self.Running = True

        while self.Running and self.Board.turn <9:

            self.events()
            self.update()
            self.draw()



    def draw(self):
        self.drawGrid()

        pygame.display.flip()

    def drawGrid(self):

        for x in range(0, WIDTH, TILESIZE):
               pygame.draw.line(self.screen, (0, 40, 40), (x, 0), (x, HEIGHT),4)

        for y in range(0, HEIGHT, TILESIZE):
               pygame.draw.line(self.screen, (0, 40, 40), (0, y), (WIDTH, y),4)

    def drawPlayer(self,x,y): # also updates 2d grid
        #note x,y come in a raw grid coords. ex: 0,0 is first square ...


        if self.turn == 'x':
            self.screen.blit(self.P1.image,(x * TILESIZE,y* TILESIZE))
            self.Board.xMove(x,y)
            self.turn = 'o'
        else:
            #self.P2.update_pos(x,y)
            self.screen.blit(self.P2.image,(x * TILESIZE,y * TILESIZE))
            self.Board.oMove(x, y)
            self.turn = 'x'



class Player:
    def __init__(self,name,x,y):

        self.n = name
        self.x = x
        self.y = y
        self.rect = pygame.rect.Rect(self.x,self.y,GRIDHEIGHT,GRIDWIDTH) #Rect(0,0,GRIDWIDTH,GRIDHEIGHT)

        if name == 'O':
            self.image = pygame.image.load('o.png')
        else:
            self.image = pygame.image.load('x.png')

    #def update_pos(self,x,y):
    #    self.rect = pygame.rect.Rect(x * TILESIZE,y * TILESIZE,GRIDHEIGHT,GRIDWIDTH)
    def show(self):
       # pygame.Surface.blit(self.image, self.rect)

        pass




class GRID:
    def __init__(self):


        self.grid = [['0'for x in range(3)] for j in range(3)]
        self. P1 = 'X'
        self. P2 = 'O'
        self.LastMove = [(0,0)]
        self.turn = 0


    def xMove(self, row, col):
        self.grid[row][col] = self.P1
        self.LastMove.append((row,col))
        self.turn += 1

    def oMove(self,row,col):
        self.grid[row][col] = self.P2
        self.LastMove.append((row,col))
        self.turn += 1



    def checkWin(self):
        self.checkRow()
        self.checkCol()
        self.checkDiag()

        print(self.LastMove)

    def checkRow(self): # checks if the entire row is a player, returns true or false, should return player?!?!

        if self.turn == 0:
            pass
        else:
            #row = self.LastMove[self.moveNum][0] # get the x position of the last move
            for i in range(3):
                if self.grid[self.LastMove[self.turn][0]][i] == self.P1: # checks for 'X' move
                    print("x true")
                else:
                    print("x False")


    def checkCol(self):
        pass
    def checkDiag(self):
        pass

    def printGrid(self):

        for x in self.grid:
            print(x)
        print("\n",end='')

