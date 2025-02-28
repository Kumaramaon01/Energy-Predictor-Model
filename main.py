import streamlit as st

# Set page config
st.set_page_config(page_title="Building Energy Predictor", page_icon="🏢", layout="wide")

# Page Title
st.title("🏢 Building Energy Predictor")

st.write("""
This application predicts **Energy Use Intensity (EUI)**, **Total Energy Outcome**, and **Peak Load** for a building using Machine Learning models.
Fill in the inputs on the left, and the predicted values will appear on the right.
""")

# Divide page into 70% (left) and 30% (right)
col1, col2 = st.columns([0.7, 0.3])

# ---------------- LEFT COLUMN (Inputs) ----------------
with col1:
    # Building Typology Section
    st.subheader("🏛️ Building Inputs")

    # Row 1 - Location & Typology
    colA, colB = st.columns(2)
    with colA:
        location = st.selectbox(
            "Location",
            [
                "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", 
                "Kolkata", "Ahmedabad", "Pune", "Jaipur", "Lucknow", 
                "Surat", "Indore", "Nagpur", "Bhopal", "Ludhiana", 
                "Patna", "Chandigarh", "Coimbatore", "Kochi", "Visakhapatnam"
            ]
        )
    with colB:
        building_typology = st.selectbox(
            "Building Typology",
            ["Office", "Residential", "Hospital", "Retail", "Hotel", "Education"]
        )

    # Row 2 - Above Grade Area & Below Grade Area
    colC, colD = st.columns(2)
    with colC:
        above_grade_area = st.number_input("Above Grade Area (m²)", min_value=100, value=1000)
    with colD:
        below_grade_area = st.number_input("Below Grade Area (m²)", min_value=0, value=0)

    # Envelope Characteristics Section
    st.subheader("🏗️ Envelope Characteristics")

    # Single row for WWR, U-Value, Window Type
    colE, colF, colG = st.columns(3)
    with colE:
        window_wall_ratio = st.text_input("WWR (0-1)", value="0.4")
    with colF:
        u_value = st.number_input("U-Value (W/m²·K)", min_value=0.1, value=1.5)
    with colG:
        window_type = st.selectbox(
            "Window Type",
            ["Single Glazed", "Double Glazed", "Triple Glazed", "Low-E Coated"]
        )

    # Internal Loads Section
    st.subheader("⚡ Internal Loads")

    # Single row for Lighting Load and Equipment Load
    colH, colI = st.columns(2)
    with colH:
        lighting_load = st.number_input("Lighting Load (W/m²)", min_value=0.0, value=10.0)
    with colI:
        equipment_load = st.number_input("Equipment Load (W/m²)", min_value=0.0, value=15.0)

    # Predict Button
    predict_button = st.button("🔍 Predict Energy Performance")

# ---------------- RIGHT COLUMN (Outputs) ----------------
with col2:
    st.subheader("📊 Predicted Outputs")

    if predict_button:
        # Placeholder predictions (replace with actual ML prediction logic)
        eui = 150
        energy_outcome = "High"
        peak_load = 350

        st.metric(label="EUI (kWh/m²/yr)", value=f"{eui:.2f}")
        st.metric(label="Energy Outcome", value=energy_outcome)
        st.metric(label="Peak Load (kW)", value=f"{peak_load:.1f}")
    else:
        st.write("👈 Fill the inputs and click **Predict Energy Performance** to see the results.")

# Footer
st.markdown("---")
st.markdown("🔬 Developed as part of a Machine Learning Energy Modeling Application")
