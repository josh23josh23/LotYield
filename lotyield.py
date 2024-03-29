import streamlit as st
import pandas as pd

def calculate_lot_yield(average_lot_size, ndh):
    l_per_ndh = 7000 / average_lot_size
    lot_yield = ndh * l_per_ndh
    return l_per_ndh, lot_yield

# Streamlit application starts here
st.title('Lot Yield Calculator')

st.markdown("""
Enter the **Average Lot Size** and **NDH** to calculate the **L/NDH** and **Lot Yield**.
""", unsafe_allow_html=True)

# Input fields for Average Lot Size and NDH
average_lot_size = st.number_input('Average Lot Size', value=0.0, step=0.001, format="%.5f")
ndh = st.number_input('NDH', value=0.0, step=0.001, format="%.5f")

# Calculate button
if st.button('Calculate'):
    if average_lot_size > 0 and ndh > 0:
        l_per_ndh, lot_yield = calculate_lot_yield(average_lot_size, ndh)

        # Create a container for the results
        with st.container():
            st.markdown("""
            <style>
            .result-box {
                border: 2px solid #e1e4e8;
                border-radius: 5px;
                padding: 10px;
                margin: 10px 0;
            }
            </style>
            """, unsafe_allow_html=True)

            # Display the results within the styled box
            st.markdown(f"""
            <div class="result-box">
                <h3>Results:</h3>
                <p><b>L/NDH:</b> {l_per_ndh:.5f}</p>
                <p><b>Lot Yield:</b> {lot_yield:.5f} HA</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.error("Please enter positive values for Average Lot Size and NDH.")
