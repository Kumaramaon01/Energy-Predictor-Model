import streamlit as st

st.set_page_config(
    page_title="Building Energy Prediction",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="collapsed"  # Hide sidebar by default
)

# Custom CSS for better visual appearance
st.markdown("""
    <style>
        body {
            background-color: #f9f9f9;
        }
        .main-title {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 15px;
            margin-bottom: 20px;
            font-weight: bold;
        }
        .main-title span {
            font-size: 48px;
        }
        .gradient-text {
            background: -webkit-linear-gradient(left, #0078D7, #00BCD4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: bold;
        }
        .section-header {
            color: #0078D7;
            font-size: 22px;
            font-weight: bold;
            margin-top: 10px;
            margin-bottom: 10px;
            border-bottom: 2px solid #0078D7;
            padding-bottom: 4px;
        }
        .footer {
            font-size: 14px;
            text-align: center;
            color: #555;
        }
    </style>
""", unsafe_allow_html=True)

# Title with gradient text and icon
st.markdown(
    """
    <div class="main-title" style="font-size: 10px; display: flex; align-items: center; gap: 10px;">
        <span></span>
        <span class="gradient-text" style="font-size: 40px; font-weight: bold;">Building Energy Predictor</span>
    </div>
    """,
    unsafe_allow_html=True
)

# st.write("""
# This application predicts **Energy Use Intensity (EUI)**, **Total Energy Outcome**, and **Peak Load** for buildings using advanced Machine Learning models.
# Fill in the inputs on the left to see the predictions.
# """)

# Divide page into 65% (left) and 35% (right) for better balance
col1, col2 = st.columns([0.65, 0.35])

# ---------------- LEFT COLUMN (Inputs) ----------------
with col1:
    st.markdown('<div class="section-header">🏛️ Building Inputs</div>', unsafe_allow_html=True)

    # Row 1 - Location & Typology
    colA, colB, colAA = st.columns(3)
    with colA:
        location = st.selectbox("📍 Location", [
            "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", 
            "Kolkata", "Ahmedabad", "Pune", "Jaipur", "Lucknow", 
            "Surat", "Indore", "Nagpur", "Bhopal", "Ludhiana", 
            "Patna", "Chandigarh", "Coimbatore", "Kochi", "Visakhapatnam"
        ])
    with colB:
        building_typology = st.selectbox("🏢 Building Typology", [
            "Office", "Residential", "Hospital", "Retail", "Hotel", "Education"
        ])
    with colAA:
        orient = st.selectbox(
            "🧭 Building Orientation (degrees)", 
            ["0", "45", "90", "135", "180", "225", "270", "315"],
            index=0
        )

    # Row 2 - Above & Below Grade Area
    colC, colD = st.columns(2)
    with colC:
        above_grade_area = st.number_input("🏗️ Above Grade Area (m²)", min_value=100, value=1000)
    with colD:
        below_grade_area = st.number_input("🏗️ Below Grade Area (m²)", min_value=0, value=0)

    # Envelope Characteristics
    st.markdown('<div class="section-header">🧱 Envelope Characteristics</div>', unsafe_allow_html=True)

    colE, colF, colG, colH = st.columns(4)
    with colE:
        window_wall_ratio = st.slider("🪟 Window-to-Wall Ratio (0-1)", 0.0, 1.0, 0.4, 0.01)
    with colF:
        wall_u_value = st.number_input("🌡️ Wall-U-Value (W/m²·K)", min_value=0.1, value=1.5)
    with colG:
        roof_u_value = st.number_input("🌡️ Roof-U-Value (W/m²·K)", min_value=0.1, value=1.5)
    with colH:
        window_u_value = st.number_input("🌡️ Window-U-Value (W/m²·K)", min_value=0.1, value=1.5)

    # Internal Loads
    st.markdown('<div class="section-header">⚡Internal Loads</div>', unsafe_allow_html=True)

    colI, colJ = st.columns(2)
    with colI:
        lighting_load = st.number_input("💡 Lighting Load (W/m²)", min_value=0.0, value=10.0)
    with colJ:
        equipment_load = st.number_input("🔌 Equipment Load (W/m²)", min_value=0.0, value=15.0)

    # Predict Button
    st.markdown("<br>", unsafe_allow_html=True)
    predict_button = st.button("🔍 Predict Energy Performance", help="Click to run the prediction model")

# ---------------- RIGHT COLUMN (Outputs) ----------------
with col2:
    st.markdown('<div class="section-header">📊 Predicted Outputs</div>', unsafe_allow_html=True)

    if predict_button:
        # Placeholder predictions (replace this with your ML model predictions)
        eui = 142.5
        energy_outcome = "Medium"
        peak_load = 326.4

        st.success("✅ Prediction Complete")
        st.metric(label="🔋EUI (kWh/m².Yr)", value=f"{eui:.2f}", delta="Predicted")
        st.metric(label="🌍Energy Outcome", value=energy_outcome)
        st.metric(label="⚡Peak Load (kW)", value=f"{peak_load:.1f}")

    else:
        st.info("👈 Fill the inputs and click **Predict Energy Performance** to generate predictions.")

# Footer
st.markdown("---")
st.markdown('<div class="footer">🔬 Developed as part of a Machine Learning Energy Modeling Application | © 2025</div>', unsafe_allow_html=True)
