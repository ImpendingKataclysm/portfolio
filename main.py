import streamlit as st
import pandas

st.set_page_config(layout="wide")

DATA_FILE = "data.csv"
IMAGE_FOLDER = "images/"

col1, col2 = st.columns(2)

with col1:
    st.image(f"{IMAGE_FOLDER}photo.png", width=500)

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

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv(DATA_FILE, sep=";")

with open(DATA_FILE) as file:
    data = file.readlines()

mid_index = int(len(data) / 2)

with col3:
    for index, row in df[:mid_index].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(IMAGE_FOLDER + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[mid_index:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(IMAGE_FOLDER + row["image"])
