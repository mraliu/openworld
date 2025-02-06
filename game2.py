# Make simple pygame window
# https://www.spriters-resource.com/snes/zombiesneighbours
import pygame
pygame.init()


class Screen():
    def __init__(self, w, h, setImage, setMask):
        self.width = w
        self.height = h
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.x = self.width/2
        self.y = self.height/2
        self.speed = 8

        self.game_surface = pygame.image.load(setImage).convert() #load the image

        self.game_surface_mask = pygame.image.load(setMask).convert() #load the image
        self.game_mask = pygame.mask.from_surface(self.game_surface_mask)

        self.img_w = self.game_surface.get_width()
        self.img_h = self.game_surface.get_height()
        self.scale = 1.5

        self.game_surface = pygame.transform.scale(self.game_surface, (self.img_w*self.scale, self.img_h*self.scale))
        self.game_rect = self.game_surface.get_rect(center=(self.x, self.y))

    def move(self):
        if pressed_keys[pygame.K_w]: #up
            self.y = self.y + self.speed
        if pressed_keys[pygame.K_s]: #down
            self.y = self.y - self.speed
        if pressed_keys[pygame.K_a]: #left
            self.x = self.x + self.speed
        if pressed_keys[pygame.K_d]: #right
            self.x = self.x - self.speed

class Player():
    def __init__(self, setImage):
        sprite_sheet = pygame.image.load(setImage).convert_alpha()
        self.sprite_width = 15
        self.sprite_height = 32
        self.walking_down_sprites_down = [
            sprite_sheet.subsurface(pygame.Rect(86+(x * self.sprite_width), 5, self.sprite_width, self.sprite_height)) 
            for x in range(5)  # Assuming there are 4 walking down sprites
            ]
        self.walking_down_sprites_right = [
            sprite_sheet.subsurface(pygame.Rect(86+(x * self.sprite_width), 44, self.sprite_width, self.sprite_height)) 
            for x in range(5)  # Assuming there are 4 walking down sprites
            ]
        self.walking_down_sprites_up = [
            sprite_sheet.subsurface(pygame.Rect(86+(x * self.sprite_width), 86, self.sprite_width, self.sprite_height)) 
            for x in range(5)  # Assuming there are 4 walking down sprites
            ]
        self.walking_down_sprites_left = [
            sprite_sheet.subsurface(pygame.Rect(86+(x * self.sprite_width), 124, self.sprite_width, self.sprite_height)) 
            for x in range(5)  # Assuming there are 4 walking down sprites
            ]
        


        self.current = self.walking_down_sprites_down[0]
        
    def move(self):
        if pressed_keys[pygame.K_w]: #up
            self.current = self.walking_down_sprites_up[0]
        if pressed_keys[pygame.K_s]: #down
            self.current = self.walking_down_sprites_down[0]
        if pressed_keys[pygame.K_a]: #left
            self.current = self.walking_down_sprites_left[0]
        if pressed_keys[pygame.K_d]: #right
            self.current = self.walking_down_sprites_right[0]

game = Screen(800, 600, "map1.png", "map1_mask.png")
player1 = Player("Zeke.png")

clock = pygame.time.Clock()
running = True
while running:
    pressed_keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.screen.fill((0, 0, 0))

    game.move()
    player1.move()
    game.screen.blit(game.game_surface, (game.x-game.game_surface.get_width()/2, game.y-game.game_surface.get_height()/2))

    # Player

    game.screen.blit(player1.current, (game.width/2-(player1.sprite_width/2), game.height/2-(player1.sprite_height/2)))

    pygame.draw.circle(game.screen, (255, 0, 0), (game.width/2, game.height/2), 2) # Player

    clock.tick(60)
    pygame.display.flip()

pygame.quit()