from skyfield.api import load, wgs84

# Create a timescale and ask the current time.
ts = load.timescale()
t = ts.now()

# Load the JPL ephemeris DE421 (covers 1900-2050).
planets = load('de421.bsp')
earth, mars = planets['earth'], planets['mars']
saturn = planets['Saturn Barycenter']

your_location = earth + wgs84.latlon(53.21667, -1.01667)  # Nottinghamshire Coordinates: 53.21667, -1.01667

# Get Mars position from your location
astrometric = your_location.at(t).observe(mars)
apparent = astrometric.apparent()
alt, az, distance = apparent.altaz()

print(f'Mars altitude: {alt.degrees:.2f}°')
print(f'Mars azimuth: {az.degrees:.2f}°')

if alt.degrees > 0:
    print("Mars is above the horizon!")
else:
    print("Mars is below the horizon.")