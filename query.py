import streamlit as st

def ask(label):
  answer = st.text_input(label)

def ask_area(label):
  answer = st.text_area(label)

def ask_chat(prompt):
  answer = st.chat_input(prompt)

def ask_alert(prompt):
  answer = input(prompt)

