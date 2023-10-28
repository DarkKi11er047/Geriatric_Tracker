import streamlit as st
from PIL import Image

with st.form("upload-form"):
    l = st.file_uploader("Upload Medical Record",accept_multiple_files=False)
    st.form_submit_button("Upload")

    try:
        ls = Image.open(l)
        st.image(ls)
        st.success("File was Uploaded!")
    except AttributeError:
        pass


