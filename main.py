import pygame, sys, random

# General Setup 
pygame.init()
clock = pygame.time.Clock()

# Game Window / Screen
screen_width = 960
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Target Practice')
background = pygame.image.load('bg_blue.jpg') 
pygame.mouse.set_visible(False) 

# Classes
class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect() 
        self.shot = pygame.mixer.Sound('shot.wav') 
    def shoot(self): 
        self.shot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)
    def update(self): 
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite): 
     def __init__(self, picture_path, pos_x, pos_y, ):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y] 

# Objects 

#Crosshair 
crosshair = Crosshair('crosshair_white.png')
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

# Target
target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target('duck.png', random.randrange(0, screen_width), random.randrange(0, screen_height))
    target_group.add(new_target)


#  Game Loop
while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()
            

# Visuals / Drawings 
    pygame.display.flip()
    screen.blit(background, (0, 0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)
  


