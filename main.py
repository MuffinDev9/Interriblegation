import pygame

pygame.init()

display_width = 800
display_height = 600
class colour:
    black = (0, 0, 0)
    silver = (192, 192, 192)
    gray = (128, 128, 128)
    white = (255, 255, 255)
    maroon = (128, 0, 0)
    red = (255, 0, 0)
    purple = (128, 0, 128)
    fuchsia = (255, 0, 255)
    green = (0, 128, 0)
    lime = (0, 255, 0)
    olive = (128, 128, 0)
    yellow = (255, 255, 0)
    navy = (0, 0, 128)
    blue = (0, 0, 255)
    teal = (0, 128, 128)
    aqua = (0, 255, 255)

class spritePos:
    detectorPos = [display_width/2-128/2, display_height/2-128/2]
    playerPos = [display_width/2-64, display_height/2-64]

mainWindow = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Interriblegation')

clock = pygame.time.Clock()
crashed = False

lieDetector = pygame.image.load("Images/lieDetectorBase.png", "Detector")

def loadDetector(x, y):
    mainWindow.blit(lieDetector, (x, y))

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
    mainWindow.fill(colour.gray)
    loadDetector(spritePos.detectorPos[0], spritePos.detectorPos[1])

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
