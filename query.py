import streamlit as st

def ask(label):
  answer = st.text_input(label)

def ask_area(label):
  answer = st.text_area(label)

def ask_chat(prompt):
  answer = st.chat_input(prompt)

def ask_alert(prompt):
  answer = input(prompt)

def three_choice(answer, prompt1, prompt2, prompt3, alignment):
  flex = st.container(horizontal=True, horizontal_alignment=alignment)
  for card in range(3):
    flex.button(prompt1)
    flex.button(prompt2)
    flex.button(prompt3)
