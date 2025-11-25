import streamlit as st
import pandas as pd
import pickle
import json
import time

# Page Configuration
st.set_page_config(
    page_title="Ola Ride Predictor",
    page_icon="🚖",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f1f1f;
        color: #B9F200;
        font-weight: bold;
        border: none;
        padding: 0.75rem;
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: #333333;
        color: #B9F200;
    }
    .result-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        border-left: 5px solid #B9F200;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("🚖 Ola Fare Predictor")
st.caption("Machine Learning Powered Estimation")

# --- Load Data & Model ---
@st.cache_resource
def load_artifacts():
    try:
        # Load the trained model
        with open('ola_model.pkl', 'rb') as f:
            models = pickle.load(f)
        
        # Load the unique locations and vehicles (derived from the dataset)
        with open('model_metadata.json', 'r') as f:
            metadata = json.load(f)
            
        return models, metadata
    except FileNotFoundError:
        st.error("Model files not found! Please run 'train_model.py' first.")
        return None, None

models, metadata = load_artifacts()

if models and metadata:
    # --- Input Form ---
    with st.container():
        st.subheader("Plan Your Ride")
        
        col1, col2 = st.columns(2)
        
        with col1:
            pickup = st.selectbox(
                "📍 Pickup Location", 
                options=metadata['locations'],
                index=0,
                help="Select your starting point"
            )
        
        with col2:
            drop = st.selectbox(
                "🏁 Drop Location", 
                options=metadata['locations'],
                index=1, # Default to second option so it's different from pickup
                help="Select your destination"
            )

        vehicle = st.radio(
            "🚗 Vehicle Type",
            options=metadata['vehicle_types'],
            horizontal=True
        )

        # Predict Button
        if st.button("Calculate Fare"):
            if pickup == drop:
                st.warning("⚠️ Pickup and Drop locations cannot be the same.")
            else:
                with st.spinner("Calculating best route..."):
                    # Simulate a tiny delay for effect
                    time.sleep(0.5)
                    
                    # Prepare input for the model
                    input_booking = pd.DataFrame({
                        'Vehicle_Type': [vehicle],
                        'Pickup_Location': [pickup], 
                        'Drop_Location': [drop] 
                        
                    })
                    input_distance = pd.DataFrame({
                        'Pickup_Location': [pickup], 
                        'Drop_Location': [drop],
                        
                    })
                    # Make Predictions
                    pred_price = models['model_booking'].predict(input_booking)[0]
                    pred_distance = models['model_distance'].predict(input_distance)[0]
                    
                    # Display Results
                    st.write("---")
                    st.subheader("Trip Details")
                    
                    res_col1, res_col2 = st.columns(2)
                    
                    with res_col1:
                        st.markdown(f"""
                        <div class="result-card">
                            <p style="color:gray; font-size:0.9rem; margin-bottom:5px;">ESTIMATED FARE</p>
                            <h2 style="color:#2c3e50; margin:0;">₹ {pred_price:.0f}</h2>
                        </div>
                        """, unsafe_allow_html=True)
                        
                    with res_col2:
                        st.markdown(f"""
                        <div class="result-card" style="border-left-color: #3498db;">
                            <p style="color:gray; font-size:0.9rem; margin-bottom:5px;">RIDE DISTANCE</p>
                            <h2 style="color:#2c3e50; margin:0;">{pred_distance:.1f} km</h2>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    st.info(f"Route: **{pickup}** ➝ **{drop}** via **{vehicle}**")

else:
    st.info("Please generate the model files to proceed.")