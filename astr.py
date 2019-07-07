import pygame, os, math

# Implement classes
class Rocket(pygame.sprite.Sprite):
    # Rocket ship utility
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # Call Sprite initializer
        self.image = pygame.image.load("rocket.png")
        self.left, self.right, self.forward, self.backward = False, False, False, False
        self.angle, self.x, self.y, self.w, self.h, self.p_r, self.pnt_dist = 90, 300, 300, 60, 42, 5, 38
        self.rect = (self.x, self.y)

    def update(self):
        # Move rocket based on keys
        if self.left:
            self.angle -= rot
        if self.right:
            self.angle += rot
        if self.forward:
            self.x -= vel * math.cos(math.radians(self.angle))
            self.y -= vel * math.sin(math.radians(self.angle))
        if self.backward:
            self.x += vel * math.cos(math.radians(self.angle))
            self.y += vel * math.sin(math.radians(self.angle))

        # Keep ship on screen
        if self.x > scr_w - self.w:
            self.x = scr_w - self.w
        elif self.x < 0:
            self.x = 0

        if self.y > scr_h - self.h:
            self.y = scr_h - self.h
        elif self.y < 0:
            self.y = 0

        self.rect = (self.x, self.y)

    def draw(self, surface):
        surface.blit(self, (self.x, self.y))
        pygame.draw.circle(surface, WHITE, ((self.x + self.w / 2) + self.pnt_dist * math.cos(math.radians(self.angle)), (self.y + self.h / 2) + self.pnt_dist * math.sin(math.radians(self.angle))), self.p_r)


class Asteroid(pygame.sprite.Sprite):
    # Astero!d utility
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # Call Sprite initializer

# Initialize game engine
pygame.init()

# Set up display
pygame.display.set_caption("Astero!ds")
surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Store hex codes for colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize variables
run = True
vel = 25
clock = pygame.time.Clock()
rocket = Rocket()
all_sprites = pygame.sprite.RenderPlain(rocket)
rot = 17

# Screen size
scr_h = 900
scr_w = 1600

while run:
    # Keeps the while loop from going too quickly and consuming too much RAM
    clock.tick(10)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    if keys[pygame.K_LEFT]:
        rocket.left = True
    else:
        rocket.left = False

    if keys[pygame.K_RIGHT]:
        rocket.right = True
    else:
        rocket.right = False

    if keys[pygame.K_UP]:
        rocket.forward = True
    else:
        rocket.forward = False

    if keys[pygame.K_DOWN]:
        rocket.backward = True
    else:
        rocket.backward = False

    if keys[pygame.K_SPACE]:
        rocket.shooting = True
    else:
        rocket.shooting = False

    # Drawing objects
    surface.fill(BLACK)
    font = pygame.font.Font(None, 36)

    # Update screen
    all_sprites.update()
    all_sprites.draw(surface)
    pygame.display.flip()

pygame.quit()



