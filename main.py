import streamlit as st

# import functions as fx

st.set_page_config()
st.title("Vijaya Homes for elders")
st.write("Welcome! This is the Home page", )

col1, empt_col, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.image("oldperson.jpeg")
with col2:
    st.write("Welcome family of Sohan! He is an ever cheerful soul")
    st.text("Full Name: Sohan Katragadda")
    st.text("Age: 85")
    st.text("Gender: Male")
    st.text("Personal C.no: 9100343137")


