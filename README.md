Habitat Prediction of Indian Peafowl Using MaxEnt
This project models and predicts the habitat suitability of the Indian Peafowl (Pavo cristatus) in India using the MaxEnt algorithm. It leverages geospatial environmental data (such as BIO1: annual mean temperature and BIO12: annual precipitation), species occurrence records, and visualization tools like QGIS.

**Project Structure
main.py: Runs the MaxEnt model and generates habitat suitability predictions.

extract.py: Extracts coordinate and environmental variable data from raw sources.

convert.py: Converts spatial layers or formats (e.g., raster to ASCII) required for MaxEnt.

data/: Contains species occurrence points and environmental variable layers (e.g., BIO1, BIO12).

outputs/: Stores habitat suitability maps and model results.

visualization/: QGIS project files or exported map images.

*Tools & Technologies
MaxEnt: Species distribution modeling using presence-only data.

QGIS: Used for spatial data visualization and map generation.

Python: Data preprocessing, formatting, and automation.

Geospatial Data: Bioclimatic variables (from sources like WorldClim), elevation layers, etc.

🔧 How to Run
Ensure all required Python libraries are installed (e.g., rasterio, pandas, numpy).

Run extract.py to gather and prepare input data.

Use convert.py to format geospatial layers for MaxEnt.

Execute main.py to generate the prediction model.

Visualize the outputs in QGIS for map-based analysis.

*Input Data
Species Coordinates: Latitude and longitude of confirmed peafowl sightings.

Bioclimatic Variables:

BIO1: Annual Mean Temperature

BIO12: Annual Precipitation
(and others if used)

🗺️ Outputs
Habitat suitability raster maps

CSV or tabular model summaries

QGIS visualization files

*Use Cases
Ecological research and conservation planning

Habitat shift analysis under climate change

Policy support for wildlife protection

