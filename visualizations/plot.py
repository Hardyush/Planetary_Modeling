import matplotlib.pyplot as plt

def plot_system(planets):
    plt.figure(figsize=(8, 8))
    for planet in planets:
        plt.plot(planet.position[0], planet.position[1], 'o', label=planet.name)
    plt.legend()
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.grid()
    plt.axis('equal')
    plt.show()