import pandas as pd
import pickle
import json
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

def train_and_save_model():
    print("Loading dataset from 'clean_ola.csv'...")
    try:
        df = pd.read_csv('clean_ola.csv')
    except FileNotFoundError:
        print("Error: 'clean_ola.csv' not found. Please ensure the file is in the same directory.")
        return

    # Extract unique values for frontend dropdowns
    unique_locations = sorted(set(df['Pickup_Location'].unique()) | set(df['Drop_Location'].unique()))
    unique_vehicles = sorted(df['Vehicle_Type'].unique().tolist())

    print(f"Found {len(unique_locations)} locations and {len(unique_vehicles)} vehicle types.")


    # 1. Train Booking Value Model
    # INPUTS: Pickup, Drop, AND Vehicle_Type

    print("Training Booking Value Model...")
    X_booking = df[['Pickup_Location', 'Drop_Location', 'Vehicle_Type']]
    y_booking = df['Booking_Value']

    # Preprocessor for Booking (Expects 3 columns)
    prep_booking = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), ['Pickup_Location', 'Drop_Location', 'Vehicle_Type'])
        ],
        remainder='drop'
    )

    model_booking = Pipeline(steps=[
        ('preprocessor', prep_booking),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1))
    ])
    
    model_booking.fit(X_booking, y_booking)


    # 2. Train Ride Distance Model
    # INPUTS: Pickup AND Drop ONLY (No Vehicle)

    print("Training Ride Distance Model...")
    
    # CRITICAL: We explicitly select only 2 columns here.
    # This ensures the model never learns about 'Vehicle_Type'.
    X_distance = df[['Pickup_Location', 'Drop_Location']] 
    y_distance = df['Ride_Distance']

    # Preprocessor for Distance (Expects 2 columns)
    prep_distance = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), ['Pickup_Location', 'Drop_Location'])
        ],
        remainder='drop'
    )

    model_distance = Pipeline(steps=[
        ('preprocessor', prep_distance),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1))
    ])
    
    model_distance.fit(X_distance, y_distance)


    # 3. Save Artifacts

    print("Saving updated models to 'ola_model.pkl'...")
    with open('ola_model.pkl', 'wb') as f:
        pickle.dump({
            'model_booking': model_booking,
            'model_distance': model_distance
        }, f)

    # Save metadata for the frontend dropdowns
    metadata = {
        'locations': unique_locations,
        'vehicle_types': unique_vehicles
    }
    
    with open('model_metadata.json', 'w') as f:
        json.dump(metadata, f)

    print("Success! Models have been decoupled and saved.")
    print("You can now run 'streamlit run ola_app.py' without errors.")

if __name__ == "__main__":
    train_and_save_model()