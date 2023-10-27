import streamlit as st

with st.form("upload-form", clear_on_submit=True):
    uploaded_file = st.file_uploader(model.upload_button_text_desc, accept_multiple_files=True,help=model.upload_help)
    submitted = st.form_submit_button(model.upload_button_text)

    if submitted and uploaded_file is not None:
        ret = self.upload_file(uploaded_file)

        if ret is not False:
            file_names = self.get_existing_file_names('docs/images/')

            annotation_index = self.get_annotation_index(annotation_selection, file_names)
            annotation_selection = placeholder_upload.selectbox(model.annotation_text, file_names,
                                                                index=annotation_index,
                                                                help=model.annotation_selection_help)
            st.session_state['annotation_index'] = annotation_index