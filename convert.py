import rasterio
import numpy as np
import pandas as pd
from rasterio.transform import from_origin

# Load prediction data
df = pd.read_csv("future_predictions.csv")

# Extract lat, lon, and predicted values
lat = df["decimalLatitude"]
lon = df["decimalLongitude"]
predictions = df["Predictions"]

# Define raster resolution
pixel_size = 0.05  # Adjust based on dataset resolution
x_min, y_max = lon.min(), lat.max()  # Top-left corner of raster
transform = from_origin(x_min, y_max, pixel_size, pixel_size)

# Define raster grid dimensions
cols = int((lon.max() - lon.min()) / pixel_size) + 1
rows = int((lat.max() - lat.min()) / pixel_size) + 1

# Create empty raster
raster = np.full((rows, cols), np.nan)

# Map predictions to raster grid
for i in range(len(df)):
    row = int((y_max - lat[i]) / pixel_size)
    col = int((lon[i] - x_min) / pixel_size)
    raster[row, col] = predictions[i]

# Save as GeoTIFF
with rasterio.open(
    "future_predictions.tif",
    "w",
    driver="GTiff",
    height=rows,
    width=cols,
    count=1,
    dtype=rasterio.float32,
    crs="EPSG:4326",  # WGS84 coordinate system
    transform=transform,
) as dst:
    dst.write(raster, 1)

print("GeoTIFF saved as 'future_predictions.tif'. You can now visualize it in QGIS.")
