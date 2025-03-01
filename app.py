import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(
    page_title="Building Energy Prediction",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="collapsed"  # Hide sidebar by default
)


def landing_page():
    # Set page configuration
    # st.set_page_config(page_title="Building Energy Prediction", page_icon="🏙️", layout="wide")

    # Background and styling
    st.markdown(
        """
        <style>
            body {
                background-color: #f0f2f6;
            }
            .main-title {
                font-size: 52px;
                font-weight: bold;
                color: #2E8B57;
                text-align: center;
                margin-top: 30px;
            }
            .sub-title {
                font-size: 22px;
                color: #555;
                text-align: center;
                margin-top: -10px;
            }
            .get-started {
                display: flex;
                justify-content: center;
                margin-top: 50px;
            }
            .get-started button {
                background-color: #2E8B57;
                color: white;
                padding: 12px 35px;
                font-size: 18px;
                font-weight: bold;
                border: none;
                border-radius: 25px;
                cursor: pointer;
                transition: background-color 0.3s ease, transform 0.2s ease;
            }
            .get-started button:hover {
                background-color: #1e7042;
                transform: translateY(-3px);
            }
            .footer {
                font-size: 14px;
                text-align: center;
                margin-top: 50px;
                color: #aaa;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<p class="main-title">Building Energy Prediction</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Smart Analysis and Forecasting for Energy Efficiency</p>', unsafe_allow_html=True)

    # Get Started Button
    st.markdown('<div class="get-started"><form action="/main" target="_self"><button type="submit">Get Started</button></form></div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown('<p class="footer">© 2025 Building Energy Prediction. All rights reserved.</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    landing_page()
