import streamlit as st
import pandas

st.title("Sohan's Data Log")

df = pandas.read_csv("patient1.csv", sep=";")
st.dataframe(df, width=1000,)

