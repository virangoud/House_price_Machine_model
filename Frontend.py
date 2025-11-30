import streamlit as st
import base64
import json
import requests
st.sidebar.title("Menu")
st.sidebar.image("newlogo.jpg", use_container_width=True)



def add_bg(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>
        /* Full app background */
        .stApp {{
            background: linear-gradient(
                rgba(0,0,0,0.5),
                rgba(0,0,0,0.5)
            ), url("data:image/png;base64,{encoded}") no-repeat center center fixed;
            background-size: cover !important;
        }}

        /* Make content area transparent so background shows fully */
        .block-container {{
            background: transparent !important;
            padding: 2rem;
        }}

        /* Remove white header/footer spacing */
        header, footer {{
            background: transparent !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
 

add_bg("background.jpg")

#metro_city                0
#locality_area             0
#house_type                0
#bhk_type                  0
#total_area_sqft           0
#num_bathrooms             0
#extraspace_and_parking    0
#furnishing                0
#floor_no                  0
#accessibility_index 

# Description
st.header("Welcome to The House Price Predictor App!")
st.header("Know your Dream House Price:")

# Input fields
metro_city  = st.selectbox("Select Location:",  ["Mumbai", "Delhi NCR", "Bengaluru", "Chennai", "Hyderabad", "Kolkata", "Pune", "Ahmedabad"]
)
localities = {
    "Mumbai": ["Andheri", "Bandra", "Borivali", "Dadar", "Juhu"],
    "Delhi NCR": ["Connaught Place", "Saket", "Dwarka", "Karol Bagh", "Rohini"],
    "Bengaluru": ["Whitefield", "Koramangala", "Indiranagar", "HSR Layout", "Jayanagar"],
    "Chennai": ["T Nagar", "Velachery", "Adyar", "Anna Nagar", "Tambaram"],
    "Hyderabad": ["Banjara Hills", "Gachibowli", "Madhapur", "Kukatpally", "Jubilee Hills"],
    "Kolkata": ["Salt Lake", "New Town", "Ballygunge", "Park Street", "Tollygunge"],
    "Pune": ["Kothrud", "Hinjewadi", "Viman Nagar", "Baner", "Kharadi"],
    "Ahmedabad": ["Satellite", "Bopal", "Navrangpura", "Thaltej", "Maninagar"]
}

locality_area = st.selectbox("Select Locality:", localities[metro_city])
house_type = st.selectbox(
    "House type:",
    ["Apartment", "Independent_House", "Villa", "Studio", "row_house", "other"]
)

total_area_sqft = st.number_input("Enter the area (in square feet):", min_value=500, max_value=4000, step=100)
bhk_type= st.segmented_control("Type of BHK:", ["1BHK","2BHK","3BHK","4BHK","5BHK","5BHK+"],selection_mode="single")
num_bathrooms = st.radio("Number of Bathrooms:", [1,2,3,4])
options= ["Furnished", "Semi-Furnished", "Unfurnished"]
furnishing =st.segmented_control(
    "Furnishing Status:",options,selection_mode="single")
extraspace_parking = st.segmented_control("Extra Space and Parking:",['no_extra', 'extra_space_only', 'extra_space+car_parking','car_parking_only'],selection_mode="single")
accessibility_index = st.slider("Accessibility Index:", min_value=2, max_value=8, value=5, step=1)



st.caption("Thank you for Visiting")
if st.button("Predict"):
    payload = {
        "metro_city": metro_city,
        "locality_area": locality_area,
        "house_type": house_type,
        "bhk_type": bhk_type,
        "total_area_sqft": total_area_sqft,
        "num_bathrooms": num_bathrooms,
        "extraspace_and_parking":extraspace_parking,
        "furnishing": furnishing,
        "accessibility_index": accessibility_index
    }
    with st.spinner("Predicting price... Please wait ⏳"):
        try:
            res = requests.post(
                "http://localhost:5000/predict",
                data=json.dumps(payload),
                headers={"Content-Type": "application/json"}
            )

            if res.status_code == 200:
                price = res.json().get("prediction")
                st.success(f"Predicted Price: ₹ {price:,.2f}")
            else:
                st.error("Error: " + res.text)

        except Exception as e:
            st.error(f"Backend connection failed: {e}")
