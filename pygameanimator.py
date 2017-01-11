 
import pygame
 
class spritesheet(object):
    def __init__(self, filename):
    
            self.sheet = pygame.image.load(filename).convert()
        
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)  
        colorkey = (255,255,255)
        image.set_colorkey(colorkey)
        return image
  