import streamlit as st
import pandas

st.set_page_config(layout="wide")

DATA_FILE = "data.csv"

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

col3, col4 = st.columns(2)
df = pandas.read_csv(DATA_FILE, sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
