import streamlit as st
import pandas as pd

st.title("What's on your mind today?")
input_text = st.text_input("Ask anything")

#conditional logic with widegets

name = st.text_input("Enter your name:")
if st.button("Greet"):
    st.success(f"Hello, {name}!")

upload_file = st.file_uploader("upload a csv", type='csv')
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("**Bold**, *Italic*, 'code',[Link](https://streamlit.io)")

st.text_input("What's your name?")
st.text_area("Write something...")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range",0,100)
st.selectbox("Select a fruit", ["Apple", "Banana", "Mango"])
st.multiselect("choose toppings", ["cheese","Tomato", "Olives"])
st.radio("Pick one", ["Option A", "Option B"])
st.checkbox("I agree to the terms")

option = st.radio("Choose view", ["Show Chart", "Show Table"])
if option == "Show Chart":
    st.write("Chart would appear here")
else:
    st.write("Table would appear here")

with st.form("login_form"):
    username = st.text_input("usernaame")
    password = st.text_input("password", type="password")
    submitted = st.form_submit_button("Login")

    if submitted:
        st.success (f"Welcome, {username}!")

st.image("https://share.google/TSedNR3eJmknshovxs", caption="Sample Image", use_column_width=True)

st.video("https://youtu.be/gLxdMmB3yI4?si=9MIpilypBYMPSDLu")
st.sidebar.title("navigation")