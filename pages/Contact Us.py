import streamlit as st
from contactemail import send_email

st.header("Contact us")


with st.form(key="Email_form"):
    email = st.text_input("Enter email")
    message = st.text_area("Enter your message")
    button = st.form_submit_button("Submit")
    print(email)
    print(message)
    if button:
        message = f"""\
Subject: User submitted contact

From {email}:
    {message}

End of message
"""
        print(message)
        send_email(message)
        st.info("Email was sent!")

st.title("Or Call us at 82312 48021")

st.write("""Address: FJPG+FRQ, TPS Colony, Nagaram, Secunderabad, Telangana 501301""")
st.write("https://maps.app.goo.gl/yhp2c8UfMVH3oxdo7")