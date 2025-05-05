import streamlit as st
import pickle
import numpy as np

with open('random_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

st.title("Automobile Price Prediction")

st.divider()

st.markdown("""
This is a simple web app for predicting the price of an automobile based on various features such as wheel base, length, width, curb weight, engine size, bore, and horsepower.
""")

st.divider()

# Define the input fields for the user to enter values
wheel_base = st.number_input("Wheel Base (in inches)", min_value=80.0, max_value=150.0, step=0.1)
length = st.number_input("Length (in inches)", min_value=140.0, max_value=210.0, step=0.1)
width = st.number_input("Width (in inches)", min_value=60.0, max_value=80.0, step=0.1)
curb_weight = st.number_input("Curb Weight (in pounds)", min_value=1500, max_value=5000, step=1)
engine_size = st.number_input("Engine Size (in cubic inches)", min_value=50, max_value=500, step=1)
bore = st.number_input("Bore (in inches)", min_value=2.0, max_value=5.0, step=0.1)
horsepower = st.number_input("Horsepower", min_value=50, max_value=500, step=1)


user_input = np.array([[
    wheel_base,
    length,
    width,
    curb_weight,
    engine_size,
    bore,
    horsepower
]])


if st.button('Predict Price'):
    
    predicted_price = model.predict(user_input)
    
    st.write(f"Predicted Car Price: ${predicted_price[0]:,.2f}")
# hello
# hi