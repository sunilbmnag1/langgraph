import streamlit as st

with st.chat_message('User'):
    st.text("Hello")

with st.chat_message('Assistant'):
    st.text("Hello, How can i help you today")

with st.chat_message('User'):
    st.text("My name is Sunil")

user_input = st.chat_input('Type here..')

if user_input:
    with st.chat_message('User'):
        st.text(user_input)