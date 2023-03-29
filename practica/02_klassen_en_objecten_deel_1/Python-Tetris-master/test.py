import pygame
import numpy as np

pygame.init()

width = 800
height = 600
window = pygame.display.set_mode([width,height])

mymatrixblock = np.array([[0,0,0],[0,1,1],[1,1,0],[0,0,0]])
print(mymatrixblock)

class figure:
    #constructor
    def __init__(self,shape,color) -> None:
        self.shape = shape
        self.color = color
    
    def getcolor(self):
        return self.color
    
    def getshape(self):
        return self.shape
    
    def rotate(self):
        return (np.rot90(self.shape)) #return the rotated numpy array
    

myfigure = figure(mymatrixblock,'orange')

p,q  = myfigure.shape.shape

for i in range(0,p):
    for j in range(0,q):
        if (myfigure.shape[i,j]== 1):
            pygame.draw.rect(window,myfigure.color,rect=[10*i+20,10*j+20,10,10])

myfigure = figure(myfigure.rotate(),'blue')
p,q  = myfigure.shape.shape

for i in range(0,p):
    for j in range(0,q):
        if (myfigure.shape[i,j]== 1):
            pygame.draw.rect(window,myfigure.color,rect=[10*i+200,10*j+200,10,10])

pygame.display.flip()

x=20
y=20
vel=10 #speed of movement

run=True
while run :
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    window.fill((0, 0, 0))

    for i in range(0,p):
        for j in range(0,q):
            if (myfigure.shape[i,j]== 1):
                rectmove =[10*i+200+x,10*j+200+y,10,10]
                pygame.draw.rect(window,'white',rectmove)
      
    pygame.display.update(rectmove) 

pygame.quit()
exit()

