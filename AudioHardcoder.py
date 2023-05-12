import os, pygame
pygame.init()
def output(path):
    sound = pygame.mixer.Sound(path)
    target=path.split('.')[-2]+'.txt'
    with open(target, 'a') as file:
        file.write(f"pygame.mixer.Sound({sound.get_raw()})")
