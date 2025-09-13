# Example code from https://rhodesmill.org/skyfield/
from skyfield.api import load

# Create a timescale and ask the current time.
ts = load.timescale()
t = ts.now()

# Load the JPL ephemeris DE421 (covers 1900-2050).
planets = load('de421.bsp')
earth, mars = planets['earth'], planets['mars']
saturn = planets['Saturn Barycenter']
# What's the position of Mars, viewed from Earth?
astrometric = earth.at(t).observe(mars)
ra, dec, distance = astrometric.radec()

print(ra)
print(dec)
print(distance)
print(f'Mars is at RA {ra} and Dec {dec}, distance {distance.km} km')

# What's the position of Saturn, viewed from Earth?
astrometric = earth.at(t).observe(saturn)
ra, dec, distance = astrometric.radec()

print(ra)
print(dec)
print(distance)
print(f'Saturn is at RA {ra} and Dec {dec}, distance {distance.km} km')