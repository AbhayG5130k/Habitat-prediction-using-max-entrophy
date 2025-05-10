import rioxarray as rxr

# Load the raster file
file_path = r"C:\Users\Lenovo\Desktop\Dp\wc2.1_2.5m_bioc_MPI-ESM1-2-HR_ssp245_2041-2060.tif"
future_bioclim = rxr.open_rasterio(file_path)

# Extract BIO1 and BIO12
bio1 = future_bioclim.sel(band=1)
bio12 = future_bioclim.sel(band=12)

# Remove metadata attributes causing the issue
bio1.attrs = {}  
bio12.attrs = {}

# Ensure the extracted layers have a band dimension
bio1 = bio1.expand_dims(dim="band")
bio12 = bio12.expand_dims(dim="band")

# Save the corrected files
bio1.rio.to_raster("bio1_2041-2060.tif")
bio12.rio.to_raster("bio12_2041-2060.tif")

print("BIO1 and BIO12 extracted and saved successfully!")
