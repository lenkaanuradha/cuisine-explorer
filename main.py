import streamlit as st
st.title("Explore the most loved dishes and restaurants across India.")
cuisine = st.sidebar.selectbox("Select Cuisine", ["Mexican", "Italian", "Chinese", "Indian", "Thai"])
from langchain_helper import generate_dishes_and_restaurant
if cuisine:
    menu_items = generate_dishes_and_restaurant(cuisine)
    st.header(f"Dishes and Restaurant for {cuisine} Cuisine")
    st.write(menu_items)