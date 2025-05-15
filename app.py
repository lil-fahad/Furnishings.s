
import streamlit as st
import requests
import datetime

st.title("🏠 AI-Powered Home Furnishing Advisor")

st.header("1. Upload Your House Plan")
uploaded_file = st.file_uploader("Upload an image of your house plan (JPG, PNG)", type=["jpg", "jpeg", "png"])
if uploaded_file:
    st.image(uploaded_file, caption="Uploaded House Plan", use_container_width=True)
    st.success("Image uploaded successfully!")

    st.header("2. Simulated Room Detection")
    st.info("Select the rooms detected in your house plan:")
    rooms = st.multiselect("Detected Rooms", ["Living Room", "Bedroom", "Kitchen", "Dining Room", "Bathroom"])

    if rooms:
        st.header("3. Recommended Furniture")
        for room in rooms:
            st.subheader(f"🛋️ {room}")
            response = requests.get("https://api.escuelajs.co/api/v1/products")
            if response.status_code == 200:
                products = response.json()
                furniture_items = [item for item in products if item['category']['name'] == "Furniture"]
                for item in furniture_items[:3]:
                    st.markdown(f"**{item['title']}**")
                    st.image(item['images'][0], width=200)
                    st.write(f"Price: ${item['price']}")
                    st.write("---")
            else:
                st.error("Failed to fetch furniture data.")
    else:
        st.warning("Please select at least one room to view furniture recommendations.")

st.header("4. Book a Designer")
designer = st.selectbox("Choose a Designer", ["Alice Johnson - Modern Interiors", "Bob Smith - Classic Luxury"])
date = st.date_input("Select a Date", datetime.date.today())
time = st.time_input("Select a Time")
notes = st.text_area("Additional Notes")

if st.button("Confirm Booking"):
    st.success(f"Booking confirmed with {designer} on {date} at {time}.")
    st.write("**Notes:**", notes)
