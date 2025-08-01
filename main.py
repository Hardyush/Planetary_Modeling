from utils.parser import load_planet_data
from models.planet import Planet
from simulation.simulator import update_positions
from visualizations.plot import plot_system

def main():
    planets_data = load_planet_data('data/sample_input.xlsx')
    planets = [Planet(**data) for data in planets_data]

    for _ in range(1000):
        update_positions(planets, dt=60)  # simulate per minute

    plot_system(planets)

if __name__ == "__main__":
    main()