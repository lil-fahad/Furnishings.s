
import streamlit as st
import datetime

st.title("Ultimate AI Furnishing Advisor")

# 1. House Layout Upload Section
st.header("Upload Your House Layout")
uploaded_file = st.file_uploader("Upload image or PDF", type=["jpg", "jpeg", "png", "pdf"])
if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Layout", use_column_width=True)
    st.success("File uploaded successfully. Ready for AI analysis.")

# 2. Simulated AI Layout Analysis Section
if uploaded_file:
    if st.button("Analyze Layout with AI"):
        st.subheader("AI Detected Rooms and Furniture Suggestions")
        st.write("**Rooms Detected:** Living Room, Kitchen, Bedroom")
        st.write("**Suggested Furnishings:**")
        st.write("- Modern Sofa")
        st.write("- Wooden Dining Table")
        st.write("- King Size Bed")

# 3. Furniture Catalog Section
st.header("Furniture Catalog")
furniture_catalog = [
    {"name": "Modern Sofa", "price": "$1200"},
    {"name": "Wooden Dining Table", "price": "$850"},
    {"name": "King Size Bed", "price": "$1500"},
]
for item in furniture_catalog:
    st.markdown(f"- **{item['name']}** - {item['price']}")

# 4. Designer Booking Section
st.header("Book a Designer")
designer_choice = st.selectbox(
    "Select a Designer",
    ["Alice Johnson - Modern Interiors", "Bob Smith - Classic Luxury"]
)
booking_date = st.date_input("Select a Date", datetime.date.today())
booking_time = st.time_input("Select a Time")
booking_notes = st.text_area("Additional Notes")

if st.button("Confirm Booking"):
    st.success(f"Booking confirmed with {designer_choice} on {booking_date} at {booking_time}.")
    st.write("**Notes:**", booking_notes)

st.markdown("---")
st.write("Powered by Streamlit - Ready for Deployment on Streamlit.io")
