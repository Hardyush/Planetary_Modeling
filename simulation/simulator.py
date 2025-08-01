from models.planet import Planet
import numpy as np

G = 6.67430e-11  # gravitational constant

def update_positions(planets, dt):
    n = len(planets)
    for i in range(n):
        force = np.zeros(2)
        for j in range(n):
            if i == j:
                continue
            r_vec = planets[j].position - planets[i].position
            r = np.linalg.norm(r_vec)
            force += G * planets[i].mass * planets[j].mass * r_vec / r**3
        # acceleration = F / m
        acc = force / planets[i].mass
        planets[i].velocity += acc * dt
    for planet in planets:
        planet.position += planet.velocity * dt