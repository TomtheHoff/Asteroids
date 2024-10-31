import pygame
from constants import *
from asteroidfield import *
from player import Player
from shoot import *



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)



    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if player.collisions(asteroid):
                print("Game over!")
                return
            
        for shot in shots:
            if shot.collides_with(asteroid):
                shot.kill()
                asteroid.kill()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)



        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

        


if __name__ == "__main__":
    main()
