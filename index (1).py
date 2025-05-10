import pandas as pd
import numpy as np
import geopandas as gpd
from shapely.geometry import Point
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
import joblib

# Load presence data
data_path = "C:/Users/Lenovo/Desktop/Dp/bird_occurrences_with_climate.csv"
data = pd.read_csv(data_path)

# Select climate variables
features = ["bio1", "bio12"]  # Adjust as needed
X_presence = data[features]
y_presence = np.ones(len(data))  # Presence labels (1)

# Generate Random Background Points
num_background = len(data)  # Equal to presence points
lon_min, lon_max = data["decimalLongitude"].min(), data["decimalLongitude"].max()
lat_min, lat_max = data["decimalLatitude"].min(), data["decimalLatitude"].max()

background_points = pd.DataFrame({
    "decimalLongitude": np.random.uniform(lon_min, lon_max, num_background),
    "decimalLatitude": np.random.uniform(lat_min, lat_max, num_background),
})

# Extract climate values for background points (you must do this using raster extraction)
background_points["bio1"] = np.random.uniform(data["bio1"].min(), data["bio1"].max(), num_background)
background_points["bio12"] = np.random.uniform(data["bio12"].min(), data["bio12"].max(), num_background)

X_background = background_points[features]
y_background = np.zeros(len(background_points))  # Absence labels (0)

# Combine Presence & Background Data
X = pd.concat([X_presence, X_background])
y = np.concatenate([y_presence, y_background])

# Split into training & test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train MaxEnt Model (Logistic Regression)
model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)

# Predict Habitat Suitability
y_pred = model.predict_proba(X_test)[:, 1]

# Evaluate Model
auc = roc_auc_score(y_test, y_pred)
print(f"✅ Model AUC Score: {auc:.4f}")

# Save Model
model_path = "C:/Users/Lenovo/Desktop/Dp/maxent_model.pkl"
joblib.dump(model, model_path)
print(f"✅ Model saved at: {model_path}")
