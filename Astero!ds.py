import pygame, os, math

# Store hex codes for colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen size
scr_h = 900
scr_w = 1600
overlap = 7

def update():
    all_sprites.update()
    bullets.update()

# Implement classes
class Rocket(pygame.sprite.Sprite):
    # Rocket ship utility
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # Call Sprite initializer
        self.image = pygame.image.load("rocket.png")
        self.left, self.right, self.forward, self.backward = False, False, False, False
        self.angle, self.x, self.y, self.w, self.h, self.p_r, self.pnt_dist, self.rot = 90, 800, 450, 42, 42, 5, 38, 17
        self.max_vel, self.init_vel, self.cntr_stack = 25, 5, 1
        self.b_counter, self.f_counter = self.init_vel, self.init_vel
        self.rect = (self.x, self.y)

    def update(self):
        # Move rocket based on keys
        if self.left:
            self.angle -= self.rot
        if self.right:
            self.angle += self.rot

        if self.forward:
            self.x -= self.f_counter * math.cos(math.radians(self.angle))
            self.y -= self.f_counter * math.sin(math.radians(self.angle))
            self.f_counter += self.cntr_stack
            if self.f_counter > self.max_vel: self.f_counter = self.max_vel
        elif not self.f_counter <= self.init_vel:
            if self.f_counter > self.init_vel: self.f_counter -= 3 * self.cntr_stack
            self.x -= self.f_counter * math.cos(math.radians(self.angle))
            self.y -= self.f_counter * math.sin(math.radians(self.angle))
        if self.backward:
            self.x += self.b_counter * math.cos(math.radians(self.angle))
            self.y += self.b_counter * math.sin(math.radians(self.angle))
            self.b_counter += self.cntr_stack
            if self.b_counter > self.max_vel: self.b_counter = self.max_vel
        elif not self.b_counter <= self.init_vel:
            if self.b_counter > self.init_vel: self.b_counter -= 3 * self.cntr_stack
            self.x += self.b_counter * math.cos(math.radians(self.angle))
            self.y += self.b_counter * math.sin(math.radians(self.angle))

        # Keep ship on screen
        if self.x > scr_w - overlap:
            self.x = 0 + overlap
        elif self.x < 0 + overlap:
            self.x = scr_w - overlap

        if self.y > scr_h - overlap:
            self.y = 0 + overlap
        elif self.y < 0 + overlap:
            self.y = scr_h - overlap

        self.rect = (self.x, self.y)

    def draw(self, surface):
        surface.blit(self, (self.x, self.y))

class Asteroid(pygame.sprite.Sprite):
    # Astero!d utility
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # Call Sprite initializer

class Projectile(object):
    def __init__(self, x, y, dir, vel, range = scr_w, color = WHITE, radius = 3, max = 10):
        self.x = x
        self.y = y
        self.dir = dir
        self.vel = vel
        self.range = range
        self.color = color
        self.radius = radius
        self.max = 10

    def draw(self):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

# Initialize game engine
pygame.init()

# Set up display
pygame.display.set_caption("Astero!ds")
surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Other necessary variables
run = True
clock = pygame.time.Clock()
rocket = Rocket()
all_sprites = pygame.sprite.RenderPlain(rocket)
bullets = []

while run:
    # Keeps the while loop from going too quickly and consuming too much RAM
    clock.tick(20)

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

    if keys[pygame.K_SPACE] and not bullets.len() > Projectile.max:

        bullets.append()

    # Update screen
    update()
    surface.fill(BLACK)

    all_sprites.draw(surface)
    pygame.draw.circle(surface, WHITE, [int((rocket.x + rocket.w / 2) - rocket.pnt_dist * math.cos(math.radians(rocket.angle))), int((rocket.y + rocket.h / 2) - rocket.pnt_dist * math.sin(math.radians(rocket.angle)))], rocket.p_r)
    for bullet in bullets:
        pygame.draw.circle(surface, bullet.color, (bullet.x, bullet.y), bullet.radius)
    pygame.display.flip()

pygame.quit()



