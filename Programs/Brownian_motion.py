
import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1550, 870
FPS = 100
PARTICLE_RADIUS = 10
NUM_PARTICLES = 100
MAX_SPEED = 2


# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Particle class
class Particle:
    def __init__(self, x, y, is_tracer=False):
        self.x = x
        self.y = y
        self.radius = PARTICLE_RADIUS
        self.color = RED
        self.speed = random.uniform(0, MAX_SPEED)
        self.angle = random.uniform(0, 2*math.pi)
        self.is_tracer = is_tracer
        self.path = [(x, y)]

    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        self.path.append((self.x, self.y))
    
    def collision_box(self):
        if self.x - PARTICLE_RADIUS <= 0 or self.x + PARTICLE_RADIUS >= WIDTH:
            if self.angle < math.pi:
                self.angle = math.pi - self.angle
            else:
                self.angle = 3*math.pi - self.angle

        if self.y - PARTICLE_RADIUS <= 0 or self.y + PARTICLE_RADIUS >= HEIGHT:
            self.angle = 2*math.pi - self.angle


    def particle_collision(self, other_particle):
        if math.sqrt((self.x - other_particle.x)**2 + (self.y - other_particle.y)**2) < 2*PARTICLE_RADIUS:
            self.speed, other_particle.speed = other_particle.speed, self.speed
            self.angle, other_particle.angle = other_particle.angle, self.angle


def new_part():
    return Particle(random.uniform(PARTICLE_RADIUS, WIDTH - PARTICLE_RADIUS), random.uniform(PARTICLE_RADIUS, HEIGHT - PARTICLE_RADIUS))

# Create particles
particles = []

#Associate a color with speed
def speed_color(speed):
    return 255 -    (speed/MAX_SPEED) * 255

# Choose one particle as a tracer
tracer_index = random.randint(0, NUM_PARTICLES - 1)

for i in range(NUM_PARTICLES):
    particles.append(new_part())

    if i == tracer_index:
        particles[i].is_tracer = True
        particles[i].color = WHITE


# Set up Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brownian Motion Simulation")
clock = pygame.time.Clock()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move particles and check collisions
    for particle in particles:
        particle.move()

    for i in range(len(particles)):
        particles[i].collision_box()

        for j in range(i+1, len(particles)):
            particles[i].particle_collision(particles[j])


    #Update particle color
    for particle in particles:
        if not particle.is_tracer:
            particle.color = [particle.color[0], speed_color(particle.speed), particle.color[2]]


    # Draw particles and paths
    screen.fill(BLACK)
    for particle in particles:
        pygame.draw.circle(screen, particle.color, (int(particle.x), int(particle.y)), particle.radius)

        # Draw path for the tracer
        if particle.is_tracer and len(particle.path) >= 2:
            pygame.draw.lines(screen, particle.color, False, particle.path, 2)

    pygame.display.flip()
    clock.tick(FPS)