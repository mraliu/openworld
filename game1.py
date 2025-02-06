# Make simple pygame window
# https://www.spriters-resource.com/snes/zombiesneighbours
import pygame
pygame.init()


class Screen():
    def __init__(self, w, h, setImage):
        self.width = w
        self.height = h
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.x = self.width/2
        self.y = self.height/2
        self.speed = 8
        self.game_surface = pygame.image.load(setImage).convert() #load the image
        self.img_w = self.game_surface.get_width()
        self.img_h = self.game_surface.get_height()
        self.scale = 1.5

        self.game_surface = pygame.transform.scale(self.game_surface, (self.img_w*self.scale, self.img_h*self.scale))
        self.game_rect = self.game_surface.get_rect(center=(self.x, self.y))

 
game = Screen(800, 600, "map1.png")
clock = pygame.time.Clock()
running = True
while running:
    pressed_keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pressed_keys[pygame.K_w]: #up
        game.y = game.y + game.speed
    if pressed_keys[pygame.K_s]: #down
        game.y = game.y - game.speed
    if pressed_keys[pygame.K_a]: #left
        game.x = game.x + game.speed
    if pressed_keys[pygame.K_d]: #right
        game.x = game.x - game.speed
    
    
    game.screen.fill((0, 0, 0))

    game.screen.blit(game.game_surface, (game.x-game.game_surface.get_width()/2, game.y-game.game_surface.get_height()/2))



    # game.screen.blit(game.game_surface, (game.x-(game.game_surface.get_width/2), game.y-(game.game_surface.get_height/2)))

    pygame.draw.circle(game.screen, (255,255,0), (game.width/2, game.height/2), 10) # Player

    
    clock.tick(60)
    pygame.display.flip()

pygame.quit()