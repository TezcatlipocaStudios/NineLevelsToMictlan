import pygame, os
pygame.init()
def output(path):
    sprite = pygame.image.load(path)
    string = pygame.image.tobytes(sprite, 'RGBA')
    size = sprite.get_size()
    target=path.split('.')[-2]+'.txt'
    with open(target, 'a') as file:
        file.write(f"pygame.image.frombytes({string}, {size}, 'RGBA')")

output(os.path.join("Assets", "PG-13.png"))