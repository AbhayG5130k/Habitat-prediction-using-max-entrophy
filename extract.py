import rasterio
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import os

# Load the bird occurrence dataset
bird_csv = "C:/Users/Lenovo/Desktop/Dp/bird.csv"  # Update this path
bird_data = pd.read_csv(bird_csv)

# Check if necessary columns exist
if "decimalLatitude" not in bird_data.columns or "decimalLongitude" not in bird_data.columns:
    raise ValueError("Dataset must contain 'decimalLatitude' and 'decimalLongitude' columns.")

# Convert to GeoDataFrame
geometry = [Point(xy) for xy in zip(bird_data["decimalLongitude"], bird_data["decimalLatitude"])]
bird_gdf = gpd.GeoDataFrame(bird_data, geometry=geometry, crs="EPSG:4326")

# Filter out invalid coordinates
bird_gdf = bird_gdf[(bird_gdf["decimalLatitude"].between(-90, 90)) & 
                     (bird_gdf["decimalLongitude"].between(-180, 180))]

print(f"✅ Loaded {len(bird_gdf)} bird occurrence records.")

# Bioclimatic variables to extract
bioclimatic_vars = ["bio1", "bio12"]
raster_folder = r"C:/Users/Lenovo/Desktop/Dp/wc2.1_2.5m_bio"   # Change this to your folder path

# Check if raster files exist
for bio_var in bioclimatic_vars:
    raster_path = f"{raster_folder}/{bio_var}.tif"
    if not os.path.exists(raster_path):
        raise FileNotFoundError(f"❌ Raster file NOT found: {raster_path}")
    print(f"Found raster file: {raster_path}")

# Extract climate data
def extract_climate_values(point, raster_path):
    with rasterio.open(raster_path) as src:
        lon, lat = point.x, point.y
        row, col = src.index(lon, lat)  # Convert lat/lon to raster indices
        value = src.read(1)[row, col]   # Extract pixel value
        print(f"Extracting at ({lon}, {lat}) -> Row: {row}, Col: {col}, Value: {value}")
        return value

# Apply extraction for each raster
for bio_var in bioclimatic_vars:
    raster_path = f"{raster_folder}/{bio_var}.tif"
    print(f"Extracting {bio_var} values...")
    bird_gdf[bio_var] = bird_gdf["geometry"].apply(lambda point: extract_climate_values(point, raster_path))
    print(f"Extracted {bio_var} for {bird_gdf[bio_var].notna().sum()} records.")

# Save results to a new CSV file
output_csv = "C:/Users/Lenovo/Desktop/Dp/bird_occurrences_with_climate.csv"
bird_gdf.drop(columns=["geometry"]).to_csv(output_csv, index=False)

print(f"Climate data extracted and saved to: {output_csv}")
