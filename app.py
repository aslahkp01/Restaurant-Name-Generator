import streamlit as st
import langchain_helper

st.title("🍽️ Restaurant Name Generator")

cuisine_options = ["Indian", "Italian", "Mexican", "American", "Arabic", "Other"]

selected_option = st.sidebar.selectbox("Pick a Cuisine", cuisine_options)

if selected_option == "Other":
    cuisine = st.sidebar.text_input("Enter your custom cuisine")
else:
    cuisine = selected_option

if cuisine:
    with st.spinner("Generating ideas..."):
        response = langchain_helper.generate_restaurant_name_and_items(cuisine)

    st.header(response['restaurant_name'])

    menu_items = response['menu_items'].split(",")

    st.write("### Menu Items")
    for item in menu_items:
        st.write("-", item.strip())