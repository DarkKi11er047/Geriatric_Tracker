import streamlit as st
import pandas as pd
from PIL import Image
import os

with st.form("upload-form"):
    l = st.file_uploader("Upload Medical Record",accept_multiple_files=False)
    st.form_submit_button("Upload")

    try:
        ls = Image.open(l)
        st.image(ls)
        with open(os.path.join("UploadedFiles",l.name),"wb") as file:
            file.write(l.getbuffer())
            st.success("File saved")
    except AttributeError:
        pass
