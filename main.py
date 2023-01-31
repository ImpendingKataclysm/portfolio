import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=500)

with col2:
    st.title("Katie Janzen")
    content = """
    Hello, I'm Katie and I code in Python, JavaScript, Java and C. I am currently 
    studying web development and application development at BCIT.  I'm currently 
    based in Vancouver, BC.
    """
    st.info(content)

message = """
Below are some of the apps I have built in Python. Feel free to contact me!
"""
st.write(message)
