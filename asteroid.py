class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__()
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", x, y, radius, width=2)

    def update(self, dt):
        x += (velocity * dt)
        y += (velocity * dt)