import numpy as np

class Planet:
    def __init__(self, name, mass, radius, orbit_radius, velocity, angle):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.position = np.array([
            orbit_radius * np.cos(np.radians(angle)),
            orbit_radius * np.sin(np.radians(angle))
        ])
        self.velocity = np.array([
            -velocity * np.sin(np.radians(angle)),
            velocity * np.cos(np.radians(angle))
        ])