import pandas as pd
import joblib

# Load trained model
model = joblib.load("maxent_model.pkl")  # Update with actual model path

# Load the future dataset
future_data = pd.read_csv("FB.csv")  # Update filename

# Load the features used during training
expected_features = ["bio1", "bio12"]  # Update with actual feature names used in training

# Ensure the column names match exactly
future_data = future_data.rename(columns={"bio1_2041-2060": "bio1", "bio12_2041-2060": "bio12"})

# Drop unnecessary columns
future_data = future_data[["decimalLatitude", "decimalLongitude"] + expected_features]

# Make predictions
predictions = model.predict(future_data.drop(columns=["decimalLatitude", "decimalLongitude"]))

# Add predictions to DataFrame
future_data["Predictions"] = predictions

# Save new dataset
future_data.to_csv("future_predictions.csv", index=False)
print("Prediction successful! File saved as 'future_predictions.csv'.")
