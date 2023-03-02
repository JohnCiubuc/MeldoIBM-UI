import streamlit as st
import pandas as pd


# if "textarea_vis" not in st.session_state:
    # st.session_state.textarea_vis = "visible"


text_input = st.empty()
txt = text_input.text_area('Text to :blue[analyze]', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, :blue[it was the season]: :+1: of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''', height=400)
#, label_visibility=st.session_state.textarea_vis

def button_callback():
    # st.session_state.textarea_vis="collapsed"
    if txt != '':
        text_input.empty()
        
    text_input_container.empty()
    
a = st.button('analyze', on_click=button_callback)

text_input_container = st.empty()
t = text_input_container.text_area("Enter something")

if t != "":
    text_input_container.empty()
    st.info(t)
    
    
if a:
    text_input.empty()
    text_input_container.empty()
    st.info(t)