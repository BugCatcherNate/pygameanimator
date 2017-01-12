import pygame

class animator:

    def __init__(self, sizex, sizey, spritefile):

        #self.displaysurf = displaysurf
        self.spritefile = pygame.image.load(spritefile)
        self.count = 0
        self.sizex = sizex
        self.sizey = sizey


    def spriteget(self, rectangle):
        
        rect = pygame.Rect(rectangle)
        self.spritefile = self.spritefile.convert()
        image = pygame.Surface(rect.size).convert()
        image.blit(self.spritefile, (0, 0), rect)  
        colorkey = (255,255,255)
        image.set_colorkey(colorkey)
        return image

    def stationary(self):
        img = self.spriteget((0, 0, self.sizex, self.sizey))
        return img       

    def animation(self, spritesheetrow, numsprites):

        img = self.spriteget((self.count * self.sizex, spritesheetrow * self.sizey, self.sizex, self.sizey))
        self.count += 1
        if self.count > numsprites-1:
            self.count = 0
        return img    


