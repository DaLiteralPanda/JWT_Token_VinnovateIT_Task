# TO RUN use `streamlit run jwt_task.py` in the terminal
import streamlit as st
import jwt


st.title("JWT Token Authentication")

import streamlit as st

# Create an empty container
placeholder = st.empty()

actual_user = "user"
actual_password = "password"
key = "VinnovateIT"
encoded_jwt_token = ""

# Insert a form in the container
with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

# Successful login attempt page 

if submit and user == actual_user and password == actual_password:
    # If the form is submitted and the user and password are correct,
    # clear the form/container and display a success message
    placeholder.empty()
    st.success("Login successful")
    st.write("Generating a JWT Token")
    encoded_jwt_token = jwt.encode({user:password}, key, algorithm = "HS256")
    st.write(f"{encoded_jwt_token} \n")


    

elif submit and user != actual_user and password != actual_password:
    st.error("Login failed")
else:
    pass

# if st.button("Decode"):
#     st.write(jwt.decode(encoded_jwt_token, key, algorithms = ["HS256"]))
