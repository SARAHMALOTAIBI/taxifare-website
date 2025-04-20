import streamlit as st
import requests
from datetime import datetime


st.title("TaxiFareModel Frontend")


st.markdown("""
This is a simple web app to predict taxi fares in New York City.
Enter the ride details below, and we'll fetch the predicted fare for you!
""")

pickup_date = st.date_input("Pickup Date", value=datetime.now().date())
pickup_time = st.time_input("Pickup Time", value=datetime.now().time())
pickup_longitude = st.number_input("Pickup Longitude", value=-73.991842)
pickup_latitude = st.number_input("Pickup Latitude", value=40.741983)
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.987403)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.748433)
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=8, value=1)


pickup_datetime = f"{pickup_date} {pickup_time}"

url = 'https://taxifare.lewagon.ai/predict'


if st.button("Predict Fare"):

    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    # Call the API
    response = requests.get(url, params=params)


    if response.status_code == 200:
        prediction = response.json().get("fare", None)
        if prediction:
            st.success(f"Predicted Fare: ${prediction:.2f}")
        else:
            st.error("Failed to retrieve a prediction from the API.")
    else:
        st.error(f"API request failed with status code: {response.status_code}")
