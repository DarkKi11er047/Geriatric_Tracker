import streamlit as st
import functions as fx

st.set_page_config()

col1,empty,col2 = st.columns([0.5,0.5,2])

with col1:
    st.image("vijayahomes.webp",width=200)

with col2:
    st.title("Vijaya Homes for elders")
st.subheader("Welcome! This is the Home page")

col1, empt_col, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.image("oldperson.jpeg")
with col2:
    st.write("Welcome family of Sohan! He is an ever cheerful soul")
    st.text("Full Name: Sohan Katragadda")
    st.text("Age: 85")
    st.text("Gender: Male")
    st.text("Personal C.no: 9100343137")
    st.text("Caretaker C.no: 9246115674")

fx.sleep_check()
fx.activity_check()
fx.meds_check()
fx.hygiene_check()
fx.mental_check()

