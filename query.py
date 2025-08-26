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
    if flex.button(prompt1):
      answer = 1
    elif flex.button(prompt2):
      answer = 2
    elif flex.button(prompt3):
      answer = 3

def dialog_ask(title, caption):
    @st.dialog(title)
    def ask_input(caption):
        answer = st.text_input(caption)
    ask(caption)

def dialog_area(title, caption):
    @st.dialog(title)
    def ask_area(caption):
        answer = st.text_area(caption)
    ask(caption)

def dialog_chat(title, caption):
    @st.dialog(title)
    def ask(caption):
        answer = st.chat_input(caption)
    ask(caption)
