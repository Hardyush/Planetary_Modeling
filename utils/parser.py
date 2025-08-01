import pandas as pd

def load_planet_data(filepath):
    df = pd.read_excel(filepath)
    planets = []
    for _, row in df.iterrows():
        planet = {
            'name': row['Planet Name'],
            'mass': row['Mass (kg)'],
            'radius': row['Radius (m)'],
            'orbit_radius': row['Orbit Radius (m)'],
            'velocity': row['Initial Velocity (m/s)'],
            'angle': row['Initial Angle (deg)']
        }
        planets.append(planet)
    return planets