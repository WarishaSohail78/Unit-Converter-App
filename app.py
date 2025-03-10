import streamlit as st
from pint import UnitRegistry


# Initialize Unit Registry
ureg = UnitRegistry()
#title of the app
st.set_page_config(page_title="Google Unit Converter", layout="centered")
st.title(":rainbow[Unit Converter App]")
# A box where users can enter a value in numbers to convert
quantity = st.number_input("Enter the value:", value=1.0)
#unit selection
unit_choices = ["meters", "kilometers", "miles", "feet", "inches", "grams", "kilograms", "pounds", "liters", "milliliters"]
from_unit = st.selectbox("Convert from:", ["Select a unit"] + unit_choices)
to_unit = st.selectbox("Convert to:", ["Select a unit"] + unit_choices)
# To convert the value
result = st.button("Convert", type="primary")
if result:
    converted_value = (quantity * ureg(from_unit)).to(to_unit)
    st.success(f"{quantity} {from_unit} = {converted_value:.4f} {to_unit}")

#adding footnote
st.write("")
st.write("")
st.write("")
st.markdown("---")  # Adds a horizontal line for separation
st.markdown("""
    <p>⭐ 
    <span style="font-size: 13px;">Developed by</span>
    <span style="font-size: 18px; font-weight: bold; color: #6c3483;">WARISHA SOHAIL</span> — 
    <span style="font-size: 12px;"> GIAIC-WED (7PM-10PM)</span></p>
    """, unsafe_allow_html=True)