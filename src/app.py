import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from scipy.interpolate import griddata

# Fix random seed for reproducibility
np.random.seed(42)

# Generate sample temperature data based on latitude
n_points = 1000
lons = np.random.uniform(-180, 180, n_points)
lats = np.random.uniform(-90, 90, n_points)
base_temp = 30 * np.cos(np.radians(lats))  # Warmer near equator, colder near poles
noise = np.random.normal(0, 10, n_points)  # Add random variation
temps = base_temp + noise  # Temperature in °C, approx. -60 to 60

# Create a grid for interpolation
lon_grid, lat_grid = np.meshgrid(np.linspace(-180, 180, 100), np.linspace(-90, 90, 50))
temp_grid = griddata((lons, lats), temps, (lon_grid, lat_grid), method='cubic')

# Create figure and Basemap
plt.figure(figsize=(12, 6))
m = Basemap(projection='merc', llcrnrlat=-60, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, resolution='c')
m.drawcoastlines()
m.drawcountries()

# Fill continents and water with neutral colors
m.fillcontinents(color='lightgray', lake_color='lightgray')
m.drawmapboundary(fill_color='white')

# Convert grid to map coordinates
x_grid, y_grid = m(lon_grid, lat_grid)

# Transform scalar data to mask water
masked_temp = np.ma.masked_where(np.isnan(m.transform_scalar(temp_grid, lon_grid[0], lat_grid[:, 0], 100, 50, masked=True)), temp_grid)

# Plot the continuous heatmap only on land
heatmap = m.contourf(x_grid, y_grid, masked_temp, levels=20, cmap='RdYlBu_r')
plt.colorbar(heatmap, label='Temperature (°C)', extend='both')

# Set title
plt.title('Annual Average Temperature Heatmap (Basemap)')

# Save and show
plt.savefig('output/basemap_heatmap.png')
plt.show()