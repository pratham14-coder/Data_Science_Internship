import streamlit as st
import numpy as np
import pickle

# Load the trained model and scaler
model = pickle.load(open("random_forest_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Define feature names based on your dataset
feature_names = [
   'acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y', 'gyro_z'
]

st.title("🏃 Walk or Run Activity Classifier")
st.write("Enter the feature values below to predict whether the activity is **Walking** or **Running**.")

# Input form
user_input = []
for feature in feature_names:
    val = st.number_input(f"Enter value for {feature}", value=0.0)
    user_input.append(val)

# Prediction
if st.button("Predict Activity"):
    # Convert user input to a numpy array
    input_array = np.array([user_input])
    
    # Debug: Show the user input
    st.write("User input:", user_input)
    
    # Scale the input using the same scaler
    input_scaled = scaler.transform(input_array)
    
    # Debug: Show the scaled input
    st.write("Scaled input:", input_scaled)
    
    # Get the model prediction
    prediction = model.predict(input_scaled)[0]
    
    # Debug: Show the raw prediction result
    st.write("Model prediction (raw output):", prediction)
    
    # Show the activity prediction
    if prediction == 0:
        st.success("🧍 The predicted activity is: **Walking**")
    else:
        st.success("🏃 The predicted activity is: **Running**")
