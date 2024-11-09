import numpy as np 
import pickle
import streamlit as st
import pandas as pd

#loading model from pickle
load_model = pickle.load(open('./trained_model.sav','rb'))

#creating a function for prediciton 
def house_price_prediction(input_data) :
    input_data =np.asarray(input_data)
    #8120000	
    # Predict price
    predicted_price = load_model.predict(input_data)

    print("Predicted Price:", predicted_price[0])

def main():
    #title 
    st.title("House Price Prediction")
    #gettign the input data 
    st.sidebar.header("Input Parameters")
    area = st.sidebar.number_input("Area (sq. ft)", min_value=500, max_value=10000, value=6000, step=100)
    bedrooms = st.sidebar.slider("Bedrooms", min_value=1, max_value=10, value=3)
    bathrooms = st.sidebar.slider("Bathrooms", min_value=1, max_value=5, value=2)
    stories = st.sidebar.slider("Stories", min_value=1, max_value=3, value=1)
    mainroad = st.sidebar.selectbox("Mainroad", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
    guestroom = st.sidebar.selectbox("Guestroom", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
    basement = st.sidebar.selectbox("Basement", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
    hotwaterheating = st.sidebar.selectbox("Hot Water Heating", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
    airconditioning = st.sidebar.selectbox("Air Conditioning", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
    parking = st.sidebar.slider("Parking", min_value=0, max_value=4, value=1)
    prefarea = st.sidebar.selectbox("Preferred Area", options=[0, 1], format_func=lambda x: "Yes" if x else "No")

    # Furnishing type dropdown
    furnishing_type = st.sidebar.selectbox("Furnishing Type", options=["Furnished", "Semi-Furnished", "Unfurnished"])

    # Set furnishing options based on selection
    furnished = furnishing_type == "Furnished"
    semi_furnished = furnishing_type == "Semi-Furnished"
    unfurnished = furnishing_type == "Unfurnished"

    #code for prediction 
    prediction = ''

    if st.button('Get Price') :
        prediction = house_price_prediction([area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnished,semi_furnished,unfurnished])

    st.success(prediction)  


if __name__ == '__main__' :
    main()
    
